import tkinter as tk
import tkinter.ttk as ttk
from custom_tk_utilities import EditableTreeview

from attribues import AttributesCreation
from attribues import AttributesUpdation
from methods import WidgetMethods


class OptionDisplay(tk.LabelFrame):
    def __init__(self, parent, widget, creation: int = 0, **options):
        super().__init__(parent, **options)

        self.widget = widget
        self.parent = parent

        if creation:
            self.attribute_class = AttributesCreation(self.widget)
        else:
            self.attribute_class = AttributesUpdation(self.widget)

    def get_data(self, func):
        return func()

    def add_Editable_Treeview(self, tree_parent, func):
        data = self.get_data(func)
        columns = ("Attributes", "Value")

        treeview = EditableTreeview(
            tree_parent,
            columns=columns,
            show="headings",
            data=data,
            non_editable_columns="#1",
        )
        return treeview

    def retrive_data_from_treeview(self, treeview):
        retrived_data = dict(
            treeview.item(i, "values") for i in treeview.get_children()
        )
        return retrived_data


class WidgetOptionDisplay(OptionDisplay):
    def __init__(self, parent, widget, creation, **options):
        super().__init__(parent, widget, creation, **options)

        self.tree = self.add_Editable_Treeview(
            tree_parent=self, func=self.attribute_class.retrive_widget_attributes
        )
        self.tree.pack(fill="y", expand=1)


class ManagerOptionDisplay(OptionDisplay):
    def __init__(self, parent, widget, creation, **options):
        super().__init__(parent, widget, creation, **options)

        self.manager_selection_button()

    def manager_selection_button(self):
        self.button_frame = tk.LabelFrame(self, text="Select Widget Manager")
        self.button_frame.pack(
            anchor="n",
            padx=10,
            pady=10,
        )

        self.tree = self.add_Editable_Treeview(
            tree_parent=self, func=self.attribute_class.retrive_place_attributes
        )

        self.RadioSelectedVar = tk.StringVar(self)

        self.selected_place = tk.Radiobutton(
            self.button_frame,
            text="Place",
            value="place",
            variable=self.RadioSelectedVar,
            command=self.update_treeview,
        )
        self.selected_place.pack(side="left", padx=10, pady=5, anchor="w", expand=0)
        self.selected_place.invoke()

        self.selected_grid = tk.Radiobutton(
            self.button_frame,
            text="Grid",
            value="grid",
            variable=self.RadioSelectedVar,
            command=self.update_treeview,
        )
        self.selected_grid.pack(side="left", padx=10, pady=5, anchor="center", expand=0)

        self.selected_pack = tk.Radiobutton(
            self.button_frame,
            text="Pack",
            value="pack",
            variable=self.RadioSelectedVar,
            command=self.update_treeview,
        )
        self.selected_pack.pack(side="left", padx=10, pady=5, anchor="e", expand=0)

        self.tree.pack(fill="x", padx=10, pady=10)

    def update_treeview(self):
        rows = self.tree.get_children()
        for item in rows:
            self.tree.delete(item)

        for values in getattr(
            self.attribute_class, f"retrive_{self.RadioSelectedVar.get()}_attributes"
        )():
            self.tree.insert("", tk.END, values=values)

    def get_selected_manager_and_tree(self):
        return self.RadioSelectedVar.get(), self.tree


class PreviewWidget(OptionDisplay, WidgetMethods):
    def __init__(
        self,
        parent,
        widget,
        widget_data_treeview_frame,
        widget_manager_frame,
        creation,
        **options,
    ):
        super().__init__(parent, widget, creation, **options)

        self.widget = widget
        self.data_treeview_frame = widget_data_treeview_frame
        self.data_treeview = self.data_treeview_frame.tree
        self.data_treeview.bind("<<TreeviewSelect>>", self.show_widget)

        self.widget_manager_frame = widget_manager_frame
        self.widget_treeview = self.widget_manager_frame.tree
        self.widget_treeview.bind("<<TreeviewSelect>>", self.show_widget)

        widget_options = self.data_treeview_frame.retrive_data_from_treeview(
            self.data_treeview
        )

        if "text" in widget_options:
            widget_options.update({"text": "Preview"})

        widget_options.pop("master")
        widget_options.pop("name")

        if not creation:
            self.widget = self.Tk_Widget_dict().get(self.widget.winfo_class())

        self.widget = self.widget(self, widget_options)
        self.widget.place(relx=0.5, rely=0.5)

    def show_widget(self, e):
        widget_options = self.data_treeview_frame.retrive_data_from_treeview(
            self.data_treeview
        )

        (
            manager,
            manager_options_tree,
        ) = self.widget_manager_frame.get_selected_manager_and_tree()
        manager_options = self.widget_manager_frame.retrive_data_from_treeview(
            manager_options_tree
        )

        manager_options.pop("in")

        self.update_widget(
            widget_refrence=self.widget,
            widget_manager=manager,
            widget_options=widget_options,
            manager_options=manager_options,
        )


class ImageEditor:
    pass


class BaseUI(tk.Toplevel, WidgetMethods):
    def __init__(self, parent, title, widget_name, notebook_frame, creation):
        super().__init__(parent)
        self.title(title)
        self.parent = parent
        self.state("zoomed")
        self.notebook_frame = notebook_frame
        self.creation = creation
        self.widget_name = widget_name

    def button_init(self):
        submit_button = ttk.Button(self, text="Submit", command=self.submit_data)
        submit_button.pack(side="bottom", pady=10, ipadx=50)

        self.widget_option_frame = WidgetOptionDisplay(
            parent=self,
            widget=self.widget_name,
            text="Widget Options",
            creation=self.creation,
        )
        self.widget_option_frame.pack(
            side="left", fill="y", ipadx=10, ipady=10, padx=10, pady=10
        )

        self.mgr_option_frame = ManagerOptionDisplay(
            parent=self,
            widget=self.widget_name,
            text="Manager Options",
            creation=self.creation,
        )

        self.widget_preview_frame = PreviewWidget(
            parent=self,
            widget=self.widget_name,
            widget_data_treeview_frame=self.widget_option_frame,
            widget_manager_frame=self.mgr_option_frame,
            text="Preview",
            creation=self.creation,
        )
        self.widget_preview_frame.pack(
            side="left", fill="both", ipadx=10, ipady=10, padx=10, pady=10, expand=1
        )

        self.mgr_option_frame.pack(
            side="left", anchor="n", fill="x", ipadx=10, ipady=10, padx=10, pady=10
        )

    def submit_data(self):
        widget_options = self.widget_option_frame.retrive_data_from_treeview(
            self.widget_option_frame.tree
        )

        manager_options = self.mgr_option_frame.retrive_data_from_treeview(
            self.mgr_option_frame.tree
        )

        if self.creation:
            self.create_widget(
                widget_name=self.widget_name,
                widget_manager=self.mgr_option_frame.get_selected_manager_and_tree()[0],
                widget_options=widget_options,
                manager_options=manager_options,
                baseroot= self.parent,
                frame=self.notebook_frame
            )
        else:
            self.update_widget(widget_refrence=self.widget_name,
                widget_manager=self.mgr_option_frame.get_selected_manager_and_tree()[0],
                widget_options=widget_options,
                manager_options=manager_options,
                root=self.notebook_frame)


class Creation_UI(BaseUI):
    def __init__(self, parent, title, widget_name, notebook_frame):
        super().__init__(parent, title, widget_name, notebook_frame, creation=1)
        self.button_init()


class Updation_UI(BaseUI):
    def __init__(self, parent, title, widget_name):
        super().__init__(parent, title, widget_name, creation=0)
        self.button_init()


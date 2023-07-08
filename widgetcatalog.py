import tkinter as tk
import tkinter.ttk as ttk

from custom_tk_utilities import DropdownButton
from methods import WidgetMethods
from Create_Update_UI import Creation_UI
from workspace import Workspace


class WidgetCatalog(
    tk.Toplevel, WidgetMethods
):  # An top level widget to create new widget in workspace.
    def __init__(self, parent, workspace_obj):  # Properties of TopLevel Window
        tk.Toplevel.__init__(self, parent)

        self.title("Create Widgets")
        self.resizable(0, 0)
        self.workspace_obj = workspace_obj
        self.parent = parent
        self.Button_Holder()

    def Button_Holder(self):  # Contains Buttons which displays All widgets
        Create_Btn_frame = tk.Frame(self)

        tk_frame = self.tk_catalog_frame()
        tk_frame.pack()

        self.Create_Tk_widget_btn = DropdownButton(
            Create_Btn_frame,
            tk_frame,
            on_press_command=self.tk_on_press,
            on_release_command=self.tk_on_release,
            ttk_btn=1,
            text="Create Tk Widget",
        )
        self.Create_Tk_widget_btn.pack(side="left", padx=10, pady=5)

        ttk_frame = self.ttk_catalog_frame()
        ttk_frame.pack()

        self.Create_Ttk_widget_btn = DropdownButton(
            Create_Btn_frame,
            ttk_frame,
            on_press_command=self.ttk_on_press,
            on_release_command=self.ttk_on_release,
            ttk_btn=1,
            text="Create Ttk Widget",
        )
        self.Create_Ttk_widget_btn.pack(padx=10, side="right", pady=5)

        self.Execute_code_btn = ttk.Button(Create_Btn_frame, text="Execute code")
        self.Execute_code_btn.pack(padx=10, pady=5)

        Create_Btn_frame.pack()

    def _widget_button_function(self, widget_class):
        notebook_frame = self.workspace_obj.get_current_frame_tcl_name()
        notebook_frame = self.parent.nametowidget(notebook_frame)
        Creation_UI(
                    parent=self.parent, title="Create Widget", widget_name=widget_class, notebook_frame=notebook_frame
                ),
    def _GridWidget_catalog(
        self, FrameName, widget_dict
    ):  # Creates Buttons for each widget in widget_dict.
        r, c = 0, 0
        for key, value in widget_dict.items():
            if c == 5:
                r += 1
                c = 0

            tk.Button(
                FrameName,
                text=key,
                bg="#008cba",
                fg="white",
                border=0,
                width=20,
                command=lambda widget_class=value: self._widget_button_function(widget_class=widget_class)
            ).grid(row=r, column=c, padx=5, pady=5)

            c += 1

    def tk_catalog_frame(self):
        TK_Catalog_Frame = tk.LabelFrame(self, name="tk_cf", text="TK Widget Catalog")
        self._GridWidget_catalog(TK_Catalog_Frame, self.Tk_Widget_dict())
        return TK_Catalog_Frame

    def ttk_catalog_frame(self):
        TtK_Catalog_Frame = tk.LabelFrame(
            self, name="ttk_cf", text="TTK Widget Catalog"
        )
        self._GridWidget_catalog(TtK_Catalog_Frame, self.Ttk_Widget_dict())
        return TtK_Catalog_Frame

    def tk_on_press(self):
        self.Create_Ttk_widget_btn.config(state="disabled")
        self.Execute_code_btn.config(state="disabled")

    def tk_on_release(self):
        self.Create_Ttk_widget_btn.config(state="active")
        self.Execute_code_btn.config(state="active")

    def ttk_on_press(self):
        self.Create_Tk_widget_btn.config(state="disabled")
        self.Execute_code_btn.config(state="disabled")

    def ttk_on_release(self):
        self.Create_Tk_widget_btn.config(state="active")
        self.Execute_code_btn.config(state="active")

    def execute_code_on_press(self):
        self.Create_Ttk_widget_btn.config(state="disabled")
        self.Create_Tk_widget_btn.config(state="disabled")

    def execute_code_tk_on_release(self):
        self.Create_Ttk_widget_btn.config(state="active")
        self.Create_Tk_widget_btn.config(state="active")

def demo():
    root = tk.Tk()
    WidgetCatalog(root)
    root.mainloop()
    
if __name__ == "__main__":
    demo()

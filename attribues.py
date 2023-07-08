import tkinter as tk
import tkinter.ttk as ttk


class Attributes:
    def __init__(self, widget_name):
        self.widget_name = widget_name

    def retrive_widget_attributes(self, widget):
        attribute = [i for i in widget.keys()]
        attribute_value_list = [widget.cget(i) for i in attribute]
        attributes_list = list(zip(attribute, attribute_value_list))
        attributes_list.insert(0, ("master", f"{widget.winfo_parent()}"))
        attributes_list.insert(
            1,
            (
                "name",
                widget.nametowidget(widget),
            ),
        )

        return attributes_list

    def retrive_pack_attributes(self, widget):
        if widget.winfo_manager() != "pack":
            widget.pack()

        pack_attributes = widget.pack_info().items()

        return pack_attributes

    def retrive_grid_attributes(self, widget):
        if widget.winfo_manager() != "grid":
            widget.grid()

        grid_attributes = widget.grid_info().items()
        widget.destroy()

        return grid_attributes

    def retrive_place_attributes(self, widget):
        if widget.winfo_manager() != "place":
            widget.place(x=0, y=0)

        place_attributes = widget.place_info().items()
        return place_attributes


class AttributesCreation(Attributes):
    def __init__(self, widget_name):
        super().__init__(widget_name)

    def _init_dummy_widget_refrence(self):
        """Intializes Dummy Widget used for creating widget"""
        self.dummy_widget_refrence = self.widget_name()

        return self.dummy_widget_refrence

    def _destroy_dummy_widget_refrence(self):
        self.dummy_widget_refrence.destroy()

    def retrive_widget_attributes(self):
        widget = self._init_dummy_widget_refrence()
        widget_attributes = super().retrive_widget_attributes(widget)
        self._destroy_dummy_widget_refrence()

        return widget_attributes

    def retrive_place_attributes(self):
        widget = self._init_dummy_widget_refrence()
        place_attributes = super().retrive_place_attributes(widget)
        self._destroy_dummy_widget_refrence()

        return place_attributes

    def retrive_pack_attributes(self):
        widget = self._init_dummy_widget_refrence()
        pack_attributes = super().retrive_pack_attributes(widget)
        self._destroy_dummy_widget_refrence()

        return pack_attributes

    def retrive_grid_attributes(self):
        widget = self._init_dummy_widget_refrence()
        grid_attributes = super().retrive_grid_attributes(widget)
        self._destroy_dummy_widget_refrence()

        return grid_attributes

    def retrive_manager_options(self):
        mgr_options = [
            self.retrive_place_attributes(),
            self.retrive_pack_attributes(),
            self.retrive_grid_attributes(),
        ]
        return mgr_options


class AttributesUpdation(Attributes):
    def __init__(self, widget_refrence):
        super().__init__(widget_refrence)
        self.widget_refrence = self.widget_name

    def retrive_widget_attributes(self):
        widget_attributes = super().retrive_widget_attributes(self.widget_refrence)

        return widget_attributes

    def retrive_place_attributes(self):
        place_attributes = super().retrive_place_attributes(self.widget_refrence)

        return place_attributes

    def retrive_pack_attributes(self):
        pack_attributes = super().retrive_pack_attributes(self.widget_refrence)

        return pack_attributes

    def retrive_grid_attributes(self):
        grid_attributes = super().retrive_grid_attributes(self.widget_refrence)

        return grid_attributes

    def retrive_manager_options(self):
        mgr_options = [
            self.retrive_place_attributes(),
            self.retrive_pack_attributes(),
            self.retrive_grid_attributes(),
        ]
        return mgr_options

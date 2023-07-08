import tkinter as tk
from tkinter import ttk


class WidgetMethods:
    def create_widget(
        self,
        widget_name,
        widget_manager,
        widget_options: dict,
        manager_options: dict,
        baseroot,
        frame
    ):
        name = widget_options.get("name")
        if "." in widget_options.get("master"):
            # frame = widget.nametowidget(frame)
            widget_options.pop("master")
            widget_options.pop("name")
            w = widget_name(frame)

            for i, j in widget_options.items():
                        w[i] = j

        else:
            frame = baseroot.nametowidget(widget_options.get("master"))

            w =widget_name(frame)
            widget_options.pop("master")
            widget_options.pop("name")

            for i, j in widget_options.items():
                        w[i] = j
            
        

        getattr(w, widget_manager)(manager_options)

        print(w)

    def update_widget(
        self,
        widget_refrence,
        widget_manager,
        widget_options: dict,
        manager_options: dict,
    ):
        widget_options.pop("master")
        widget_options.pop("name")

        widget_refrence.configure(widget_options)
        getattr(widget_refrence, widget_manager)(manager_options)

    def Tk_Widget_dict(self):
        dict = {
            "Button": tk.Button,
            "Frame": tk.Frame,
            "Label": tk.Label,
            "Entry": tk.Entry,
            "Listbox": tk.Listbox,
            "Menubutton": tk.Menubutton,
            "Radiobutton": tk.Radiobutton,
            "Text": tk.Text,
            "Checkbutton": tk.Checkbutton,
            "Menu": tk.Menu,
            "LabelFrame": tk.LabelFrame,
            "PanedWindow": tk.PanedWindow,
            "SpinBox": tk.Spinbox,
            "Scrollbar": tk.Scrollbar,
            "Scale": tk.Scale,
            "Message": tk.Message,
            "Canvas": tk.Canvas,
        }
        return dict

    def Ttk_Widget_dict(self):
        dict = {
            "Button": ttk.Button,
            "Frame": ttk.Frame,
            "Label": ttk.Label,
            "Entry": ttk.Entry,
            "Menubutton": ttk.Menubutton,
            "Radiobutton": ttk.Radiobutton,
            "LabelFrame": ttk.LabelFrame,
            "PanedWindow": ttk.PanedWindow,
            "SpinBox": ttk.Spinbox,
            "Scrollbar": ttk.Scrollbar,
            "Scrollbar": ttk.Scrollbar,
            "Checkbutton": ttk.Checkbutton,
            "ComboBox": ttk.Combobox,
            "NoteBook": ttk.Notebook,
            "ProgressBar": ttk.Progressbar,
            "Separator": ttk.Separator,
            "Sizegrip": ttk.Sizegrip,
            "TreeView": ttk.Treeview,
        }

        return dict


class ErrorHanding:
    pass

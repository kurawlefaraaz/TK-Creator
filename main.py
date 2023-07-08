import tkinter as tk
import tkinter.ttk as ttk

from menubar import MenuBar
from workspace import Workspace
from widgetcatalog import WidgetCatalog


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Workspace")
        self.state("zoomed")
        self.config(bg="#404040")

        s = ttk.Style()
        # s.theme_use("clam")

        self.menubar()
        self.workspace()
        self.catalog_window()
    
    def catalog_window(self):
        catalog = WidgetCatalog(self, workspace_obj=self.workspace_widget)

    def menubar(self):
        MenuBar(self)

    def workspace(self):

        self.workspace_widget = Workspace(self)
        self.workspace_widget.pack(fill="both", expand=1, padx=5, pady=5)



if __name__ == "__main__":
    A = GUI()
    A.mainloop()

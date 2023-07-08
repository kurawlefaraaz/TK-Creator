import tkinter as tk
class MenuBar(tk.Menu):
    # Located at top
    def __init__(self, parent, **options):
        super().__init__(parent, options)
        self.root = parent

        self.root.config(menu=self)

        self.FileMenu()

    def FileMenu(self):
        file_menu = tk.Menu(master=self)
        file_menu.add_command(
        label='Exit',
    command=self.root.destroy,
)
        self.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

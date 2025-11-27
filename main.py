import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()


    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="add.png")
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog,
                                    bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)
        
        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'ui', 'norm'),
                                 height=15, show='headings')
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('ui', width=150, anchor=tk.CENTER)
        self.tree.column('norm', width=100, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='Наименование')
        self.tree.heading('ui', text='Ед.изм.')
        self.tree.heading('norm', text='Норма времени')

        self.tree.pack()


    def open_dialog(self):

        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
    def init_child(self):
        self.title('Добавить')
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'ui', 'norm'),
                                 height=15, show='headings')
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('ui', width=150, anchor=tk.CENTER)
        self.tree.column('norm', width=100, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='Наименование')
        self.tree.heading('ui', text='Ед.изм.')
        self.tree.heading('norm', text='Норма времени')

        self.tree.pack()
        self.grab_set()
        self.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Household finance")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
#https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
from   tkinter              import  ttk
import tkinter              as      tk
import tkinter.filedialog   as      tkFileDialog
import tkinter.simpledialog as      tkSimpleDialog


class Navbar(tk.Frame): 
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window1', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Toolbar(tk.Frame): 
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window1', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Statusbar(tk.Frame): 
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window1', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar  = Statusbar(self)
        self.toolbar    = Toolbar(self)
        self.navbar     = Navbar(self)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")

if __name__ == "__main__":
    GUI = tk.Tk()
    MainApplication(GUI).pack(side="top", fill="both", expand=True)
    GUI.mainloop()

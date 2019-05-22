#https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application

from   tkinter              import  ttk
import tkinter              as      Tk
import tkinter.filedialog   as      tkFileDialog
import tkinter.simpledialog as      tkSimpleDialog

END = Tk.END                                

class MainApplication(Tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        Tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

if __name__ == "__main__":
    GUI = Tk.Tk()
    MainApplication(GUI).pack(side="top", fill="both", expand=True)
    GUI.mainloop()

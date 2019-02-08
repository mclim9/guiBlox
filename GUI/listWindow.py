from initGui    import theme
from tkinter    import ttk
import tkinter  as Tk
import sys
END = Tk.END

class listWindow:
    def __init__(self, master):
        self.master = master
        self.frame = Tk.Frame(master)
        self.listWindow = Tk.Text(self.frame,bg=master.clr['txtBg'], fg=master.clr['txtFg'])
        self.scrlWindow = ttk.Scrollbar(self.frame, orient=Tk.VERTICAL,command=self.listWindow.yview)  #Create scrollbar

        self.listWindow.grid(row=0,column=0,sticky=(Tk.E))
        self.scrlWindow.grid(column=1,row=0,sticky=(Tk.W,Tk.N,Tk.S))

        self.frame.grid()
    
    def stdOut(self):
        sys.stdout = StdoutRedirector(self.listWindow)

    def clear(self):
        self.listWindow.delete(0.0,END)

    def wwrite(self,inStr):
        self.listWindow.insert(END,inStr+'\n')
        self.listWindow.see(END)
        self.master.update()

class StdoutRedirector(object):
    def __init__(self,text_area):
        self.text_area = text_area

    '''A class for redirecting stdout to this Text widget.'''
    def write(self,str):
        self.text_area.insert("end", str)

if __name__ == '__main__':
    root = theme().addColor()
    app = listWindow(root)                     #pylint: disable=unused-variable
    app.stdOut()
    print(1234)
    root.mainloop()

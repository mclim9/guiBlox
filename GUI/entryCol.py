import tkinter  as tk
from initGui    import theme
import sys

class entryCol:
    def __init__(self, master, names):
        self.master = master
        self.frame = tk.Frame(master)
        for i,label in enumerate(names):
            setattr(self, f'label{i}', tk.Label(self.frame,width=15, bg=master.clr['appBg'], fg=master.clr['appFg'], text=label))
            getattr(self,f'label{i}').grid(row=i,column=0)
            setattr(self, f'entry{i}', tk.Entry(self.frame,width=15, bg=master.clr['txtBg'], fg=master.clr['txtFg']))
            getattr(self,f'entry{i}').grid(row=i,column=1)
        self.frame.grid()

if __name__ == '__main__':
    root = theme().addColor()
    app = entryCol(root,['asdf','sdfg'])                     #pylint: disable=unused-variable
    root.mainloop()

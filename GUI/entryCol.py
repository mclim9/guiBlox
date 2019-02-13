import tkinter  as tk
from initGui    import theme
import sys

class entryCol:
    def __init__(self, master, names):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.config(bg=master.clr['appBg'])
        for i,key in enumerate(names):
            setattr(self, f'label{i}', tk.Label(self.frame,width=15, bg=master.clr['appBg'], fg=master.clr['appFg'], text=key))
            getattr(self,f'label{i}').grid(row=i,column=0)
            setattr(self, f'entry{i}', tk.Entry(self.frame,width=15, bg=master.clr['txtBg'], fg=master.clr['txtFg']))
            getattr(self,f'entry{i}').insert(tk.END,names[key])
            getattr(self,f'entry{i}').grid(row=i,column=1)
            getattr(self,'frame').grid_rowconfigure(i, weight=1)
        self.frame.grid(column=1,sticky="nsew")
#        self.frame.grid_columnconfigure(1, weight=1)
    def save(self):
        outDict = {}
        childList = self.frame.winfo_children()
        for child in childList:
            if type(child) == tk.Entry:
                outDict[child._name] = child.get()
        return outDict

if __name__ == '__main__':
    root = theme().addColor()
    root.geometry(f'{300}x{300}')
    dictIn = {} 
    dictIn['FreqStart']     = '24e9'
    dictIn['FreqStop']      = '39e9'
    
    app = entryCol(root,dictIn)                     #pylint: disable=unused-variable
    app.frame.config(width=100)
    app.frame.grid(row=0,column=0,sticky="ns")
    asdf = app.save()
    root.mainloop()

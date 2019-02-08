import tkinter  as tk
from initGui    import theme

import sys

class buttonRow:
    def __init__(self, master, iNum):
        self.master = master
        self.frame = tk.Frame(self.master)
        for i in range(iNum):
            setattr(self, f'button{i}', tk.Button(self.frame, text=f'Button{i}', width=15, command=self.new_window))
            getattr(self,f'button{i}').config(bg=master.clr['appBg'],fg=master.clr['appFg'])
            getattr(self,f'button{i}').grid(row=0,column=i)
        if 1:   #Quit Button
            setattr(self, f'button{i+1}', tk.Button(self.frame, text=f'Quit', width=15, command=self.GUI_quit))
            getattr(self,f'button{i+1}').config(bg='red2',fg=master.clr['appFg'])
            getattr(self,f'button{i+1}').grid(row=0,column=i+1)
        self.frame.grid()

    def GUI_quit(self):
        self.master.quit()
        self.master.destroy()


    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Popup(self.newWindow)

class Popup:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.grid()
        self.frame.grid()
    def close_windows(self):
        self.master.destroy()

if __name__ == '__main__':
    root = theme().addColor()
    app = buttonRow(root,6)                     #pylint: disable=unused-variable
    root.mainloop()

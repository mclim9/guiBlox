import tkinter as tk

class theme:
    def __init__(self):
        pass
        
    def addColor(self):
        self = tk.Tk()
        self.clr = {}
        self.clr['txtFg']    = "green2"
        self.clr['txtBg']    = "black" 
        self.clr['appFg']    = 'white'
        self.clr['appBg']    = "grey30"
        return self

if __name__ == '__main__':
    app = theme().addColor()
    app.mainloop()

#https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application

import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window1', width = 25, command = self.new_window)
        self.button2 = tk.Button(self.frame, text = 'New Window2', width = 25, command = self.new_window)
        self.button1.grid(row=0,column=0)
        self.button2.grid(row=1,column=1)
        self.frame.grid()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.grid()
        self.frame.grid()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)   #pylint: disable=unused-variable
    root.mainloop()

if __name__ == '__main__':
    main()
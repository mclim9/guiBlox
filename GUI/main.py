import tkinter as tk

from buttonRow  import buttonRow
from entryCol   import entryCol
from initGui    import theme
from listWindow import listWindow

def testprint1():
    print("root.entryCol.entry0.text")

def testprint2(root):
    print(root.entryCol.entry0.get())

def testprint3(root):
    root.listWind.wwrite('asdf')

def main(): 
    root = theme().addColor()

    ### Create Sections
    root.buttnRow = buttonRow(root, 3)                     #pylint: disable=unused-variable
    root.entryCol = entryCol(root, ['SMW IP','FSW IP','Freq Start','Freq Stop','Freq Step'])
    root.toppWind = listWindow(root)
    root.bottWind = listWindow(root)
    root.bottWind.stdOut()                                  #Stdout --> window

    ### Define Sections
    root.buttnRow.button0.config(text='foo',command=testprint1)
    root.buttnRow.button1.config(text='bar',command=lambda: testprint2(root))
    root.buttnRow.button2.config(text='baz',command=lambda: testprint3(root))
    root.toppWind.listWindow.config(height=10,width=60)
    root.bottWind.listWindow.config(height= 5,width=85)
    root.buttnRow.frame.config(width=85)

    ### Grid Sections
    root.entryCol.frame.grid(row=0,column=0,sticky=(tk.N,tk.S))
    root.toppWind.frame.grid(row=0,column=1)
    root.bottWind.frame.grid(row=1,column=0,columnspan=2)
    root.buttnRow.frame.grid(row=2,column=0,columnspan=2,sticky=(tk.W,tk.E))
    root.mainloop()

if __name__ == '__main__':
    main()
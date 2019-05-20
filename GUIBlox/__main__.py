#####################################################################
### Purpose: Object Oriented Python Tkinter example
### Author : Martin C Lim
### Date   : 2019.02.01
### Objects:
#####################################################################
### User Inputs
#####################################################################
entryDict = {} 
entryDict['Entry1']     = '192.168.1.114'
entryDict['Entry2']     = '192.168.1.114'
entryDict['Entry3']     = 'spam.ham.eggs'

#####################################################################
### OOGUI Import 
#####################################################################
from GUIBlox                    import buttonRow, entryCol, theme, listWindow

#####################################################################
### Function Definition
#####################################################################
def buttonfunc1(root):
    root.bottWind.writeH('Highlight')
    pass

def buttonfunc2(root):
    root.bottWind.clear()
    
def buttonfunc3(root):
    root.bottWind.writeN('Normal')
    print('Print works too')

#####################################################################
### GUI Layout
#####################################################################
def main(): 
    root = theme().addColor()
    root.title('GUI Example')

    ### Create GUI Elements
    root.entryCol = entryCol(root, entryDict)
    root.toppWind = listWindow(root)
    root.bottWind = listWindow(root)
    root.bottWind.stdOut()                                  #Stdout --> window
    root.buttnRow = buttonRow(root, 3)                      #pylint: disable=unused-variable

    ### Assign Functions
    root.entryCol.frame.config(width=100)
    root.toppWind.listWindow.config(height=10,width=40)
    root.bottWind.listWindow.config(height= 5,width=66)
    root.buttnRow.button0.config(text='foo'  ,command=lambda: buttonfunc1(root))     #pylint: disable=E1101
    root.buttnRow.button1.config(text='clear',command=lambda: buttonfunc2(root))     #pylint: disable=E1101
    root.buttnRow.button2.config(text='baz'  ,command=lambda: buttonfunc3(root))     #pylint: disable=E1101

    ### Place into root
    root.grid_rowconfigure(2, weight=1)
    root.entryCol.frame.grid(row=0,column=0,sticky="ns")
    root.toppWind.frame.grid(row=0,column=1)
    root.bottWind.frame.grid(row=1,column=0,columnspan=2)
    root.buttnRow.frame.grid(row=2,column=0,columnspan=2,sticky="nsew")
    root.mainloop()

if __name__ == '__main__':
    main()
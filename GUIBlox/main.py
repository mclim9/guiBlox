#####################################################################
### Purpose: Object Oriented Python Tkinter example
### Author : Martin C Lim
### Date   : 2019.02.01
### Objects:
#####################################################################
### User Inputs
#####################################################################
entryDict = {} 
entryDict['SMW IP']     = '192.168.1.114'
entryDict['FSW IP']     = '192.168.1.114'
entryDict['Freq Start'] = '24e9'
entryDict['Freq Stop']  = '39e9'
entryDict['Freq Step']  = '500e6'

if 0:
    buttnDict = {}
    buttnDict['foo'] = lambda: testprint1(root) #pylint: disable=E0602
    buttnDict['bar'] = lambda: testprint2(root) #pylint: disable=E0602
    buttnDict['baz'] = lambda: testprint3(root) #pylint: disable=E0602

#####################################################################
### OOGUI Import 
#####################################################################
from GUIBlox.buttonRow  import buttonRow
from GUIBlox.entryCol   import entryCol
from GUIBlox.theme    import theme
from GUIBlox.listWindow import listWindow

#####################################################################
### Function Definition
#####################################################################
def testprint1(root):
    #print(f'asdf-{root.entryCol.entry0.get()}')
    #root.bottWind.clear()
    #root.bottWind.wwrite('asdf')
    root.bottWind.hwrite('asdfadsf')
    pass

def testprint2(root):
    root.bottWind.clear()
    
def testprint3(root):
    root.bottWind.wwrite('asdf')

#####################################################################
### GUI Layout
#####################################################################
def main(): 
    root = theme().addColor()
    root.title('GUI Example')

    ### Create Sections
    root.entryCol = entryCol(root, entryDict)
    root.toppWind = listWindow(root)
    root.bottWind = listWindow(root)
    root.bottWind.stdOut()                                  #Stdout --> window
    root.buttnRow = buttonRow(root, 3)                      #pylint: disable=unused-variable

    ### Define Sections
    root.entryCol.frame.config(width=100)
    root.toppWind.listWindow.config(height=10,width=40)
    root.bottWind.listWindow.config(height= 5,width=66)
#    for i,key in enumerate(buttnDict):
#        getattr(root.buttnRow,f'button{i}').config(text=f'{key}', command=lambda: buttnDict[key]())
    root.buttnRow.button0.config(text='foo'  ,command=lambda: testprint1(root))     #pylint: disable=E1101
    root.buttnRow.button1.config(text='clear',command=lambda: testprint2(root))     #pylint: disable=E1101
    root.buttnRow.button2.config(text='baz'  ,command=lambda: testprint3(root))     #pylint: disable=E1101

    ### Grid Sections
    root.grid_rowconfigure(2, weight=1)
    root.entryCol.frame.grid(row=0,column=0,sticky="ns")
    root.toppWind.frame.grid(row=0,column=1)
    root.bottWind.frame.grid(row=1,column=0,columnspan=2)
    root.buttnRow.frame.grid(row=2,column=0,columnspan=2,sticky="nsew")
    root.mainloop()

if __name__ == '__main__':
    main()
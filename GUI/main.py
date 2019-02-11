#####################################################################
### Purpose: Object Oriented Python Tkinter example
### Author : Martin C Lim
### Date   : 2019.02.01
### Objects:
#####################################################################
### User Inputs
#####################################################################
entryArry = ['SMW IP','FSW IP','Freq Start','Freq Stop','Freq Step']
buttnArry = {'foo':'testprint1(root)', \
             'bar':'testprint2(root)', \
             'baz':'testprint3(root)'}
#####################################################################
### OOGUI Import 
#####################################################################
from buttonRow  import buttonRow
from entryCol   import entryCol
from initGui    import theme
from listWindow import listWindow

#####################################################################
### Function Definition
#####################################################################
def testprint1(root):
    print(f'asdf-{root.entryCol.entry0.get()}')

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
    root.entryCol = entryCol(root, entryArry)
    root.toppWind = listWindow(root)
    root.bottWind = listWindow(root)
    root.bottWind.stdOut()                                  #Stdout --> window
    root.buttnRow = buttonRow(root, 3)                      #pylint: disable=unused-variable

    ### Define Sections
    root.entryCol.frame.config(width=100)
    root.toppWind.listWindow.config(height=10,width=40)
    root.bottWind.listWindow.config(height= 5,width=66)
#    for i,key in enumerate(buttnArry):
#        getattr(root.buttnRow,f'button{i}').config(text=f'{key}', command=f'lambda: {buttnArry[key]}')
#    root.entryCol.save()
    root.buttnRow.button0.config(text='foo'  ,command=lambda: testprint1(root))
    root.buttnRow.button1.config(text='clear',command=lambda: testprint2(root))
    root.buttnRow.button2.config(text='baz'  ,command=lambda: testprint3(root))

    ### Grid Sections
    root.grid_rowconfigure(2, weight=1)
    root.entryCol.frame.grid(row=0,column=0,sticky="ns")
    root.toppWind.frame.grid(row=0,column=1)
    root.bottWind.frame.grid(row=1,column=0,columnspan=2)
    root.buttnRow.frame.grid(row=2,column=0,columnspan=2,sticky="nsew")
    root.mainloop()

if __name__ == '__main__':
    main()
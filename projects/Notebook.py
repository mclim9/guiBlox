"""Synchronize settings between FSW/SMW K144 5GNR personality"""
###############################################################################
### Import
###############################################################################
from tkinter.ttk        import Notebook, Frame
from guiblox            import theme, listWindow
# pylint: disable=bad-whitespace,invalid-name,line-too-long
###############################################################################
### User Inputs
###############################################################################
entryDict = {}          # Dict for entry column object
entryDict['Label1']     = 'Data1'
entryDict['Label2']     = 'Data2'
entryDict['Label3']     = 'Data3'

###############################################################################
### Code Import
###############################################################################

###############################################################################
### Function Definition
###############################################################################
def function(root):
    """Function"""
    print('Hello')

###############################################################################
### GUI Main
###############################################################################
def main():
    """main"""
    root = theme().addColor()
    root.title('Notebook Test Program')

    ###########################################################################
    ### guiBlox: Create Widgets
    ###########################################################################
    note = Notebook(root)
    tab1 = Frame(note)
    tab2 = Frame(note)
    tab3 = Frame(note)

    note.add(tab1, text = "Tab1")
    note.add(tab2, text = "Tab2")
    note.add(tab3, text = "Tab3")

    ###########################################################################
    ### guiBlox: Place Widgets
    ###########################################################################
    note.grid(row=0, column=0,sticky="nsew")
    root.mainloop()

if __name__ == '__main__':
    main()

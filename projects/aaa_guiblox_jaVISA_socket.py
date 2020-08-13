""" Purpose: Object Oriented Python Tkinter example"""
###############################################################################
### Import Statements
###############################################################################
#pylint: disable=E1101
from guiblox            import buttonRow, entryCol, theme, listWindow
from rssd.yaVISA_socket import jaVisa

###############################################################################
### User Inputs
###############################################################################
entryDict = {}          # Dict for entry column object
entryDict['Label1']     = '10.0.0.10'
entryDict['Label2']     = 'Data2'
entryDict['Label3']     = 'Data3'

###############################################################################
### Function Definition
###############################################################################
def buttonfunc1(root):
    """docstring"""
    txt = root.entryCol.entry0.get()
    root.bottWind.writeH(f'Highlight {txt}')

def buttonfunc2(root):
    """docstring"""
    root.bottWind.clear()

def buttonfunc3(root):
    """docstring"""
    root.bottWind.writeN('Normal')
    print('Print works too')

def IDN(tkEvent):
    """System ID (*IDN?) of ipAddy"""
    ipAddy = tkEvent.widget.get()
    print(f'IDN       : {ipAddy}')
    instr = jaVisa().jav_Open(ipAddy)
    print(instr.dataIDN)
    instr.jav_Close()

###############################################################################
### Main Function
###############################################################################
def main():
    """docstring"""
    ### guiblox: Create Tk GUI object
    root = theme().addColor()                           # Create GUI object
    root.title('guiblox Example')                       # Opt: Specify title
    root.resizable(0,0)                                 # Opt: Disables resizing
    root.geometry("600x300")                            # Opt: specify x/y size
    # root.iconbitmap('guiblox.ico')                    # Opt: specify icon

    ###########################################################################
    ### guiBlox: Create Widgets
    ###########################################################################
    root.entryCol = entryCol(root, entryDict)           # Create entry fields Col
    root.toppWind = listWindow(root)                    # Create top text box
    root.bottWind = listWindow(root)                    # Create bottom text box
    root.bottWind.stdOut()                              # Print --> bottWind
    root.buttnRow = buttonRow(root, 3)                  # pylint: disable=unused-variable

    ###########################################################################
    ### guiblox: Customize behavior
    ###########################################################################
    root.entryCol.frame.config(width=100)
    root.entryCol.chg2Enum('entry2', ['Opt1','Opt2'])   # Chg entry2 to pull down
    root.entryCol.entry2_enum.set('Opt1')               # entry2 default value
    root.entryCol.entry0.bind("<Double-Button-1>"  ,IDN)

    root.toppWind.listWindow.config(height=10,width=40)
    root.bottWind.listWindow.config(height= 5,width=66)
    root.buttnRow.button0.config(text='Get Data1'   ,command=lambda: buttonfunc1(root))     #pylint: disable=E1101
    root.buttnRow.button1.config(text='clear'       ,command=lambda: buttonfunc2(root))     #pylint: disable=E1101
    root.buttnRow.button2.config(text='Print Normal',command=lambda: buttonfunc3(root))     #pylint: disable=E1101

    ###########################################################################
    ### guiblox: draw elements
    ###########################################################################
    root.grid_rowconfigure(2, weight=1)
    root.entryCol.frame.grid(row=0,column=0,sticky="ns")
    root.toppWind.frame.grid(row=0,column=1,sticky='e')
    root.bottWind.frame.grid(row=1,column=0,columnspan=2)
    root.buttnRow.frame.grid(row=2,column=0,columnspan=2,sticky="nsew")
    root.mainloop()

if __name__ == '__main__':
    main()

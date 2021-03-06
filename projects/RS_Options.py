"""Display Rohde & Schwarz Instrument Options"""
# pylint: disable=bad-whitespace,invalid-name,line-too-long
###############################################################################
### Import
###############################################################################
import  datetime
import  os

from guiblox                import buttonRow, entryCol, theme, listWindow
from rssd.yaVISA_socket     import jaVisa
# from    tkinter             import messagebox

###############################################################################
### User Inputs
###############################################################################
SCPIWidth = 50
SCPIHeigh = 5

###############################################################################
### Function Definition
###############################################################################
def clrBottom(root):
    """Clear Bottom Window"""
    root.bottWind.clear()
    # root.bottWind.writeH('2xLt:IDN        Rt:SystError        2xRt:SystInfo')

def fopen():
    """Open File"""
    os.system('notepad.exe ' + __file__ + '.txt')

def fwrite(root):
    """Write data to file"""
    RS = gui_reader(root)
    f = open(__file__+'.txt', 'a')
    f.write(datetime.datetime.now().strftime("%y%m%d-%H:%M:%S.%f")+'\n')        #Date String
    f.write(RS.Output)
    print(f'Text Written to {__file__}')
    f.close()

def gui_reader(root):
    """Read values from GUI"""
    RS = lambda: None
    RS.IP1             = root.entryCol1.entry0.get()                            #pylint:disable=E1101
    RS.SCPI1           = root.SCPI1.getlist()
    RS.Output          = root.bottWind.getstr()
    return RS

def IDN(tkEvent):
    """System ID (*IDN?) of ipAddy"""
    ipAddy = tkEvent.widget.get()
    print(f'IDN       : {ipAddy}')
    instr = jaVisa().jav_Open(ipAddy)                                           #pylint:disable=E1101
    instr.jav_Close()

def SYSTERR(tkEvent):
    """System Error (SYST:ERR?) of ipAddy"""
    ipAddy = tkEvent.widget.get()
    print(f'SYS Err   : {ipAddy}')
    instr = jaVisa().jav_Open(ipAddy)                                           #pylint:disable=E1101
    instr.jav_ClrErr()
    print(f'SYS Err   : No Error')
    instr.jav_Close()

def SYSTNFO(tkEvent):
    """System Info (SYST:DFPR?) of ipAddy"""
    ipAddy = tkEvent.widget.get()
    print(f'SYS INFO  : {ipAddy}')
    instr = jaVisa().jav_Open(ipAddy)                                           #pylint:disable=E1101
    instr.query('SYST:DFPR?')
    instr.jav_Close()

def instr1(root):
    """Send SCPI cmds to instr1"""
    Output = ""
    RS = gui_reader(root)
    Instr = jaVisa()
    Instr.debug = 0
    Instr.jav_Open(RS.IP1)
    for scpi in RS.SCPI1:
        if '?' in scpi:
            rdStr = Instr.query(scpi)
            Output = Output + ', ' + rdStr
        else:
            Instr.write(scpi)
    Output = datetime.datetime.now().strftime("%y%m%d, %H:%M:%S.%f") + Output
    print(Output)
    f = open(__file__+'.txt', 'a')
    f.write(Output+'\n')
    f.close()
    Instr.jav_Close()

###############################################################################
### GUI Main
###############################################################################
def main():
    """main"""
    root = theme().addColor()
    root.title('Rohde & Schwarz Options')
    root.resizable(0, 0)

    ###########################################################################
    ### guiBlox: Create Widgets
    ###########################################################################
    root.entryCol1  = entryCol(root, {'Instr': '10.0.0.10'})
    root.SCPI1      = listWindow(root).writeN('*IDN?\n*OPT?\nSYST:DFPR?\n')

    root.bottWind   = listWindow(root)
    root.bottWind.stdOut()                                                          #Stdout --> window
    root.btnRowTop  = buttonRow(root, 1, makequit=0)                                #pylint: disable=unused-variable
    root.btnRowBot  = buttonRow(root, 3)                                            #pylint: disable=unused-variable
    clrBottom(root)

    ###########################################################################
    ### guiBlox: Customize Widgets
    ###########################################################################
    root.entryCol1.entry0.bind("<Double-Button-1>", IDN)                           #pylint: disable=E1101
    root.entryCol1.entry0.bind("<Button-3>",        SYSTERR)                       #pylint: disable=E1101
    root.entryCol1.entry0.bind("<Double-Button-3>", SYSTNFO)                       #pylint: disable=E1101

    root.SCPI1.listWindow.config(width=SCPIWidth, height=5)

    root.bottWind.listWindow.config(height= 15, width=(SCPIWidth))
    root.btnRowTop.button0.config(text='Query',     command=lambda: instr1(root))   #pylint: disable=E1101

    root.btnRowBot.button0.config(text='write File', command=lambda: fwrite(root))  #pylint: disable=E1101
    root.btnRowBot.button1.config(text='open File',  command=lambda: fopen())       #pylint: disable=E1101
    root.btnRowBot.button2.config(text='clear',      command=lambda: clrBottom(root))#pylint: disable=E1101

    ###########################################################################
    ### guiBlox: Place Widgets
    ###########################################################################
    root.grid_rowconfigure(2, weight=1)
    root.entryCol1.frame.grid(row=0, column=0, sticky="ns")
    root.SCPI1.frame.grid(row=1, column=0, sticky='ew')
    root.btnRowTop.frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
    root.bottWind.frame.grid(row=3, column=0, columnspan=2, sticky='nsew')
    root.btnRowBot.frame.grid(row=10, column=0, columnspan=2, sticky="nsew")

    root.mainloop()

if __name__ == '__main__':
    main()

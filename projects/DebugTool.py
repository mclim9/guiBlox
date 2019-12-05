###############################################################################
### Purpose: Object Oriented Python Tkinter example
### Author : Martin C Lim
### Date   : 2019.02.01
###############################################################################
### User Inputs
###############################################################################
SCPIWidth = 50
SCPIHeigh = 15
FSW_SCPI  = """:FETC:CC1:ISRC:FRAM:SUMM:EVM:ALL:AVER?
:FETC:CC1:ISRC:FRAM:SUMM:EVM:PCH:AVER?
:FETC:CC1:ISRC:FRAM:SUMM:EVM:PSIG:AVER?
:FETC:CC1:ISRC:FRAM:SUMM:FERR:AVER?
:FETC:CC1:ISRC:FRAM:SUMM:SERR:AVER?
:FETC:CC1:ISRC:FRAM:SUMM:IQOF:AVER?
:FETC:CC1:ISRC:FRAM:SUMM:GIMB:AVER?
:FETC:CC1:ISRC:FRAM:SUMM:QUAD:AVER?
:FETC:CC1:ISRC:FRAM:SUMM:OSTP:AVER?
:FETC:CC1:ISRC:FRAM:SUMM:POW:AVER?
:FETC:CC1:ISRC:SUMM:CRES:AVER?
"""

###############################################################################
### Code Import 
###############################################################################
from guiblox                import buttonRow, entryCol, theme, listWindow

### Code specific imports
from   rssd.yaVISA_socket   import jaVisa
import datetime
import socket
import os

###############################################################################
### Function Definition
###############################################################################
def clrBottom(root):
    root.bottWind.clear()
    # root.bottWind.writeH('2xLt:IDN        Rt:SystError        2xRt:SystInfo')

def fopen(root):
    os.system('notepad.exe ' + __file__ + '.txt')

def fwrite(root):
    RS = gui_reader(root)
    f = open(__file__+'.txt','a')
    f.write(datetime.datetime.now().strftime("%y%m%d-%H:%M:%S.%f")+'\n') #Date String
    f.write(RS.Output)
    print(f'Text Written to {__file__}')
    f.close()

def gui_reader(root):
    ### Read values from GUI
    RS = lambda: None
    RS.IP1             = root.entryCol1.entry0.get()                                 #pylint:disable=E1101
    RS.IP2             = root.entryCol2.entry0.get()                                 #pylint:disable=E1101
    RS.SCPI1           = root.SCPI1.getlist()
    RS.SCPI2           = root.SCPI2.getlist()
    RS.Output          = root.bottWind.getstr()
    return RS

def IDN(tkEvent):
    ipAddy = tkEvent.widget.get()
    print(f'IDN       : {ipAddy}')
    instr = jaVisa().jav_Open(ipAddy)                          #pylint:disable=E1101
    instr.jav_Close()

def SYSTERR(tkEvent):
    ipAddy = tkEvent.widget.get()
    print(f'SYS Err   : {ipAddy}')
    instr = jaVisa().jav_Open(ipAddy)                          #pylint:disable=E1101
    instr.jav_ClrErr()
    print(f'SYS Err   : No Error')
    instr.jav_Close()

def SYSTNFO(tkEvent):
    ipAddy = tkEvent.widget.get()
    print(f'SYS INFO  : {ipAddy}')
    instr = jaVisa().jav_Open(ipAddy)                          #pylint:disable=E1101
    instr.query('SYST:DFPR?')
    instr.jav_Close()

def instr1(root):
    Output = ""
    RS = gui_reader(root)
    Instr = jaVisa()
    Instr.debug = 0
    Instr.jav_Open(RS.IP1)
    for scpi in RS.SCPI1:
        if '?' in scpi: 
            rdStr = Instr.query(scpi)
            print(rdStr)
        else:
            Instr.write(scpi)
    Instr.jav_Close()

def instr2(root):
    Output = ""
    RS = gui_reader(root)
    Instr = jaVisa()
    Instr.debug = 0
    Instr.jav_Open(RS.IP2)
    for scpi in RS.SCPI2:
        if '?' in scpi: 
            rdStr = Instr.query(scpi)
            Output = Output + ',' + rdStr
        else:
            Instr.write(scpi)
    print(Output)
    Instr.jav_Close()

def MyIp():
    hostname = socket.gethostname()
    IPAddr   = socket.gethostbyname(hostname)
    print(f'{hostname}:{IPAddr}')
    WinOut = os.popen('arp -a | findstr "Interf"').read()
    print(WinOut)

###############################################################################
### GUI Main
###############################################################################
def main():
    global root
    root = theme().addColor()
    root.title('Socket Test Program')
    root.resizable(0,0)

    ###########################################################################
    ### guiBlox: Create Widgets
    ###########################################################################
    root.entryCol1  = entryCol(root, {'SMW-IP': '192.168.1.114'})
    root.entryCol2  = entryCol(root, {'FSW-IP': '192.168.1.109'})
    root.SCPI1      = listWindow(root).writeN('SYST:ERR?')
    root.SCPI2      = listWindow(root).writeN(FSW_SCPI)


    root.bottWind   = listWindow(root)
    root.bottWind.stdOut()                                                          #Stdout --> window
    root.btnRowTop  = buttonRow(root, 2,makequit=0)                                 #pylint: disable=unused-variable
    root.btnRowBot  = buttonRow(root, 4)                                            #pylint: disable=unused-variable
    clrBottom(root)

    ###########################################################################
    ### guiBlox: Customize Widgets
    ###########################################################################
    root.entryCol1.entry0.bind("<Double-Button-1>",IDN)                             #pylint: disable=E1101
    root.entryCol2.entry0.bind("<Double-Button-1>",IDN)                             #pylint: disable=E1101
    root.entryCol1.entry0.bind("<Button-3>",SYSTERR)                                #pylint: disable=E1101
    root.entryCol2.entry0.bind("<Button-3>",SYSTERR)                                #pylint: disable=E1101
    root.entryCol1.entry0.bind("<Double-Button-3>",SYSTNFO)                         #pylint: disable=E1101
    root.entryCol2.entry0.bind("<Double-Button-3>",SYSTNFO)                         #pylint: disable=E1101

    root.SCPI1.listWindow.config(width=SCPIWidth,height=SCPIHeigh)
    root.SCPI2.listWindow.config(width=SCPIWidth,height=SCPIHeigh)

    root.bottWind.listWindow.config(height= 10,width=(2*SCPIWidth+2))
    root.btnRowTop.button0.config(text='Query'  ,command=lambda: instr1(root))  #pylint: disable=E1101
    root.btnRowTop.button1.config(text='Query'  ,command=lambda: instr2(root))  #pylint: disable=E1101

    root.btnRowBot.button0.config(text='write File',command=lambda: fwrite(root))   #pylint: disable=E1101
    root.btnRowBot.button1.config(text='open File' ,command=lambda: fopen(root))    #pylint: disable=E1101
    root.btnRowBot.button2.config(text='clear'     ,command=lambda: clrBottom(root))#pylint: disable=E1101
    root.btnRowBot.button3.config(text='MyIP'      ,command=MyIp)                   #pylint: disable=E1101

    ###########################################################################
    ### guiBlox: Place Widgets
    ###########################################################################
    root.grid_rowconfigure(2, weight=1)
    root.entryCol1.frame.grid(row=0,column=0,sticky="ns")
    root.entryCol2.frame.grid(row=0,column=1,sticky="ns")
    root.SCPI1.frame.grid(row=1,column=0,sticky='ew')
    root.SCPI2.frame.grid(row=1,column=1,sticky='ew')
    root.btnRowTop.frame.grid(row=2,column=0,columnspan=3,sticky="nsew")
    root.bottWind.frame.grid(row=3,column=0,columnspan=3,sticky='nsew')
    root.btnRowBot.frame.grid(row=10,column=0,columnspan=3,sticky="nsew")

    root.mainloop()

if __name__ == '__main__':
    main()
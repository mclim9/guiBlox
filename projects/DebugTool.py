#####################################################################
### Purpose: Object Oriented Python Tkinter example
### Author : Martin C Lim
### Date   : 2019.02.01
### Objects:
#####################################################################
### User Inputs
#####################################################################

#####################################################################
### OOGUI Import 
#####################################################################
from guiblox                import buttonRow, entryCol, theme, listWindow

### Code specific imports
from   rssd.yaVISA_socket   import jaVisa
import datetime
import socket
import os

#####################################################################
### Function Definition
#####################################################################
def clearBottom(root):
    root.bottWind.clear()
    root.bottWind.writeH('2xLt-Click: IDN     Rt-Click: SystError     2xRt-Click: SystInfo')

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
    RS.IP3             = root.entryCol3.entry0.get()                                 #pylint:disable=E1101
    RS.SCPI1           = root.SCPI1.getlist()
    RS.SCPI2           = root.SCPI2.getlist()
    RS.SCPI3           = root.SCPI3.getlist()
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
    RS = gui_reader(root)
    Instr = jaVisa().jav_Open(RS.IP1)
    for scpi in RS.SCPI1:
        if '?' in scpi: 
            rdStr = Instr.query(scpi)
            print(rdStr)
        else:
            Instr.write(scpi)
    Instr.jav_Close()

def instr2(root):
    RS = gui_reader(root)
    Instr = jaVisa().jav_Open(RS.IP2)
    for scpi in RS.SCPI2:
        if '?' in scpi: 
            rdStr = Instr.query(scpi)
            print(rdStr)
        else:
            Instr.write(scpi)
    Instr.jav_Close()

def instr3(root):
    RS = gui_reader(root)
    Instr = jaVisa().jav_Open(RS.IP3)
    for scpi in RS.SCPI3:
        if '?' in scpi: 
            rdStr = Instr.query(scpi)
            print(rdStr)
        else:
            Instr.write(scpi)
    Instr.jav_Close()

def MyIp():
    hostname = socket.gethostname()
    IPAddr   = socket.gethostbyname(hostname)
    print(f'{hostname}:{IPAddr}')
    WinOut = os.popen('arp -a | findstr "Interf"').read()
    print(WinOut)

#####################################################################
### GUI Layout
#####################################################################
def main():
    global root
    root = theme().addColor()
    root.title('Socket Test Program')
    root.resizable(0,0)

    ### Create Sections
    root.entryCol1  = entryCol(root, {'IP1': '192.168.1.114'})
    root.entryCol2  = entryCol(root, {'IP2': '192.168.1.109'})
    root.entryCol3  = entryCol(root, {'IP3': '192.168.1.150'})
    root.SCPI1      = listWindow(root).writeN('SYST:ERR?')
    root.SCPI2      = listWindow(root).writeN('SYST:ERR?')
    root.SCPI3      = listWindow(root).writeN('SYST:ERR?')

    root.bottWind   = listWindow(root)
    root.bottWind.stdOut()                              #Stdout --> window
    root.buttnRow   = buttonRow(root, 3,makequit=0)                                 #pylint: disable=unused-variable
    root.bottbtnRow = buttonRow(root, 4)                                            #pylint: disable=unused-variable
    clearBottom(root)

    ### Define Sections
    root.entryCol1.entry0.bind("<Double-Button-1>",IDN)                             #pylint: disable=E1101
    root.entryCol2.entry0.bind("<Double-Button-1>",IDN)                             #pylint: disable=E1101
    root.entryCol3.entry0.bind("<Double-Button-1>",IDN)                             #pylint: disable=E1101
    root.entryCol1.entry0.bind("<Button-3>",SYSTERR)                                #pylint: disable=E1101
    root.entryCol2.entry0.bind("<Button-3>",SYSTERR)                                #pylint: disable=E1101
    root.entryCol3.entry0.bind("<Button-3>",SYSTERR)                                #pylint: disable=E1101
    root.entryCol1.entry0.bind("<Double-Button-3>",SYSTNFO)                         #pylint: disable=E1101
    root.entryCol2.entry0.bind("<Double-Button-3>",SYSTNFO)                         #pylint: disable=E1101
    root.entryCol3.entry0.bind("<Double-Button-3>",SYSTNFO)                         #pylint: disable=E1101

    root.SCPI1.listWindow.config(width=20,height=10)
    root.SCPI2.listWindow.config(width=20,height=10)
    root.SCPI3.listWindow.config(width=20,height=10)

    root.bottWind.listWindow.config(height= 10,width=66)
    root.buttnRow.button0.config(text='Inst1 SCPI'  ,command=lambda: instr1(root))  #pylint: disable=E1101
    root.buttnRow.button1.config(text='Inst2 SCPI'  ,command=lambda: instr2(root))  #pylint: disable=E1101
    root.buttnRow.button2.config(text='Inst3 SCPI'  ,command=lambda: instr3(root))  #pylint: disable=E1101

    root.bottbtnRow.button0.config(text='write File',command=lambda: fwrite(root))  #pylint: disable=E1101
    root.bottbtnRow.button1.config(text='open File' ,command=lambda: fopen(root))   #pylint: disable=E1101
    root.bottbtnRow.button2.config(text='clear'     ,command=lambda: clearBottom(root))   #pylint: disable=E1101
    root.bottbtnRow.button3.config(text='MyIP'      ,command=MyIp)                          #pylint: disable=E1101

    ### Grid Sections
    root.grid_rowconfigure(2, weight=1)
    root.entryCol1.frame.grid(row=0,column=0,sticky="ns")
    root.entryCol2.frame.grid(row=0,column=1,sticky="ns")
    root.entryCol3.frame.grid(row=0,column=2,sticky="ns")
    root.SCPI1.frame.grid(row=1,column=0,sticky='ew')
    root.SCPI2.frame.grid(row=1,column=1,sticky='ew')
    root.SCPI3.frame.grid(row=1,column=2,sticky='ew')
    root.buttnRow.frame.grid(row=2,column=0,columnspan=3,sticky="nsew")
    root.bottWind.frame.grid(row=3,column=0,columnspan=3,sticky='nsew')
    root.bottbtnRow.frame.grid(row=10,column=0,columnspan=3,sticky="nsew")
    
    root.mainloop()

if __name__ == '__main__':
    main()
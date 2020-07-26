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
entryDict['FSW IP']     = '192.168.1.109'
entryDict['Freq Start'] = '24e9'
entryDict['Freq Stop']  = '39e9'
entryDict['Freq Step']  = '500e6'
entryDict['FSW Span']   = '10e6'
entryDict['SMW Pwr']    = '0'
entryDict['Filename']   = 'Output'

#####################################################################
### OOGUI Import
#####################################################################
import time
import os
from guiblox            import buttonRow, entryCol, theme, listWindow
from rssd.VST.Common    import VST           #pylint:disable=E0611,E0401
from rssd.FileIO        import FileIO

#####################################################################
### Function Definition
#####################################################################
def IDN(root):
    Instr = VST().jav_Open(root.entryCol.entry0.get(),root.entryCol.entry1.get())  #pylint:disable=E1101
    print(Instr.SMW.query('*IDN?'))
    print(Instr.FSW.query('*IDN?'))
    Instr.jav_Close()

def run(root):
    Instr = VST().jav_Open(root.entryCol.entry0.get(),root.entryCol.entry1.get())  #pylint:disable=E1101
    OFileCSV = FileIO().makeFile(root.entryCol.entry7.get()+'csv')
    OFileXML = FileIO().makeFile(root.entryCol.entry7.get()+'xml')

    root.toppWind.writeN('Sweep Begin')
    root.toppWind.writeN(f'-{Instr.SMW.Model} {Instr.SMW.Device} {Instr.SMW.Version} ')
    root.toppWind.writeN(f'-{Instr.FSW.Model} {Instr.FSW.Device} {Instr.FSW.Version} ')

    ##########################################################
    ### Instrument Settings
    ##########################################################
    FreqStart = int(float(root.entryCol.entry2.get()))
    FreqStop  = int(float(root.entryCol.entry3.get()))
    FreqStep  = int(float(root.entryCol.entry4.get()))
    fSpan     = float(root.entryCol.entry5.get())
    SWM_Out   = float(root.entryCol.entry6.get())

    Instr.SMW.Set_RFPwr(SWM_Out)                    #Output Power
    Instr.SMW.Set_IQMod('OFF')                      #Modulation Off
    Instr.SMW.Set_RFState('ON')                     #Turn RF Output on
    Instr.FSW.Set_Channel("Spectrum")
    Instr.FSW.Set_SweepCont(0)
    Instr.FSW.Set_Span(fSpan)

    for freq in range(FreqStart,FreqStop,FreqStep):
        Instr.Set_Freq(freq)
        time.sleep(0.01)
        Instr.FSW.Set_InitImm()
        Instr.FSW.Set_Mkr_Peak()
        Mkr = Instr.FSW.Get_Mkr_XY()
        OFileCSV.write(f'{freq},{Mkr[0]},{Mkr[1]}')
        OFileXML.write(f'  <Point x="{Mkr[0]}" y="{Mkr[1]}"/>')
    Instr.jav_Close()
    root.toppWind.writeN("Sweep Complete")

def openF(root):
    os.system(f'explorer.exe {os.path.abspath(os.path.dirname(__file__))}')

#####################################################################
### GUI Layout
#####################################################################
def main():
    root = theme().addColor()
    root.title('VSG VSA Frequency Sweep')

    ### Create Sections
    root.entryCol = entryCol(root, entryDict)
    root.toppWind = listWindow(root)
    root.bottWind = listWindow(root)
    root.bottWind.stdOut()                                  #Stdout --> window
    root.buttnRow = buttonRow(root, 3)                      #pylint: disable=unused-variable

    ### Define Sections
    root.entryCol.frame.config(width=50)
    root.toppWind.listWindow.config(height=20,width=40)
    root.toppWind.writeH("===Please Click Buttons Below===")

    root.bottWind.listWindow.config(height= 7,width=66)
    root.buttnRow.button0.config(text='*IDN?'   ,command=lambda: IDN(root))     #pylint: disable=E1101
    root.buttnRow.button1.config(text='Run'     ,command=lambda: run(root))     #pylint: disable=E1101
    root.buttnRow.button2.config(text='Folder'  ,command=lambda: openF(root))   #pylint: disable=E1101

    ### Grid Sections
    root.grid_rowconfigure(2, weight=1)
    root.entryCol.frame.grid(row=0,column=0,sticky="ns")
    root.toppWind.frame.grid(row=0,column=1,sticky='e')
    root.bottWind.frame.grid(row=1,column=0,columnspan=2,sticky='nsew')
    root.buttnRow.frame.grid(row=2,column=0,columnspan=2,sticky="nsew")
    root.mainloop()

if __name__ == '__main__':
    main()

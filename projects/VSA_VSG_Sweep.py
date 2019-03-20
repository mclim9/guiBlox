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
entryDict['Freq Step']  = '10e6'
entryDict['FSW Span']   = '10e6'
entryDict['SMW Pwr']    = '0'

#####################################################################
### OOGUI Import 
#####################################################################
from GUIBlox.buttonRow  import buttonRow
from GUIBlox.entryCol   import entryCol
from GUIBlox.theme      import theme
from GUIBlox.listWindow import listWindow

from rssd.VST_Common    import VST           #pylint:disable=E0611,E0401

#####################################################################
### Function Definition
#####################################################################
def IDN(root):
    VST = VST.jav_Open(root.entryCol.entry0.get(),root.entryCol.entry1.get())  #pylint:disable=E1101
    print(VST.SMW.query('*IDN?'))
    print(VST.FSW.query('*IDN?'))
    VST.jav_Close()
    
def run(root):
    VST = VST().jav_Open(root.entryCol.entry0.get(),root.entryCol.entry1.get())  #pylint:disable=E1101
    OFileCSV = FileIO().makeFile(__file__+'csv')
    OFileXML = FileIO().makeFile(__file__+'xml')

    ##########################################################
    ### Instrument Settings
    ##########################################################
    FreqStart = root.entryCol.entry2.get()
    FreqStop  = root.entryCol.entry3.get()
    FreqStep  = root.entryCol.entry4.get()
    fSpan     = root.entryCol.entry5.get()
    SWM_Out   = root.entryCol.entry6.get()

    VST.SMW.Set_RFPwr(SWM_Out)                    #Output Power
    VST.SMW.Set_RFState('ON')                     #Turn RF Output on
    VST.FSW.Set_SweepCont(0)
    VST.FSW.Set_Span(fSpan)

    for freq in range(FreqStart,FreqStop,FreqStep):
        VST.Set_Freq(freq)
        time.sleep(0.01)
        VST.FSW.Set_InitImm()
        VST.FSW.Set_Mkr_Peak()
        Mkr = VST.FSW.Get_Mkr_XY()
        OFileCSV.write(f'{freq},{Mkr[0]},{Mkr[1]}')
        OFileXML.write(f'  <Point x="{Mkr[0]}" y="{Mkr[1]}"/>')
    VST.jav_Close()

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
    root.buttnRow = buttonRow(root, 2)                      #pylint: disable=unused-variable

    ### Define Sections
    root.entryCol.frame.config(width=100)
    root.toppWind.listWindow.config(height=10,width=40)
    root.toppWind.writeH("===Please Click Buttons Below===")

    root.bottWind.listWindow.config(height= 5,width=66)
    root.buttnRow.button0.config(text='*IDN?'   ,command=lambda: IDN(root))     #pylint: disable=E1101
    root.buttnRow.button1.config(text='Run'     ,command=lambda: run(root))     #pylint: disable=E1101

    ### Grid Sections
    root.grid_rowconfigure(2, weight=1)
    root.entryCol.frame.grid(row=0,column=0,sticky="ns")
    root.toppWind.frame.grid(row=0,column=1,sticky='e')
    root.bottWind.frame.grid(row=1,column=0,columnspan=2)
    root.buttnRow.frame.grid(row=2,column=0,columnspan=2,sticky="nsew")
    root.mainloop()

if __name__ == '__main__':
    main()
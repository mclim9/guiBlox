########################################################################
# Title: Rohde & Schwarz Simple ATE example GUI
# Description:
#
########################################################################
# User Input Settings
########################################################################
ColxWid     = 60 -4
BotWindWid  = ColxWid + 15

entryDict = {} 
entryDict['SMW IP']         = '192.168.1.114'
entryDict['FSW IP']         = '192.168.1.109'
entryDict['Frequency']      = '28e9'
entryDict['SMW Power,RMS']  = '-5'
entryDict['Direction']      = 'UL'
entryDict['Freq Band']      = 'HIGH'
entryDict['Ch BW,MHz']      = '100'
entryDict['SubCarr,kHz']    = '60'
entryDict['RB']             = '132'
entryDict['RB Offset']      = '0'
entryDict['Modulation']     = 'QPSK'

########################################################################
### Code Import
########################################################################
from datetime                   import datetime
import tkinter                  as     Tk
import tkinter.filedialog       as     tkFileDialog
from guiblox                    import buttonRow, entryCol, theme, listWindow
END = Tk.END

#Code specific libraries
import copy
from rssd.VST.NR5G_K144         import VST          #pylint:disable=E0611,E0401

########################################################################
### GUIBlox Create items
########################################################################
GUI = theme().addColor()                            #Create GUI object
GUI.title('Rohde&Schwarz FSW SMW 5GNR Utility')     #GUI Title
topWind  = listWindow(GUI)
botWind  = listWindow(GUI)
buttnRow = buttonRow(GUI, 6)                        #pylint: disable=unused-variable
entryCol = entryCol(GUI, entryDict)

########################################################################
### GUI Functions
########################################################################
class GUIData(object):
    def __init__(self):
        self.List1 = ['- Utility does not validate settings against 3GPP 5G',
                    '- Click *IDN? to validate IP Addresses',
                    '- Frequency & SMW Power labels are clickable',
                    '']

def gui_reader():
    ### Read values from GUI
    SMW_IP          = entryCol.entry0.get()                 #pylint:disable=E1101
    FSW_IP          = entryCol.entry1.get()                 #pylint:disable=E1101

    ### Set 5GNR Parameters
    NR5G            = VST().jav_Open(SMW_IP,FSW_IP)         #pylint:disable=E1101
    NR5G.Freq       = float(entryCol.entry2.get())          #pylint:disable=E1101
    NR5G.SWM_Out    = float(entryCol.entry3.get())          #pylint:disable=E1101
    NR5G.NR_Dir     = entryCol.entry4_enum.get()            #pylint:disable=E1101
    NR5G.NR_Deploy  = entryCol.entry5_enum.get()            #pylint:disable=E1101
    NR5G.NR_ChBW    = int(entryCol.entry6_enum.get())       #pylint:disable=E1101
    NR5G.NR_SubSp   = int(entryCol.entry7_enum.get())       #pylint:disable=E1101
    NR5G.NR_RB      = int(entryCol.entry8.get())            #pylint:disable=E1101
    NR5G.NR_RBO     = int(entryCol.entry9.get())            #pylint:disable=E1101
    NR5G.NR_Mod     = entryCol.entry10_enum.get()           #pylint:disable=E1101
    NR5G.NR_TF      = 'OFF'
    return NR5G

def btn1():
    ### *IDN Query ###
    NR5G = VST().jav_Open(entryCol.entry0.get(),entryCol.entry1.get())  #pylint:disable=E1101
    print(NR5G.SMW.query('*IDN?'))
    print(NR5G.FSW.query('*IDN?'))
    NR5G.jav_Close()

def btn2():
    ### Display Max RB
    topWind.writeN('--------------------------    --------------------------')
    topWind.writeN('|u[<6GHz ]010 020 050 100|    |u[>6GHz ]050 100 200 400|')
    topWind.writeN('|-+------+---+---+---+---|    |-+------+---+---+---+---|')
    topWind.writeN('|0 015kHz|052 106 270 N/A|    |0 015kHz|N/A N/A N/A N/A|')
    topWind.writeN('|1 030kHz|024 051 133 273|    |1 030kHz|N/A N/A N/A N/A|')
    topWind.writeN('|2 060kHz|011 024 065 135|    |2 060kHz|066 132 264 N/A|')
    topWind.writeN('|3 120kHz|N/A N/A N/A N/A|    |3 120kHz|032 066 132 264|')
    topWind.writeN('--------------------------    --------------------------')
    topWind.writeN(' ')

    # NR5G = gui_reader()
    # data = NR5G.SMW.Get_5GNR_RBMax()
    # topWind.writeN("=== Max RB ===")
    # topWind.writeN("Mode: %s %sMHz"%(NR5G.SMW.Get_5GNR_FreqRange(),NR5G.SMW.Get_5GNR_ChannelBW()))
    # for i in data:
    #     topWind.writeN("SubC:%d  RB Max:%d"%(i[0],i[1]))
    # NR5G.jav_Close()

def btn3():
    ### Get EVM
    NR5G = gui_reader()
    NR5G.FSW.Set_InitImm()
    topWind.writeN(f'EVM: {NR5G.FSW.Get_5GNR_EVM():.4f}')
    NR5G.FSW.jav_Close()
    
def btn4():
    ### Set 5GNR Parameters
    NR5G = gui_reader()

    print("SMW Creating Waveform.")
    NR5G.Set_5GNR_All()
    print(NR5G.FSW.jav_ClrErr())
    print(NR5G.SMW.jav_ClrErr())
    print("SMW/FSW Setting Written")
    NR5G.jav_Close()

def btn5():
    ### Read 5GNR Parameters ###
    NR5G = gui_reader()

    K144Data = NR5G.Get_5GNR_All() 
    topWind.writeN(" ")
    botWind.writeH('Get_5GNR Differences                 ')
    for i in range(len(K144Data[0])):
        try:
            topWind.writeN("%s\t%s\t%s"%(K144Data[0][i],K144Data[1][i],K144Data[2][i]))
            if 'Direction'  in K144Data[0][i]:
                K144Data[1][i] = 'UL'   if K144Data[1][i] == 'UP' else 'DL'
            if 'FreqRange'  in K144Data[0][i]:
                K144Data[1][i] = 'HIGH' if K144Data[1][i] == 'GT6'  else K144Data[1][i]
                K144Data[1][i] = 'MIDD' if K144Data[1][i] == 'BT36' else K144Data[1][i]
                K144Data[1][i] = 'LOW'  if K144Data[1][i] == 'LT3'  else K144Data[1][i]
            if 'SubSpacing' in K144Data[0][i]:
                K144Data[1][i] = K144Data[1][i].replace('N','')
                K144Data[2][i] = K144Data[2][i].replace('SS','')
            if 'DMRS Config'in K144Data[0][i]:
                K144Data[1][i] = K144Data[1][i].replace('T','')
            if 'L_PTRS'     in K144Data[0][i]:
                K144Data[1][i] = K144Data[1][i].replace('TD','')
            if 'K_PTRS'     in K144Data[0][i]:
                K144Data[1][i] = K144Data[1][i].replace('FD','')
            if 'RE-offs'    in K144Data[0][i]:
                K144Data[1][i] = K144Data[1][i].replace('RE','')
                K144Data[2][i] = K144Data[2][i].replace('OS','')
            if K144Data[1][i] != K144Data[2][i]:
                botWind.writeH(f'{K144Data[0][i]}\t{K144Data[1][i]}\t{K144Data[2][i]}')
        except: 
            pass
    NR5G.jav_Close()

def btn6():
    ## filename: 5GNR_UL_BW_SubCar_Mod
    NR5G = gui_reader()
    dir = NR5G.SMW.Get_5GNR_Direction()
    filename = f'5GNR_{dir}_{NR5G.SMW.Get_5GNR_ChannelBW()}MHz_{NR5G.SMW.Get_5GNR_BWP_SubSpace()}kHz_{NR5G.SMW.Get_5GNR_BWP_Ch_Modulation()}'
    topWind.writeN(f'Writing: {filename}')
    NR5G.FSW.Set_5GNR_savesetting(filename)
    for i in range(1):
        NR5G.SMW.Set_5GNR_savesetting(filename+str(i))
    topWind.writeN('Writing: DONE!')

def click3(tkEvent):
    #print(tkEvent)
    NR5G = gui_reader()
    NR5G.SMW.Set_Freq(NR5G.Freq)
    NR5G.FSW.Set_Freq(NR5G.Freq)
    NR5G.jav_Close()
    botWind.writeN('SMW/FSW Freq: %d Hz'%NR5G.Freq)
    
def click4(tkEvent):
    #print(tkEvent)
    NR5G = gui_reader()
    NR5G.SMW.Set_RFPwr(int(NR5G.SWM_Out))
    NR5G.jav_Close()
    botWind.writeN('SMW RMS Pwr : %d dBm'%int(NR5G.SWM_Out))

def click14(tkEvent):
    #print(tkEvent)
    if 0:
        NR5G = gui_reader()
        if 0:
            NR5G.SMW.Set_5GNR_Direction(NR5G.NR_Dir)
            NR5G.SMW.Set_5GNR_BWP_ResBlock(NR5G.NR_RB)
            NR5G.SMW.Set_5GNR_BWP_Ch_ResBlock(NR5G.NR_RB)
            NR5G.FSW.Set_5GNR_Direction(NR5G.NR_Dir)
            NR5G.FSW.Set_5GNR_BWP_ResBlock(NR5G.NR_RB)
            NR5G.FSW.Set_5GNR_BWP_Ch_ResBlock(NR5G.NR_RB)
        NR5G.jav_Close()
    botWind.writeN('FSW:Signal Description-->RadioFrame-->BWP Config-->RB')
    botWind.writeN('FSW:Signal Description-->RadioFrame-->PxSCH Config-->RB')
    botWind.writeN('SMW:User/BWP-->UL BWP-->RB')
    botWind.writeN('SMW:Scheduling-->PxSCH-->RB')

def click15(tkEvent):
    botWind.writeN('FSW:Signal Description-->RadioFrame-->BWP Config-->RB Offset')
    botWind.writeN('SMW:User/BWP-->UL BWP-->RB Offset')
    pass

def clearTopWind(tkEvent):
    topWind.clear()
    topWind.writeH("===Please Click Buttons Below===")
    RSVar = GUIData() 
    for item in RSVar.List1:
        topWind.writeN(item)

def dataLoad():
    try:
        try:          #Python3
            f = open(__file__ + ".csv","rt")
        except:      #Python2
            f = open(__file__ + ".csv","rb")
        data = f.read().split(',')
        entryCol.entry0.delete(0,END)
        entryCol.entry0.insert(0,data[0])
        entryCol.entry1.delete(0,END)
        entryCol.entry1.insert(0,data[1])
        entryCol.entry2.delete(0,END)
        entryCol.entry2.insert(0,data[2])
        entryCol.entry3.delete(0,END)
        entryCol.entry3.insert(0,data[3])
        botWind.writeN("DataLoad: File")
    except:
        botWind.writeN("DataLoad: Default")

def dataSave():
    # NR5G = gui_reader()
    try: #Python3
        f = open(__file__ + ".csv",'wt', encoding='utf-8')
    except:
        f = open(__file__ + ".csv",'wb')
    f.write('%s,'%(entryCol.entry0.get()))
    f.write('%s,'%(entryCol.entry1.get()))
    f.write('%s,'%(entryCol.entry2.get()))
    f.write('%s,'%(entryCol.entry3.get()))
    f.close()
    print("DataSave: File Saved")

def menu_Exit():
    global GUI
    dataSave() 
    GUI.quit()
    GUI.destroy()
    # print("Program End")

def menu_Open():
    asdf = tkFileDialog.askopenfilename()
    print(asdf)

def menu_Save():
    dataSave()

########################################################################
### Main Code
########################################################################
dataLoad()

try:
    #GUI.tk.call('wm', 'iconphoto', GUI._w, Tk.PhotoImage(file='Unity.gif'))
    GUI.geometry("740x600")
    # GUI.resizable(0,0)
    GUI.config(bg=ClrAppBg)
    #Tk.Font(family="Helvetica", size=10, weight=Tk.font.BOLD, slant=Tk.font.ITALIC)
    GUI.iconbitmap('Unity.ico')
except:
    pass

########################################################################
### GUIBlox modify: EntryCol
########################################################################
entryCol.chg2Enum('entry4', ['UL','DL'])
entryCol.chg2Enum('entry5', ["LOW", "MIDD", "HIGH"])
entryCol.chg2Enum('entry6', ["20","50","100","200","400"])
entryCol.chg2Enum('entry7', ["15", "30", "60", "120"])
entryCol.chg2Enum('entry10', ["QPSK", "QAM16", "QAM64", "QAM256"])

entryCol.entry4_enum.set("UL")              # default value pylint:disable=E1101
entryCol.entry5_enum.set("HIGH")            # default value pylint:disable=E1101
entryCol.entry6_enum.set("100")             # default value pylint:disable=E1101
entryCol.entry7_enum.set("60")              # default value pylint:disable=E1101
entryCol.entry10_enum.set("QPSK")           # default value pylint:disable=E1101

entryCol.label2.bind("<Button-1>",click3)                   #Frequency
entryCol.label3.bind("<Button-1>",click4)                   #Power, RMS
entryCol.label8.bind("<Button-1>",click14)                  #RB
entryCol.label9.bind("<Button-1>",click15)                  #RB Offset

########################################################################
### GUIBlox modify: Button Row
########################################################################
buttnRow.button0.config(text='*IDN?'   ,command=btn1)       #pylint: disable=E1101
buttnRow.button1.config(text='Max RB'  ,command=btn2)       #pylint: disable=E1101
buttnRow.button2.config(text='Get EVM' ,command=btn3)       #pylint: disable=E1101
buttnRow.button3.config(text='Set_5GNR',command=btn4)       #pylint: disable=E1101
buttnRow.button4.config(text='Get_5GNR',command=btn5)       #pylint: disable=E1101
buttnRow.button5.config(text='Save WV' ,command=btn6)       #pylint: disable=E1101
buttnRow.button6.config(command=menu_Exit)                  #pylint: disable=E1101

########################################################################
### GUIBlox modify: Output Text Boxes
########################################################################
topWind.listWindow.config(width=ColxWid, height=25, tabs=('5c', '7c', '9c'))
topWind.listWindow.bind("<Button-3>",clearTopWind)
clearTopWind(None)

botWind.listWindow.config(wrap='none', height=8, tabs=('5c', '7c', '9c'))
botWind.stdOut()
botWind.writeH("Output Window")

########################################################################
### GUIBlox Draw Widgets w/ Grid 
########################################################################
entryCol.frame.grid(row=0,column=0,sticky="nsew")
topWind.frame.grid(row=0,column=1,sticky='e')
botWind.frame.grid(row=1,column=0,columnspan=2,sticky='e')
buttnRow.frame.grid(row=4,column=0,columnspan=2,sticky="nsew")

########################################################################
# Define menu
########################################################################
if 0:
    menu = Tk.Menu(GUI)                                     #create GUI dropdown 
    GUI.config(menu=menu)                                   #define GUI's menu

    fileMenu = Tk.Menu(menu)                                #create dropdown menu
    fileMenu.add_command(label="Open",command=menu_Open)
    fileMenu.add_command(label="Save",command=menu_Save)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=menu_Exit)
    menu.add_cascade(label="File",menu=fileMenu)            #add dropdown menu

    editMenu = Tk.Menu(menu)                                #create dropdown menu
    editMenu.add_command(label="Edit",command=menu_Open)
    menu.add_cascade(label="Edit",menu=editMenu)            #add dropdown menu

########################################################################
# GUIBLox Start Program
########################################################################
GUI.mainloop()                                              #Display window
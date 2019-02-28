from __future__ import division     #int div to float
########################################################################
# Title: Rohde & Schwarz Simple ATE example GUI
# Description:
#
########################################################################
# User Input Settings
########################################################################
ColxWid     = 60 -4
BotWindWid  = ColxWid + 25

########################################################################       
### Code Import
########################################################################
from datetime                 import datetime
import tkinter             as     Tk
from   tkinter             import ttk
import tkinter.filedialog  as     tkFileDialog
from buttonRow  import buttonRow
from initGui    import theme
from listWindow import listWindow
from entryCol   import entryCol
END = Tk.END

#Code specific libraries
import copy
from rssd.yaVISA              import jaVisa        #pylint:disable=E0611,E0401
from rssd.VST_5GNR_K144       import VST           #pylint:disable=E0611,E0401

########################################################################
### Create GUI Objects
########################################################################
GUI = theme().addColor()                           #Create GUI object
GUI.title('Rohde&Schwarz FSW SMW 5GNR Utility')                             #GUI Title
topWind = listWindow(GUI)
botWind = listWindow(GUI)
buttnRow = buttonRow(GUI, 5)                      #pylint: disable=unused-variable

entryDict = {} 
entryDict['SMW IP']        = '192.168.1.114'
entryDict['FSW IP']        = '192.168.1.109'
entryDict['Frequency']     = '28e9'
entryDict['SMW Power,RMS'] = '-5'
entryDict['Direction']     = 'UL'
entryDict['Freq Band']     = 'HIGH'
entryDict['Ch BW,MHz']     = '100'
entryDict['SubCarr,kHz']   = '60'
entryDict['RB']            = '132'
entryDict['RB Offset']     = '0'
entryDict['Modulation']    = 'QPSK'
entryCol = entryCol(GUI, entryDict)

########################################################################
### GUI Functions
########################################################################
class GUIData(object):
   def __init__(self):
      self.List1     = ['- Utility does not validate settings against 3GPP 5G',
                        '- Click *IDN? to validate IP Addresses',
                        '- Frequency & SMW Power labels are clickable',
                        '']


entryCol.chg2Enum('entry4', ['UL','DL'])
entryCol.chg2Enum('entry5', ["LOW", "MIDD", "HIGH"])
entryCol.chg2Enum('entry6', ["20","50","100","200","400"])
entryCol.chg2Enum('entry7', ["15", "30", "60", "120"])
entryCol.chg2Enum('entry10', ["QPSK", "QAM16", "QAM64", "QAM256"])

entryCol.entry4_enum.set("UL")      # default value
entryCol.entry5_enum.set("HIGH")    # default value
entryCol.entry6_enum.set("100")     # default value
entryCol.entry7_enum.set("60")      # default value
entryCol.entry10_enum.set("QPSK")    # default value


def btn1():
   ### *IDN Query ###
   NR5G = VST().jav_Open(entryCol.entry0.get(),entryCol.entry1.get())
   botWind.writeN(NR5G.SMW.query('*IDN?'))
   botWind.writeN(NR5G.FSW.query('*IDN?'))
   NR5G.jav_Close()
   
def btn2():
   ### Get Max RB ###
   topWind.writeN('--------------------------   --------------------------')
   topWind.writeN('|u[<6GHz ]010 020 050 100|   |u[>6GHz ]050 100 200 400|')
   topWind.writeN('|-+------+---+---+---+---|   |-+------+---+---+---+---|')
   topWind.writeN('|0 015kHz|052 106 270 N/A|   |0 015kHz|N/A N/A N/A N/A|')
   topWind.writeN('|1 030kHz|024 051 133 273|   |1 030kHz|N/A N/A N/A N/A|')
   topWind.writeN('|2 060kHz|011 024 065 135|   |2 060kHz|066 132 264 N/A|')
   topWind.writeN('|3 120kHz|N/A N/A N/A N/A|   |3 120kHz|032 066 132 264|')
   topWind.writeN('--------------------------   --------------------------')
   topWind.writeN(' ')

   NR5G = VST().jav_Open(entryCol.entry0.get(),entryCol.entry1.get())
   data = NR5G.SMW.Get_5GNR_RBMax()
   topWind.writeN("=== Max RB ===")
   topWind.writeN("Mode: %s %sMHz"%(NR5G.SMW.Get_5GNR_FreqRange(),NR5G.SMW.Get_5GNR_ChannelBW()))
   for i in data:
      topWind.writeN("SubC:%d  RB Max:%d"%(i[0],i[1]))
   NR5G.jav_Close()

def btn3():
   ### Get EVM ###
   NR5G = VST().jav_Open(entryCol.entry0.get(),entryCol.entry1.get())
   NR5G.FSW.Set_InitImm()
   topWind.writeN('EVM:' + str(NR5G.FSW.Get_5GNR_EVM()))
   NR5G.FSW.jav_Close()
   
def btn4():
   ### Set 5GNR Parameters
   NR5G = VST().jav_Open(entryCol.entry0.get(),entryCol.entry1.get())
   
   ### Read values from GUI
   NR5G.Freq        = float(entryCol.entry2.get())
   NR5G.SWM_Out     = float(entryCol.entry3.get())
   NR5G.NR_Dir      = Enum10.get()
   NR5G.NR_Deploy   = Enum11.get()
   NR5G.NR_ChBW     = int(Enum12.get())
   NR5G.NR_SubSp    = int(Enum13.get())
   NR5G.NR_RB       = int(entryCol.entry8.get())
   NR5G.NR_RBO      = int(entryCol.entry9.get())
   NR5G.NR_Mod      = Enum16.get()
   
   ### Do some work
   botWind.writeN("SMW Creating Waveform.")
   NR5G.Set_5GNR_All()
   botWind.writeN(NR5G.FSW.jav_ClrErr())
   botWind.writeN(NR5G.SMW.jav_ClrErr())
   botWind.writeN("SMW/FSW Setting Written")
   NR5G.jav_Close()

def btn5():
   NR5G = VST().jav_Open(entryCol.entry0.get(),entryCol.entry1.get())

   ### Read 5GNR Parameters ###
   K144Data = NR5G.Get_5GNR_All() 
   #windowUpperClear()
   topWind.writeN(" ")
   for i in range(len(K144Data[0])):
      try:
         topWind.writeN("%s\t%s\t%s"%(K144Data[0][i],K144Data[1][i],K144Data[2][i]))
      except: 
         try:
            topWind.writeN("%s\t%s\t%s"%(K144Data[0][i],K144Data[1][i],'<notRead>'))
         except:
            topWind.writeN("%s\t%s\t%s"%(K144Data[0][i],'<notRead>',K144Data[2][i]))
   NR5G.jav_Close()

def click3(tkEvent):
   #print(tkEvent)
   freq = int(entryCol.entry2.get())
   NR5G = VST().jav_Open(entryCol.entry0.get(),entryCol.entry1.get())
   NR5G.SMW.Set_Freq(freq)
   NR5G.FSW.Set_Freq(freq)
   NR5G.jav_Close()
   botWind.writeN('SMW/FSW Freq: %d Hz'%freq)
   
def click4(tkEvent):
   #print(tkEvent)
   NR5G = VST().jav_Open(entryCol.entry0.get(),entryCol.entry1.get())
   NR5G.SMW.Set_RFPwr(int(entryCol.entry3.get()))
   NR5G.jav_Close()
   botWind.writeN('SMW RMS Pwr : %d dBm'%int(entryCol.entry3.get()))

def click14(tkEvent):
   #print(tkEvent)
   if 0:
      NR5G = VST().jav_Open(entryCol.entry0.get(),entryCol.entry1.get())
      NR_RB  = int(entryCol.entry8.get())
      NR_Dir = Enum10.get()
      if 0:
         NR5G.SMW.Set_5GNR_Direction(NR_Dir)
         NR5G.SMW.Set_5GNR_BWP_ResBlock(NR_RB)
         NR5G.SMW.Set_5GNR_BWP_Ch_ResBlock(NR_RB)
         NR5G.FSW.Set_5GNR_Direction(NR_Dir)
         NR5G.FSW.Set_5GNR_BWP_ResBlock(NR_RB)
         NR5G.FSW.Set_5GNR_BWP_Ch_ResBlock(NR_RB)
      NR5G.jav_Close()
   botWind.writeN('FSW:Signal Description-->RadioFrame-->BWP Config-->RB')
   botWind.writeN('FSW:Signal Description-->RadioFrame-->PxSCH Config-->RB')
   botWind.writeN('SMW:User/BWP-->UL BWP-->RB')
   botWind.writeN('SMW:Scheduling-->PxSCH-->RB')
   
def click15(tkEvent):
   botWind.writeN('FSW:Signal Description-->RadioFrame-->BWP Config-->RB Offset')
   botWind.writeN('SMW:User/BWP-->UL BWP-->RB Offset')
   pass
   
def dataLoad():
   OutObj = GUIData()
   try:
      try:        #Python3
         f = open(__file__ + ".csv","rt")
      except:     #Python2
         f = open(__file__ + ".csv","rb")         
      data = f.read().split(',')
      OutObj.Entry1 = data[0]
      OutObj.Entry2 = data[1]
      OutObj.Entry3 = data[2]
      OutObj.Entry4 = data[3]
      botWind.writeN("DataLoad: File")
   except:
      botWind.writeN("DataLoad: Default")
   return OutObj
                 
def dataSave():
   try: #Python3
      f = open(__file__ + ".csv",'wt', encoding='utf-8')
   except:
      f = open(__file__ + ".csv",'wb')      
   f.write('%s,'%(entryCol.entry0.get()))
   f.write('%s,'%(entryCol.entry1.get()))
   f.write('%s,'%(entryCol.entry2.get()))
   f.write('%s,'%(entryCol.entry3.get()))
   f.close()
   botWind.writeN("DataSave: File Saved")
   
def menu_Exit():
   global GUI
   dataSave() 
   GUI.quit()
   GUI.destroy()
   print("Program End")

def menu_Open():
   asdf = tkFileDialog.askopenfilename()
   print(asdf)
   
def menu_Save():
   dataSave()


########################################################################       
### Main Code
########################################################################
RSVar = copy.copy(dataLoad())

try:
   #GUI.tk.call('wm', 'iconphoto', GUI._w, Tk.PhotoImage(file='Unity.gif'))
   GUI.resizable(0,0)
   GUI.config(bg=ClrAppBg)
   #Tk.Font(family="Helvetica", size=10, weight=Tk.font.BOLD, slant=Tk.font.ITALIC)
   GUI.iconbitmap('Unity.ico')
except:
   pass
########################################################################
### Define GUI Widgets
########################################################################
entryCol.label2.bind("<Button-1>",click3)
entryCol.label3.bind("<Button-1>",click4)
entryCol.label8.bind("<Button-1>",click14)
entryCol.label9.bind("<Button-1>",click15)

buttnRow.button0.config(text='*IDN?'   ,command=btn1)     #pylint: disable=E1101
buttnRow.button1.config(text='Max RB'  ,command=btn2)     #pylint: disable=E1101
buttnRow.button2.config(text='Get EVM' ,command=btn3)     #pylint: disable=E1101
buttnRow.button3.config(text='Set_5GNR',command=btn4)     #pylint: disable=E1101
buttnRow.button4.config(text='Get_5GNR',command=btn5)     #pylint: disable=E1101

########################################################################
### List Boxes
########################################################################
topWind.listWindow.config(width=ColxWid, height=20, tabs=('5c', '7c', '9c'))
topWind.listWindow.bind("<Button-3>",topWind.clear)
topWind.writeH("===Please Click Buttons Below===")
for item in RSVar.List1:
   topWind.writeN(item)

botWind.listWindow.config(wrap='none', height=8)
botWind.stdOut()
botWind.writeH("Output Window")

########################################################################
### Draw Widgets w/ Grid 
########################################################################
entryCol.frame.grid(row=0,column=0,sticky="nsew")
topWind.frame.grid(row=0,column=1,sticky='ew')
botWind.frame.grid(row=1,column=0,columnspan=2,sticky='nsew')
buttnRow.frame.grid(row=4,column=0,columnspan=2,sticky="nsew")

########################################################################
# Define menu
########################################################################
if 0:
   menu = Tk.Menu(GUI)                                #create GUI dropdown 
   GUI.config(menu=menu)                              #define GUI's menu

   fileMenu = Tk.Menu(menu)                           #create dropdown menu
   fileMenu.add_command(label="Open",command=menu_Open)
   fileMenu.add_command(label="Save",command=menu_Save)
   fileMenu.add_separator()
   fileMenu.add_command(label="Exit",command=menu_Exit)
   menu.add_cascade(label="File",menu=fileMenu)       #add dropdown menu

   editMenu = Tk.Menu(menu)                           #create dropdown menu
   editMenu.add_command(label="Edit",command=menu_Open)
   menu.add_cascade(label="Edit",menu=editMenu)       #add dropdown menu

########################################################################
# Start Program
########################################################################
GUI.mainloop()                      #Display window

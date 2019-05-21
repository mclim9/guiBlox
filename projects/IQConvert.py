#####################################################################
### Purpose: Object Oriented Python Tkinter example
### Author : Martin C Lim
### Date   : 2019.04.01
### Objects:
#####################################################################
### User Inputs
#####################################################################

#####################################################################
### OOGUI Import 
#####################################################################
from guiblox                import buttonRow, entryCol, theme, listWindow

### Code specific imports
import tkinter as tk
from tkinter.filedialog     import askopenfilename
from   rssd                 import jaVisa
import time
import os
from rssd.iqdata            import IQ

#####################################################################
### Function Definition
#####################################################################
def convert(root):
    print('convert')
    iq = IQ()
    ### Read data
    iq.ReadIqTar(root.files.entry0.get())

    start = time.time()
    iq.writeWv("test2.wv")
    duration = time.time() - start
    print(f"IQ:{iq.NumberOfSamples} samples in {duration*1e3:2.2f} ms --> {iq.NumberOfSamples/1e6/duration:3.2f} MSamples/s")

    pass

def getFilename(tkEvent):
    fny = askopenfilename()
    tkEvent.widget.delete(0,tk.END)
    tkEvent.widget.insert(0,fny)
    print(fny)

#####################################################################
### GUI Layout
#####################################################################
def main():
    global root
    root = theme().addColor()
    root.title('Socket Test Program')
    root.resizable(0,0)

    ### Create Sections
    root.files  = entryCol(root, {'Input File': 'Input.txt','Input Type':'iq.tar','Output File': 'Output.txt','Output Type':'iq.tar'})
    root.bottWind   = listWindow(root)
    root.bottWind.stdOut()                                                          #Stdout --> window
    root.buttnRow = buttonRow(root, 2)                                              #pylint: disable=unused-variable

    ### Define Sections
    widdy = 45
    root.files.chg2Enum('entry1', ['iq.tar','iqw','wv'])
    root.files.chg2Enum('entry3', ['iq.tar','iqw','wv'])

    root.files.entry0.bind("<Button-1>",getFilename)                                       #pylint: disable=E1101
    root.files.entry2.bind("<Button-1>",getFilename)                                       #pylint: disable=E1101
    root.files.entry0.config(width = widdy)                                       #pylint: disable=E1101    
    root.files.entry1.config(width = widdy-7)                                       #pylint: disable=E1101    
    root.files.entry2.config(width = widdy)                                       #pylint: disable=E1101    
    root.files.entry3.config(width = widdy-7)                                       #pylint: disable=E1101    

    root.bottWind.listWindow.config(height= 5,width=50)
    root.buttnRow.button0.config(text='Convert'     ,command=lambda: convert(root))     #pylint: disable=E1101
    root.buttnRow.button1.config(text='Convert'     ,command=lambda: convert(root))     #pylint: disable=E1101

    ### Grid Sections
    root.files.frame.grid(row=0,column=0,sticky="ns")
    root.bottWind.frame.grid(row=3,column=0,sticky='ns')
    root.buttnRow.frame.grid(row=20,column=0,columnspan=3,sticky="nsew")
    root.mainloop()

if __name__ == '__main__':
    main()

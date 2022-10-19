from tkinter import *
from tkinter import filedialog as fd
import pandas as pd
import csv

window=Tk() 

width= window.winfo_screenwidth()  
height= window.winfo_screenheight() 
window.geometry("%dx%d" % (width, height)) 
window.title("GeoAnalysis") 

def donothing():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()



def askOpenFile():
        data = fd.askopenfile(title='Abrir arquivo de projeto', initialdir='/', filetypes = (('text files', '*.csv'),('All files', '*.*')))
    


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=askOpenFile)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)


window.config(menu=menubar)


mainloop()


from tkinter import *
from tkinter import filedialog as fd
import tkinter.ttk as ttk
import pandas as pd
import csv

window=Tk() 

width = 1900
height = 1000
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(0, 0)

def donothing():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def askOpenFile(self):
        data = fd.askopenfile(title='Abrir arquivo de projeto', initialdir='/', filetypes = (('text files', '*.csv'),('All files', '*.*')))
    


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=askOpenFile)
filemenu.add_command(label="Salvar", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
window.config(menu=menubar)

TableMargin = Frame(window, width=500)
TableMargin.pack(side=TOP)

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Comment", "K2O", "TiO2", "FeO", "MnO", "CaO", "Cr2O3", "Al2O3", "SiO2", "MgO", "Total", "Date")
, height=600, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('Comment', text="Comment", anchor=W)
tree.heading('K2O', text="K2O", anchor=W)
tree.heading('TiO2', text="TiO2", anchor=W)
tree.heading('FeO', text="FeO", anchor=W)
tree.heading('MnO', text="MnO", anchor=W)
tree.heading('CaO', text="CaO", anchor=W)
tree.heading('Cr2O3', text="Cr2O3", anchor=W)
tree.heading('Al2O3', text="Al2O3", anchor=W)
tree.heading('SiO2', text="SiO2", anchor=W)
tree.heading('MgO', text="MgO", anchor=W)
tree.heading('Total', text="Total", anchor=W)
tree.heading('Date', text="Date", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=200, width=250)
tree.column('#2', stretch=NO, minwidth=50, width=50)
tree.column('#3', stretch=NO, minwidth=50, width=50)
tree.column('#4', stretch=NO, minwidth=50, width=50)
tree.column('#5', stretch=NO, minwidth=50, width=50)
tree.column('#6', stretch=NO, minwidth=50, width=50)
tree.column('#7', stretch=NO, minwidth=50, width=50)
tree.column('#8', stretch=NO, minwidth=50, width=50)
tree.column('#9', stretch=NO, minwidth=50, width=50)
tree.column('#10', stretch=NO, minwidth=50, width=50)
tree.column('#11', stretch=NO, minwidth=50, width=50)
tree.pack()

with open('dados.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        Comment = row['Comment']
        K2O = row['K2O']
        TiO2 = row['TiO2']
        FeO = row['FeO']
        MnO = row['MnO']
        CaO = row['CaO']
        Cr2O3 = row['Cr2O3']
        Al2O3 = row['Al2O3']
        SiO2 = row['SiO2']
        MgO = row['MgO']
        Total = row['Total']
        Date = row['Date']
        tree.insert("", 0, values=(Comment, K2O, TiO2, FeO, MnO, CaO, Cr2O3, Al2O3, SiO2, MgO, Total, Date))

if __name__ == '__main__':
    window.mainloop()




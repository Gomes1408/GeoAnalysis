
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox, ttk
import csv
import pandas as pd

class DataClass:
    def __init__(self, head, row):
        self.head = head
        self.row = row

window=tk.Tk() 

meta = DataClass

width = 1000
height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(0, 0)
frame1 = tk.LabelFrame(window, text="Excel Data")
frame1.place(height=400, width=1000)



def askOpenFile():
        data = fd.askopenfilename(title='Abrir arquivo de projeto', initialdir='/', filetypes = (("Csv Files", '*.csv'),('All files', '*.*')))
        df = pd.read_csv(data, delimiter=';')
        meta.head = list(df.columns)
        tree["column"] = meta.head
        tree["show"] = "headings"
        for column in tree["columns"]:
            tree.heading(column, text=column) 

        meta.row = df.to_numpy().tolist() 
        for row in meta.row:
            tree.insert("", "end", values=row)
        return None

def saveOpenFile():
    filePath = fd.asksaveasfilename(title='Salvar arquivo de projeto', initialdir='/', filetypes = (("Csv Files", '*.csv'),('All files', '*.*')))
    if filePath[-4] != ".csv":
        filePath = filePath + ".csv"
    
    with open(filePath, 'w', encoding="utf-8", newline='') as newFile:
        writer = csv.writer(newFile, delimiter=';')
        writer.writerow(meta.head)
        for rows in meta.row:
            writer.writerow(rows)

    newFile.close()
    return None


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command= lambda: askOpenFile())
filemenu.add_command(label="Save", command= lambda: saveOpenFile())
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
window.config(menu=menubar)

tree = ttk.Treeview(frame1)
tree.place(relheight=1, relwidth=1)

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tree.yview) 
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tree.xview) 
tree.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
treescrollx.pack(side="bottom", fill="x") 
treescrolly.pack(side="right", fill="y")

if __name__ == "__main__":
    window.mainloop()
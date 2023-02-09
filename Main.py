
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
path = 'oi'

width = 1400
height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(0, 0)
frame1 = tk.LabelFrame(window, text="Excel Data")
frame1.place(height=400, width=1400)
frame2 = tk.LabelFrame(window, text="Calculations")
frame2.place(height=300, width=1400, y=400)


def calculos(path):
    
    nO = 12.00
    cst = 8.00
    mCat = {'K2O','TiO2','FeO','MnO','CaO','Cr2O3','Na2O','Al2O3','SiO2','MgO','Fe2O3','Total'}
    mOxy = {'K2O','TiO2','FeO','MnO','CaO','Cr2O3','Na2O','Al2O3','SiO2','MgO','Fe2O3','Total'}
    nCat = {'K2O','TiO2','FeO','MnO','CaO','Cr2O3','Na2O','Al2O3','SiO2','MgO','Fe2O3','Total','Calculado'}
    nOxy = {'K2O','TiO2','FeO','MnO','CaO','Cr2O3','Na2O','Al2O3','SiO2','MgO','Fe2O3','Total'}
    atmU = {'FeO','Fe2O3'}
    diag = {'XMg','XFe','XMn','Xca'}
    triplot = {'XMg', 'XCa', 'XFM'}
    sig = {'X', 'Y'}


    data = pd.read_csv(path, delimiter=';')

    for x in range(len(data)):
        totalMCat = 0
        totalMOxy = 0
        totalNCat = 0
        totalNOxy = 0

#Calculo Molecular Cátion
        mCat('SiO2').append(data('SiO2')[x]/60.0843)
        totalMCat += data('SiO2')[x]/60.0843

        mCat('TiO2').append(data('TiO2')[x]/79.8988)
        totalMCat += data('TiO2')[x]/79.8988
        
        mCat('Al2O3').append(2*data('Al2O3')[x]/101.9613)
        totalMCat += 2*data('Al2O3')[x]/101.9613
        
        mCat('Cr2O3').append(2*data('Cr2O3')[x]/151.9902)
        totalMCat += 2*data('Cr2O3')[x]/151.9902
        
        mCat('FeO').append(data('FeO')[x]/71.8464)
        totalMCat += data('FeO')[x]/71.8464
        
        mCat('MnO').append(data('MnO')[x]/70.9374)
        totalMCat += data('MnO')[x]/70.9374
        
        mCat('MgO').append(data('MgO')[x]/40.3044)
        totalMCat += data('MgO')[x]/40.3044
        
        mCat('CaO').append(data('CaO')[x]/56.0794)
        totalMCat += data('CaO')[x]/56.0794
       
        mCat('K2O').append(data('K2O')[x]/39.0983)
        totalMCat += data('K2O')[x]/39.0983
       
        mCat('Na2O').append(2*data('Na2O')[x]/22.989769)
        totalMCat += 2*data('Na2O')[x]/22.989769

        if(data('Fe2O3')[x]>0):
                mCat('Fe2O3').append(data('Fe2O3')[x]*2/159.6922) 
                totalMCat += data('Fe2O3')[x]*2/159.6922
        else:
                mCat('Fe2O3').append(0) 
                totalMCat += 0

        mCat('Total').append(totalMCat)


#Calculo Molecular Oxigênio
        mOxy('SiO2').append(2*data('SiO2')[x]/60.0843)
        totalMOxy += 2*data('SiO2')[x]/60.0843

        mOxy('TiO2').append(2*data('TiO2')[x]/79.8988)
        totalMOxy += 2*data('TiO2')[x]/79.8988
        
        mOxy('Al2O3').append(3*data('Al2O3')[x]/101.9613)
        totalMOxy += 3*data('Al2O3')[x]/101.9613
        
        mOxy('Cr2O3').append(3*data('Cr2O3')[x]/151.9902)
        totalMOxy += 3*data('Cr2O3')[x]/151.9902
        
        mOxy('FeO').append(data('FeO')[x]/71.8464)
        totalMOxy += data('FeO')[x]/71.8464
        
        mOxy('MnO').append(data('MnO')[x]/70.9374)
        totalMOxy += data('MnO')[x]/70.9374
        
        mOxy('MgO').append(data('MgO')[x]/40.3044)
        totalMOxy += data('MgO')[x]/40.3044
        
        mOxy('CaO').append(data('CaO')[x]/56.0794)
        totalMOxy += data('CaO')[x]/56.0794
       
        mOxy('K2O').append(data('K2O')[x]/39.0983)
        totalMOxy += data('K2O')[x]/39.0983
       
        mOxy('Na2O').append(data('Na2O')[x]/22.989769)
        totalMOxy += data('Na2O')[x]/22.989769

        if(data('Fe2O3')[x]>0):
                mOxy('Fe2O3').append(data('Fe2O3')[x]*3/159.6922) 
                totalMOxy += data('Fe2O3')[x]*3/159.6922
        else:
                mOxy('Fe2O3').append(0) 
                totalMOxy += 0

        mOxy('Total').append(totalMOxy)

#Normalização de cations
        if(data('Fe2O3')[x]>0):
                nCat('SiO2').append(cst*mCat('SiO2')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('SiO2')[x]/mOxy('Total')[x]

                nCat('TiO2').append(cst*mCat('TiO2')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('TiO2')[x]/mOxy('Total')[x]
                
                nCat('Al2O3').append(cst*mCat('Al2O3')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('Al2O3')[x]/mOxy('Total')[x]
                
                nCat('Cr2O3').append(cst*mCat('Cr2O3')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('Cr2O3')[x]/mOxy('Total')[x]
                
                nCat('FeO').append(cst*mCat('FeO')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('FeO')[x]/mOxy('Total')[x]
                
                nCat('MnO').append(cst*mCat('MnO')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('MnO')[x]/mOxy('Total')[x]
                
                nCat('MgO').append(cst*mCat('MgO')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('MgO')[x]/mOxy('Total')[x]
                
                nCat('CaO').append(cst*mCat('CaO')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('CaO')[x]/mOxy('Total')[x]
        
                nCat('K2O').append(cst*mCat('K2O')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('K2O')[x]/mOxy('Total')[x]
        
                nCat('Na2O').append(cst*mCat('Na2O')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('Na2O')[x]/mOxy('Total')[x]

                nCat('Fe2O3').append(cst*mCat('Fe2O3')[x]/mOxy('Total')[x])
                totalNCat += cst*mCat('Fe2O3')[x]/mOxy('Total')[x]

                nCat('Total').append(totalNCat)
        else:
                nCat('SiO2').append(nO*mCat('SiO2')[x]/mCat('Total')[x])
                totalNCat += nO*mCat('SiO2')[x]/mCat('Total')[x]

                nCat('TiO2').append(nO*mCat('TiO2')[x]/mCat('Total')[x])
                totalNCat += nO*mCat('TiO2')[x]/mCat('Total')[x]
                
                nCat('Al2O3').append(nO*mCat('Al2O3')[x]/mCat('Total')[x])
                totalNCat += nO*mCat('Al2O3')[x]/mCat('Total')[x]
                
                nCat('Cr2O3').append(nO*mCat('Cr2O3')[x]/mCat('Total')[x])
                totalNCat += nO*mCat('Cr2O3')[x]/mCat('Total')[x]
                
                nCat('FeO').append(nO*mCat('FeO')[x]/mCat('Total')[x])
                totalNCat += nO*mCat('FeO')[x]/mCat('Total')[x]
                
                nCat('MnO').append(nO*mCat('MnO')[x]/mCat('Total')[x])
                totalNCat += nO*mCat('MnO')[x]/mCat('Total')[x]
                
                nCat('MgO').append(nO*mCat('MgO')[x]/mCat('MgO')[x])
                totalNCat += nO*mCat('MgO')[x]/mCat('Total')[x]
                
                nCat('CaO').append(nO*mCat('CaO')[x]/mCat('Total')[x])
                totalNCat += nO*mCat('CaO')[x]/mCat('Total')[x]
        
                nCat('K2O').append(nO*mCat('K2O')[x]/mCat('Total')[x])
                totalNCat += nO*mCat('K2O')[x]/mCat('Total')[x]

                nCat('Na2O').append(nO*mCat('Na2O')[x]/mCat('Total')[x])
                totalNCat += nO*mCat('Na2O')[x]/mCat('Total')[x]

                nCat('Fe2O3').append(nO*mCat('Fe2O3')[x]/mCat('Total')[x])
                totalNCat += nO*mCat('Fe2O3')[x]/mCat('Total')[x]

                nCat('Total').append(totalNCat)
        nCat('Calculado').append(4*(nCat('SiO2')[x]+nCat('TiO2')[x])+3*(nCat('Al2O3')[x]+nCat('Cr2O3')[x]+nCat('Fe2O3')[x])+2*(nCat('FeO')[x]+nCat('MnO')[x]+nCat('MgO')[x]+nCat('CaO')[x]))

#Unidades atômicas para compostos com ferro; Fe2+ para FeO e Fe3+ para Fe2O3
        if(data('Fe2O3')[x]>0):
                atmU('Fe2O3').append(mOxy('Fe2O3')[x])
        else:
                if((24-totalNCat[x])>0):
                        atmU('Fe2O3').append(24-totalNCat[x])
                else:
                        atmU('Fe2O3').append(0)

        if(data('Fe2O3')[x]>0):
                atmU('FeO').append(nCat('FeO')[x])
        else:
                atmU('FeO').append(atmU('Fe2O3')[x] - nCat('FeO')[x])

#Normalização de Oxigenios
        nOxy('SiO2').append(2*nCat('SiO2')[x])
        totalNOxy += 2*nCat('SiO2')[x]

        nOxy('TiO2').append(2*nCat('TiO2')[x])
        totalNOxy += 2*nCat('TiO2')[x]
        
        nOxy('Al2O3').append((3/2)*nCat('Al2O3')[x])
        totalNOxy += (3/2)*nCat('Al2O3')[x]
        
        nOxy('Cr2O3').append((3/2)*nCat('Cr2O3')[x])
        totalNOxy += (3/2)*nCat('Cr2O3')[x]
        
        nOxy('FeO').append(atmU('FeO')[x])
        totalNOxy += atmU('FeO')[x]
        
        nOxy('MnO').append(nCat('MnO')[x])
        totalNCat += nCat('MnO')[x]
        
        nOxy('MgO').append(nCat('MgO')[x])
        totalNOxy += nCat('MgO')[x]
        
        nOxy('CaO').append(nCat('CaO')[x])
        totalNOxy += nCat('CaO')[x]
       
        nOxy('K2O').append(2*nCat('K2O')[x])
        totalNOxy += 2*nCat('K2O')[x]
       
        nOxy('Na2O').append(2*nCat('Na2O')[x])
        totalNOxy += 2*nCat('Na2O')[x]

        nOxy('Fe2O3').append((3/2)*atmU('Fe2O3')[x])
        totalNOxy += (3/2)*atmU('Fe2O3')[x]

        nOxy('Total').append(totalNOxy)


        

#Calculo para diagramas
        diag('XMg').append(nCat('MgO')[x]/(nCat('MgO')[x]+nCat('FeO')[x]+nCat('MnO')[x]+nCat('CaO')[x]))
        diag('XFe').append(nCat('XFe')[x]/(nCat('MgO')[x]+nCat('FeO')[x]+nCat('MnO')[x]+nCat('CaO')[x]))
        diag('XMn').append(nCat('XMn')[x]/(nCat('MgO')[x]+nCat('FeO')[x]+nCat('MnO')[x]+nCat('CaO')[x]))
        diag('XCa').append(nCat('XCa')[x]/(nCat('MgO')[x]+nCat('FeO')[x]+nCat('MnO')[x]+nCat('CaO')[x]))

#triplot Morton Mange
        triplot('XMg').append(100*diag('XMg')[x])
        triplot('XCa').append(100*diag('XCa')[x])
        triplot('XFM').append(100*(diag('XFe')[x]+diag('XMn')))

#Coordenadas para SIG
        sig('X').append((triplot('XCa')[x]+(0.5*triplot('XMg')[x]))/100)
        sig('Y').append((0.866*triplot('XMg')[x])/100)

    return None


def askOpenFile():
        data = fd.askopenfilename(title='Abrir arquivo de projeto', initialdir='/', filetypes = (("Csv Files", '*.csv'),('All files', '*.*')))
        path = data
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
filemenu.add_command(label="Open", command= lambda: askOpenFile())
filemenu.add_command(label="Save", command= lambda: saveOpenFile())
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
mathmenu = tk.Menu(menubar, tearoff= 0)
mathmenu.add_command(Label="Calculations", command= lambda: calculos(path))
window.config(menu=menubar)

tree = ttk.Treeview(frame1)
tree.place(relheight=1, relwidth=1)

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tree.yview) 
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tree.xview) 
tree.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
treescrollx.pack(side="bottom", fill="x") 
treescrolly.pack(side="right", fill="y")


tree2 = ttk.Treeview(frame2)
tree2.place(relheight=1, relwidth=1)

treescrolly2 = tk.Scrollbar(frame2, orient="vertical", command=tree2.yview) 
treescrollx2 = tk.Scrollbar(frame2, orient="horizontal", command=tree2.xview) 
tree2.configure(xscrollcommand=treescrollx2.set, yscrollcommand=treescrolly2.set) 
treescrollx2.pack(side="bottom", fill="x") 
treescrolly2.pack(side="right", fill="y")


if __name__ == "__main__":
    window.mainloop()
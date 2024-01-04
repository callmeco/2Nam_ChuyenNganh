from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
import pandas as pd
from pandas import DataFrame
class CreateOUFromCSV:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_csv= StringVar()

        readCsvFrame = LabelFrame(self.root,text="Create OU From CSV",bg='white',bd=2,relief=RIDGE)
        readCsvFrame.place(x=10,y=20,width=1000,height=550)
        ten_lb=Label(readCsvFrame,text="Nhập file CSV",bg="white",font="22").place(x=200,y=100)
        ten_Entry=Entry(readCsvFrame,bg="lightgrey",width=80,textvariable=self.var_csv)
        ten_Entry.place(x=400,y=105)

        btn_create = Button(readCsvFrame,text="Create",bg="#b0d46c",width=20,command=self.executed)
        btn_create.place(x=500, y=295)
        
    def createOU_fromCSV(self,file):
        f = pd.read_csv(file)
        ou = DataFrame(f, columns=['OU'])
        for i in range(len(ou)):
            command = f'dsadd ou "ou={ou.iloc[i,0]},ou=QTM_CTY,dc=qlab,dc=com"'
            sendCommand(command)
            os.system(command)  
    def executed(self):
            file = self.var_csv.get()
            f = pd.read_csv(file)
            ou = DataFrame(f, columns=['OU'])
            for i in range(len(ou)):
                if file:
                    command = f'dsadd ou "OU={ou.iloc[i,0]},ou=QTM_CTY,dc=qlab,dc=QTM_CTY,dc=com"'
                    self.createOU_fromCSV(file)
                    sendCommand(command)
                break
if __name__ == "__main__":    
    root = Tk()
    obj = CreateOUFromCSV(root)
    root.mainloop()
from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
import pandas as pd
from pandas import DataFrame
class CreateUserFromCSV:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_csv= StringVar()

        readCsvFrame = LabelFrame(self.root,text="Create User From CSV",bg='white',bd=2,relief=RIDGE)
        readCsvFrame.place(x=10,y=20,width=1000,height=550)
        ten_lb=Label(readCsvFrame,text="Nhập file CSV",bg="white",font="22").place(x=200,y=100)
        ten_Entry=Entry(readCsvFrame,bg="lightgrey",width=80,textvariable=self.var_csv)
        ten_Entry.place(x=400,y=105)

        btn_create = Button(readCsvFrame,text="Create",bg="#b0d46c",width=20,command=self.executed)
        btn_create.place(x=500, y=295)
        
    def splitName(ho_ten):
        ten=ho_ten.split(" ")
        ten_tam=ten[-1]
        for i in range(len(ten)-1):
            ten_tam=ten_tam+ten[i][0]
        return ten_tam
    def createuser_fromCSV(self,file):
        f = pd.read_csv(file)
        us = DataFrame(f, columns=['Fullname'])
        ou = DataFrame(f, columns=['OU'])
        pwd = DataFrame(f, columns=['Password'])
        for i in range(len(us)):
            sendCommand(f"dsadd user " + chr(34) + "cn=" + splitName(us.iloc[i,0]) + ",ou=" + ou.iloc[i,0] + "," + domain + chr(34)+" -pwd "+pwd.iloc[i,0])
    def executed(self):
            file = self.var_csv.get()
            f = pd.read_csv(file)
            ou = DataFrame(f, columns=['OU'])
            for i in range(len(ou)):
                if file:
                    command = f'dsadd ou "OU={ou.iloc[i,0]},ou=QTMCTY,dc=qlab,dc=com"'
                    self.createuser_fromCSV(file)
                    sendCommand(command)
                break
if __name__ == "__main__":    
    root = Tk()
    obj = CreateUserFromCSV(root)
    root.mainloop()
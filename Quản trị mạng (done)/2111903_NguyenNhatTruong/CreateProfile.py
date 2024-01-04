from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
from pandas import DataFrame
import pandas as pd
class CreateProfile:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_csv= StringVar()
        self.var_fd= StringVar()

        delete_user = LabelFrame(self.root,text="Create Profile For User",bg='white',bd=2,relief=RIDGE)
        delete_user.place(x=10,y=20,width=1000,height=550)
        username_lb=Label(delete_user,text="Nhập file",bg="white",font="22").place(x=200,y=100)
        username_Entry=Entry(delete_user,bg="lightgrey",width=80,textvariable=self.var_csv)
        username_Entry.place(x=400,y=105)
        ou_lb=Label(delete_user,text="Nhập Folder",bg="white",font="22").place(x=200,y=190)
        ou_Entry=Entry(delete_user,bg="lightgrey",width=80,textvariable=self.var_fd)
        ou_Entry.place(x=400,y=195)

        btn_delete = Button(delete_user,text="Delete",bg="#b0d46c",width=20,command=self.executed)
        btn_delete.place(x=500, y=340)
        
    def splitName(self,ho_ten):
        ten=ho_ten.split(" ")
        ten_tam=ten[-1]
        for i in range(len(ten)-1):
            ten_tam=ten_tam+ten[i][0]
        return ten_tam
    def createProfile_forUser(self,file):
        nameFolder = self.var_fd.get()
        f = pd.read_csv(file)
        us = DataFrame(f, columns=['Fullname'])
        for i in range(len(us)):
            cmdMKDir = "mkdir C:\\"+nameFolder
            os.system(cmdMKDir)
            cmdShare = "net share "+nameFolder+"=C:\\"+nameFolder+" /grant:everyone,full"
            sendCommand(cmdShare)
            os.system(cmdShare)
            pathProfile =  f'" -profile 192.168.65.138 +"\\profile\\"+{self.splitName(us.iloc[i,0])}'
            sendCommand(pathProfile)  
    def executed(self):
        file = self.var_csv.get()
        f = pd.read_csv(file)
        us = DataFrame(f, columns=['Fullname'])
        nameFolder = self.var_fd.get()
        for i in range(len(us)):
            cmdMKDir = "mkdir C:\\"+nameFolder
            os.system(cmdMKDir)
            cmdShare = "net share "+nameFolder+"=C:\\"+nameFolder+" /grant:everyone,full"
            sendCommand(cmdShare)
            os.system(cmdShare)
            pathProfile =  f'" -profile 192.168.65.138 +"\\profile\\"+{self.splitName(us.iloc[i,0])}'
            sendCommand(pathProfile) 
            break 

if __name__ == "__main__":    
    root = Tk()
    obj = CreateProfile(root)
    root.mainloop()
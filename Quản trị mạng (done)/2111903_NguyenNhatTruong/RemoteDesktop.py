from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class RemoteDesktop:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_username= StringVar()
        self.var_password= StringVar()
        self.var_ou= StringVar()
        self.var_domain= StringVar()

        readCsvFrame = LabelFrame(self.root,text="Remote Desktop For User",bg='white',bd=2,relief=RIDGE)
        readCsvFrame.place(x=10,y=20,width=1000,height=550)
        ten_lb=Label(readCsvFrame,text="Nhập username",bg="white",font="22").place(x=200,y=100)
        ten_Entry=Entry(readCsvFrame,bg="lightgrey",width=80,textvariable=self.var_username)
        ten_Entry.place(x=400,y=105)

        btn_create = Button(readCsvFrame,text="Accept",bg="#b0d46c",width=20,command=self.executed)
        btn_create.place(x=500, y=295)
    def splitName(ho_ten):
        ten=ho_ten.split(" ")
        ten_tam=ten[-1]
        for i in range(len(ten)-1):
            ten_tam=ten_tam+ten[i][0]
        return ten_tam    
    def remoteDesktop(self,username):
        username = self.var_username.get()
        us = splitName(username)
        command = f'NET LOCALGROUP "Remote Desktop Users" {us} /ADD'
        sendCommand(command)
        os.system(command)
    def executed(self):
        username = self.var_username.get()
        command = f'NET LOCALGROUP "Remote Desktop Users" {username} /ADD' 
        if username:
                self.remoteDesktop(username)
                sendCommand(command)
if __name__ == "__main__":    
    root = Tk()
    obj = RemoteDesktop(root)
    root.mainloop()
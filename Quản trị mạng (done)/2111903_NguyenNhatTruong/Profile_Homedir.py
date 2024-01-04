from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class CreateProfile_Homedir:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_username= StringVar()
        self.var_ip= StringVar()
        self.var_ou= StringVar()
        self.var_domain= StringVar()
        self.var_folder= StringVar()

        createP_H = LabelFrame(self.root,text="Create Profile And Homedir For User",bg='white',bd=2,relief=RIDGE)
        createP_H.place(x=10,y=20,width=1000,height=550)
        username_lb=Label(createP_H,text="Nhập họ tên",bg="white",font="22").place(x=200,y=100)
        username_Entry=Entry(createP_H,bg="lightgrey",width=80,textvariable=self.var_username)
        username_Entry.place(x=400,y=105)
        ip_lb=Label(createP_H,text="Nhập IP",bg="white",font="22").place(x=200,y=145)
        ip_Entry=Entry(createP_H,bg="lightgrey",width=80,textvariable=self.var_ip)
        ip_Entry.place(x=400,y=150)
        ou_lb=Label(createP_H,text="Nhập OU",bg="white",font="22").place(x=200,y=190)
        ou_Entry=Entry(createP_H,bg="lightgrey",width=80,textvariable=self.var_ou)
        ou_Entry.place(x=400,y=195)
        domain_lb=Label(createP_H,text="Nhập domain",bg="white",font="22").place(x=200,y=235)
        domain_Entry=Entry(createP_H,bg="lightgrey",width=80,textvariable=self.var_domain)
        domain_Entry.place(x=400,y=240)
        folder_lb=Label(createP_H,text="Nhập folder",bg="white",font="22").place(x=200,y=280)
        folder_Entry=Entry(createP_H,bg="lightgrey",width=80,textvariable=self.var_folder)
        folder_Entry.place(x=400,y=295)

        btn_create = Button(createP_H,text="Create",bg="#b0d46c",width=20,command=self.executed)
        btn_create.place(x=500, y=340)
    def splitName(ho_ten):
        ten=ho_ten.split(" ")
        ten_tam=ten[-1]
        for i in range(len(ten)-1):
            ten_tam=ten_tam+ten[i][0]
        return ten_tam    
    def createProfileAndHomeDir(self,account,ip,ou,domain,namefd):
        username = splitName(account)
        cmdMkdir = f'mkdir C:\\{namefd}'
        os.system(cmdMkdir)
        cmdshare = f'net share {namefd}= C:\\{namefd}'
        sendCommand(cmdshare)
        os.system(cmdshare)
        path_profile = f'-profile \\{ip}\\profiles\\{username}'
        command2 = f'dsmod user "CN={username},OU={ou},dc={domain},dc=com" {path_profile}'
        pathHomeDir = " -hmdir " + chr(92) + chr(92) + "192.168.65.136\\dungchung\\" + username + " -hmdrv Z: "
        command1 = f'dsmod user "CN={username},OU={ou},dc={domain},dc=com" {pathHomeDir}'
        print(command2)
        sendCommand(command1)
        sendCommand(command2)
        os.system(command2)
    def executed(self):
            account = self.var_username.get()
            ip = self.var_ip.get()
            ou = self.var_ou.get()
            domain = self.var_domain.get()
            namefd = self.var_folder.get()
            if account and namefd and ou and domain and ip:
                self.createProfileAndHomeDir(account,ip,ou,domain,namefd)

if __name__ == "__main__":    
    root = Tk()
    obj = CreateProfile_Homedir(root)
    root.mainloop()
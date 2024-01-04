from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class EnableUser:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        createP_H = LabelFrame(self.root,text="User Setting",bg='white',bd=2,relief=RIDGE)
        createP_H.place(x=10,y=20,width=1000,height=550)

        btn_install = Button(createP_H,text="Enable",bg="#b0d46c",width=20,command=self.enableUser)
        btn_install.place(x=400, y=240)
        btn_install = Button(createP_H,text="Disable",bg="#b0d46c",width=20,command=self.disableUser)
        btn_install.place(x=400, y=440)
        
    def enableUser(username):
        command = "net user " + username + "/active:yes"
        sendCommand(command)

    def disableUser(username):
        command = "net user " + username + "/active:no"
        sendCommand(command)

if __name__ == "__main__":    
    root = Tk()
    obj = EnableUser(root)
    root.mainloop()
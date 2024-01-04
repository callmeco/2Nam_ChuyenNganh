from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class Firewall:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        createP_H = LabelFrame(self.root,text="Firewall Service",bg='white',bd=2,relief=RIDGE)
        createP_H.place(x=10,y=20,width=1000,height=550)
        heading_lb=Label(createP_H,text="FIREWALL",bg="white",font="40").place(x=400,y=100)

        btn_install = Button(createP_H,text="Turn On",bg="#b0d46c",width=20,command=self.turnonFirewall)
        btn_install.place(x=400, y=240)
        btn_install = Button(createP_H,text="Turn Off",bg="#b0d46c",width=20,command=self.turnoffFirewall)
        btn_install.place(x=400, y=440)
        
    def turnoffFirewall():
        commmand = "netsh advfirewall set allprofiles state off"
        sendCommand(commmand)

    def turnonFirewall():
        commmand = "netsh advfirewall set allprofiles state on"
        sendCommand(commmand)

if __name__ == "__main__":    
    root = Tk()
    obj = Firewall(root)
    root.mainloop()
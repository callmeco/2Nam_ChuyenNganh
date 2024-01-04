from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class InstallTelnet:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        createP_H = LabelFrame(self.root,text="Install Telnet Service",bg='white',bd=2,relief=RIDGE)
        createP_H.place(x=10,y=20,width=1000,height=550)
        heading_lb=Label(createP_H,text="Install Telnet Service",bg="white",font="40").place(x=400,y=100)

        btn_install = Button(createP_H,text="Install",bg="#b0d46c",width=20,command=self.installService)
        btn_install.place(x=400, y=340)
        
    def installService(self):
        command = "powershell.exe Install-WindowsFeature -name telnet-clients"
        try:
            sendCommand(command)
            os.system(command)
        except Exception as Err:
            print('Đã xảy ra lỗi: ', str(Err))

if __name__ == "__main__":    
    root = Tk()
    obj = InstallTelnet(root)
    root.mainloop()
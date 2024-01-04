from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class ChangePassword:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_username= StringVar()
        self.var_password= StringVar()

        readCsvFrame = LabelFrame(self.root,text="Change Password Into QTM2023@",bg='white',bd=2,relief=RIDGE)
        readCsvFrame.place(x=10,y=20,width=1000,height=550)
        ten_lb=Label(readCsvFrame,text="Nhập file CSV",bg="white",font="22").place(x=200,y=100)
        ten_Entry=Entry(readCsvFrame,bg="lightgrey",width=80,textvariable=self.var_username)
        ten_Entry.place(x=400,y=105)
        btn_create = Button(readCsvFrame,text="Accept",bg="#b0d46c",width=20,command=self.executed)
        btn_create.place(x=500, y=295)
        
    def splitName(self,ho_ten):
        ten=ho_ten.split(" ")
        ten_tam=ten[-1]
        for i in range(len(ten)-1):
            ten_tam=ten_tam+ten[i][0]
        return ten_tam   
    def createNewPassword(file):
        f = pd.read_csv(file)
        us = DataFrame(f, columns=['Fullname'])
        for i in range(len(us)):
            command = f"dsmod user " + chr(34) + "cn=" + splitName(us.iloc[i,0]) + chr(34)+" -pwd QTM@2023"
            sendCommand(command)
    def executed(self):
            file = self.var_username.get()
            f = pd.read_csv(file)
            ou = DataFrame(f, columns=['OU'])
            for i in range(len(ou)):
                if file:
                    command = f'dsadd ou "OU={ou.iloc[i,0]},ou=QTM_CTY,dc=qlab,dc=com"'
                    sendCommand(command)
                    self.createNewPassword(file)
                break
if __name__ == "__main__":    
    root = Tk()
    obj = ChangePassword(root)
    root.mainloop()
from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class CreateOU:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_ou= StringVar()

        readCsvFrame = LabelFrame(self.root,text="Create OU",bg='white',bd=2,relief=RIDGE)
        readCsvFrame.place(x=10,y=20,width=1000,height=550)
        ten_lb=Label(readCsvFrame,text="Nhập OU",bg="white",font="22").place(x=200,y=100)
        ten_Entry=Entry(readCsvFrame,bg="lightgrey",width=80,textvariable=self.var_ou)
        ten_Entry.place(x=400,y=105)

        btn_create = Button(readCsvFrame,text="Accept",bg="#b0d46c",width=20,command=self.executed)
        btn_create.place(x=500, y=295)
        
    def createOU(self,ou):
        command = f'dsadd ou "OU={ou},dc=qlab,dc=com"'
        sendCommand(command)
        os.system(command)
    def executed(self):
            ou = self.var_ou.get()
            if ou and domain:
                self.createOU(ou)

if __name__ == "__main__":    
    root = Tk()
    obj = CreateOU(root)
    root.mainloop()
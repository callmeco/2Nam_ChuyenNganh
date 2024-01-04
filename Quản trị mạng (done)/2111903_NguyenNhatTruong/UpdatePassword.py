from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class UpdatePassword:
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

        updatePwdFrame = LabelFrame(self.root,text="Update Password",bg='white',bd=2,relief=RIDGE)
        updatePwdFrame.place(x=10,y=20,width=1000,height=550)
        username_lb=Label(updatePwdFrame,text="Nhập họ tên",bg="white",font="22").place(x=200,y=100)
        username_Entry=Entry(updatePwdFrame,bg="lightgrey",width=80,textvariable=self.var_username)
        username_Entry.place(x=400,y=105)
        password_lb=Label(updatePwdFrame,text="Password mới",bg="white",font="22").place(x=200,y=145)
        password_Entry=Entry(updatePwdFrame,bg="lightgrey",width=80,textvariable=self.var_password)
        password_Entry.place(x=400,y=150)
        ou_lb=Label(updatePwdFrame,text="Nhập OU",bg="white",font="22").place(x=200,y=190)
        ou_Entry=Entry(updatePwdFrame,bg="lightgrey",width=80,textvariable=self.var_ou)
        ou_Entry.place(x=400,y=195)
        domain_lb=Label(updatePwdFrame,text="Nhập domain",bg="white",font="22").place(x=200,y=235)
        domain_Entry=Entry(updatePwdFrame,bg="lightgrey",width=80,textvariable=self.var_domain)
        domain_Entry.place(x=400,y=240)

        btn_create = Button(updatePwdFrame,text="Update",bg="#b0d46c",width=20,command=self.changePwd)
        btn_create.place(x=500, y=295)
        
    def changePwd(self):
        user = self.var_username.get()
        passwd = self.var_password.get()
        ou = self.var_ou.get()
        if user and passwd and ou:
            changePassword(user, passwd, ou)
        else: 
            messagebox.showerror('Lỗi', 'Hãy nhập đầy đủ thông tin')

if __name__ == "__main__":    
    root = Tk()
    obj = UpdatePassword(root)
    root.mainloop()
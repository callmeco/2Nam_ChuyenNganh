from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class UserForm:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1080x560+320+185")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_username= StringVar()
        self.var_username1= StringVar()
        self.var_username2= StringVar()
        self.var_username3= StringVar()
        self.var_username4= StringVar()
        self.var_username5= StringVar()
        self.var_password = StringVar()
        self.var_newpass = StringVar()
        self.var_ou = StringVar()
        self.var_ou1 = StringVar()
        self.var_ou2 = StringVar()
        self.var_ou3 = StringVar()
        self.var_ou4 = StringVar()
        self.var_file = StringVar()

        createUserFrame = LabelFrame(self.root,text="Create User",bg='white',bd=2,relief=RIDGE)
        createUserFrame.place(x=10,y=20,width=350,height=100)
        username_lb=Label(createUserFrame,text="Nhập họ tên",bg="white").place(x=20,y=10)
        username_Entry=Entry(createUserFrame,bg="lightgrey",textvariable=self.var_username)
        username_Entry.place(x=120,y=10)
        password_lb=Label(createUserFrame,text="Nhập password",bg="white").place(x=20,y=30)
        password_Entry=Entry(createUserFrame,bg="lightgrey",textvariable=self.var_password)
        password_Entry.place(x=120,y=30)
        ou_lb=Label(createUserFrame,text="Nhập OU",bg="white").place(x=20,y=50)
        ou_Entry=Entry(createUserFrame,bg="lightgrey",textvariable=self.var_ou)
        ou_Entry.place(x=120,y=50)
        btn_create = Button(createUserFrame,text="Create",bg="#b0d46c",width=10,command=self.taoUser)
        btn_create.place(x=250, y=40)

        updatePasswordFrame = LabelFrame(self.root,text="Update Password For User",bg='white',bd=2,relief=RIDGE)
        updatePasswordFrame.place(x=10,y=150,width=350,height=100)
        username_lb=Label(updatePasswordFrame,text="Nhập họ tên",bg="white").place(x=20,y=10)
        username_Entry=Entry(updatePasswordFrame,bg="lightgrey",textvariable=self.var_username1)
        username_Entry.place(x=120,y=10)
        password_lb=Label(updatePasswordFrame,text="Password mới",bg="white").place(x=20,y=30)
        password_Entry=Entry(updatePasswordFrame,bg="lightgrey",textvariable=self.var_newpass)
        password_Entry.place(x=120,y=30)
        ou_lb=Label(updatePasswordFrame,text="Nhập OU",bg="white").place(x=20,y=50)
        ou_Entry=Entry(updatePasswordFrame,bg="lightgrey",textvariable=self.var_ou1)
        ou_Entry.place(x=120,y=50)       
        btn_update = Button(updatePasswordFrame,text="Update",bg="#b0d46c",width=10,command=self.capnhatMK)
        btn_update.place(x=250, y=40) 

        deleteUserFrame = LabelFrame(self.root,text="Delete User",bg='white',bd=2,relief=RIDGE)
        deleteUserFrame.place(x=10,y=280,width=350,height=100)
        username_lb=Label(deleteUserFrame,text="Nhập họ tên",bg="white").place(x=20,y=10)
        username_Entry=Entry(deleteUserFrame,bg="lightgrey",textvariable=self.var_username2)
        username_Entry.place(x=120,y=10)
        ou_lb=Label(deleteUserFrame,text="Nhập OU",bg="white").place(x=20,y=30)
        ou_Entry=Entry(deleteUserFrame,bg="lightgrey",textvariable=self.var_ou2)
        ou_Entry.place(x=120,y=30) 
        btn_delete = Button(deleteUserFrame,text="Delete",bg="#b0d46c",width=10,command=self.xoaUser)
        btn_delete.place(x=250, y=20)  

        createPnHFrame = LabelFrame(self.root,text="Create Profile & Homedir For User",bg='white',bd=2,relief=RIDGE)
        createPnHFrame.place(x=380,y=20,width=450,height=230)
        file_lb=Label(createPnHFrame,text="Nhập file",bg="white").place(x=20,y=10)
        file_Entry=Entry(createPnHFrame,bg="lightgrey",width=50,textvariable=self.var_file)
        file_Entry.place(x=120,y=10)
        username_lb=Label(createPnHFrame,text="Nhập username",bg="white").place(x=20,y=60)
        username_Entry=Entry(createPnHFrame,bg="lightgrey",width=50,textvariable=self.var_username3)
        username_Entry.place(x=120,y=60)
        ou_lb=Label(createPnHFrame,text="Nhập OU",bg="white").place(x=20,y=110)
        ou_Entry=Entry(createPnHFrame,bg="lightgrey",width=50,textvariable=self.var_ou3)
        ou_Entry.place(x=120,y=110)
        btn_create = Button(createPnHFrame,text="Create",bg="#b0d46c",width=10,command=self.taoHomedirProfile)
        btn_create.place(x=200, y=150)  

        activeUserFrame = LabelFrame(self.root,text="Enable - Disable User",bg='white',bd=2,relief=RIDGE)
        activeUserFrame.place(x=10,y=410,width=350,height=100)
        username_lb=Label(activeUserFrame,text="Nhập username",bg="white").place(x=20,y=30)
        username_Entry=Entry(activeUserFrame,bg="lightgrey",width=20,textvariable=self.var_username4)
        username_Entry.place(x=120,y=30)
        btn_enable = Button(activeUserFrame,text="Enable",bg="#b0d46c",width=10,command=self.batUser)
        btn_enable.place(x=250, y=5)
        btn_disable = Button(activeUserFrame,text="Disable",bg="#b0d46c",width=10,command=self.tatUser)
        btn_disable.place(x=250, y=40)

        createOUFrame = LabelFrame(self.root,text="Create OU",bg='white',bd=2,relief=RIDGE)
        createOUFrame.place(x=380,y=280,width=450,height=100)
        ou_lb=Label(createOUFrame,text="Nhập OU",bg="white").place(x=20,y=30)
        ou_Entry=Entry(createOUFrame,bg="lightgrey",width=20,textvariable=self.var_username4)
        ou_Entry.place(x=120,y=30)
        btn_create = Button(createOUFrame,text="Tạo",bg="#b0d46c",width=10,command=self.taoOU)
        btn_create.place(x=250, y=25)

        remoteDesktopFrame = LabelFrame(self.root,text="Remote Desktop For User",bg='white',bd=2,relief=RIDGE)
        remoteDesktopFrame.place(x=380,y=410,width=450,height=100)
        username_lb=Label(remoteDesktopFrame,text="Nhập username",bg="white").place(x=20,y=30)
        username_Entry=Entry(remoteDesktopFrame,bg="lightgrey",width=20,textvariable=self.var_username5)
        username_Entry.place(x=120,y=30)
        btn_confirm = Button(remoteDesktopFrame,text="Confirm",bg="#b0d46c",width=10,command=self.remote)
        btn_confirm.place(x=250, y=25)
        
    def taoUser(self):
        user = self.var_username.get()
        passwd = self.var_password.get()
        ou = self.var_ou.get()
        if user and passwd and ou:
            createUsers_withOU(user, passwd, ou)
        else: 
            messagebox.showerror('Lỗi', 'Hãy nhập đầy đủ thông tin')
    
    def capnhatMK(self):
        user = self.var_username1.get()
        passwd = self.var_newpass.get()
        ou = self.var_ou1.get()
        if user and passwd and ou:
            changePassword(user, passwd, ou)
        else: 
            messagebox.showerror('Lỗi', 'Hãy nhập đầy đủ thông tin')
    
    def xoaUser(self):
        user = self.var_username2.get()
        ou = self.var_ou2.get()
        if user and ou:
            deleteUser(user, ou)
        else: 
            messagebox.showerror('Lỗi', 'Hãy nhập đầy đủ thông tin')
        
    def taoHomedirProfile(self):
        file = self.var_file.get()
        user = self.var_username3.get()
        ou = self.var_ou3.get()
        if user and ou:
            createProfile_Homedir(user, ou,file)
        else: 
            messagebox.showerror('Lỗi', 'Hãy nhập đầy đủ thông tin')

    def batUser(self):
        user = self.var_username4.get()
        if user:
            enableUser(user)
        else:
            messagebox.showerror("Lỗi","Phải nhập đúng username")
    
    def tatUser(self):
        user = self.var_username4.get()
        if user:
            disableUser(user)
        else:
            messagebox.showerror("Lỗi","Phải nhập đúng username")
    
    def remote(self):
        user = self.var_username5.get()
        if user:
            remoteDesktop(user)
        else:
            messagebox.showerror("Lỗi","Phải nhập đúng username")
    
    def taoOU(self):
        ou = self.var_ou4.get()
        if ou:
            remoteDesktop(ou)
        else:
            messagebox.showerror("Lỗi","Phải nhập đúng ou")
        
if __name__ == "__main__":    
    root = Tk()
    obj = UserForm(root)
    root.mainloop()
from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class DeleteUser:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_username= StringVar()
        self.var_ou= StringVar()

        delete_user = LabelFrame(self.root,text="Delete User",bg='white',bd=2,relief=RIDGE)
        delete_user.place(x=10,y=20,width=1000,height=550)
        username_lb=Label(delete_user,text="Nhập họ tên",bg="white",font="22").place(x=200,y=100)
        username_Entry=Entry(delete_user,bg="lightgrey",width=80,textvariable=self.var_username)
        username_Entry.place(x=400,y=105)
        ou_lb=Label(delete_user,text="Nhập OU",bg="white",font="22").place(x=200,y=190)
        ou_Entry=Entry(delete_user,bg="lightgrey",width=80,textvariable=self.var_ou)
        ou_Entry.place(x=400,y=195)

        btn_delete = Button(delete_user,text="Delete",bg="#b0d46c",width=20,command=self.executed)
        btn_delete.place(x=500, y=340)

    def splitName(ho_ten):
        ten=ho_ten.split(" ")
        ten_tam=ten[-1]
        for i in range(len(ten)-1):
            ten_tam=ten_tam+ten[i][0]
        return ten_tam
    def deleteUser(username, ou):
        domain = 'dc=qlab,dc=com'
        username = splitName(username)
        command1 = f'dsrm "CN={username},OU={ou},{domain}"'
        print(command1)
        sendCommand(command1)
        sendCommand("y")
    def executed(self):
            user = self.var_username.get()
            ou = self.var_ou.get()
            if user and ou:
                deleteUser(user, ou)

if __name__ == "__main__":    
    root = Tk()
    obj = DeleteUser(root)
    root.mainloop()
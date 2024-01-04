from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
class CopyFile:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_source= StringVar()
        self.var_dest= StringVar()

        delete_user = LabelFrame(self.root,text="Copy File .txt",bg='white',bd=2,relief=RIDGE)
        delete_user.place(x=10,y=20,width=1000,height=550)
        username_lb=Label(delete_user,text="Nhập thư mục nguồn",bg="white",font="22").place(x=200,y=100)
        username_Entry=Entry(delete_user,bg="lightgrey",width=80,textvariable=self.var_source)
        username_Entry.place(x=400,y=105)
        ou_lb=Label(delete_user,text="Nhập thư mục đích",bg="white",font="22").place(x=200,y=190)
        ou_Entry=Entry(delete_user,bg="lightgrey",width=80,textvariable=self.var_dest)
        ou_Entry.place(x=400,y=195)

        btn_delete = Button(delete_user,text="Delete",bg="#b0d46c",width=20,command=self.executed)
        btn_delete.place(x=500, y=340)
        
    def copyFile(self,source,dest):
        source = self.var_source.get()
        dest = self.var_dest.get()
        os.system(f'copy "{source}" "{dest}"')
        sendCommand(f'copy "{source}" "{dest}"')
    def executed(self):
        source = self.var_source.get()
        dest = self.var_dest.get()
        if source and dest:
            self.copyFile(source, dest)

if __name__ == "__main__":    
    root = Tk()
    obj = CopyFile(root)
    root.mainloop()
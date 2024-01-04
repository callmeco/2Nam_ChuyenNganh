from tkinter import *
from tkinter import ttk
from AAD_CLIENT import *
class CopyForm:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1080x560+320+185")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_source = StringVar()
        self.var_dest = StringVar()

        mainFrame = LabelFrame(self.root,text="Copy File",bg='white',bd=2,relief=RIDGE)
        mainFrame.place(x=280,y=10,width=550,height=400)

        source_lb=Label(mainFrame,text="Địa chỉ thư mục nguồn",bg="white")
        source_lb.place(x=20,y=30)
        source_Entry=Entry(mainFrame,bg="lightgrey",width=60)
        source_Entry.place(x=150,y=30)

        dest_lb = Label(mainFrame,text="Địa chỉ thư mục đích",bg="white")
        dest_lb.place(x=20,y=60)
        dest_Entry=Entry(mainFrame,bg="lightgrey",width=60)
        dest_Entry.place(x=150,y=60)

        btn_confirm = Button(mainFrame,text="Confirm",bg="#b0d46c",cursor='hand2',width=10,command=self.copyfile)
        btn_confirm.place(x=250,y=100)

    def copyfile(self):
        source = self.var_source.get()
        dest = self.var_dest.get()
        copyFile(source,dest)

if __name__ == "__main__":    
    root = Tk()
    obj = CopyForm(root)
    root.mainloop()
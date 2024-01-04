from tkinter import *
from AAD_CLIENT import *
from tkinter import messagebox
import csv
class ReadCSV:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1030x620+370+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_source= StringVar()

        readCsvFrame = LabelFrame(self.root,text="Deploy Foxi",bg='white',bd=2,relief=RIDGE)
        readCsvFrame.place(x=10,y=20,width=1000,height=550)
        ten_lb=Label(readCsvFrame,text="Nhập thư mục nguồn",bg="white",font="22").place(x=200,y=100)
        ten_Entry=Entry(readCsvFrame,bg="lightgrey",width=80,textvariable=self.var_source)
        ten_Entry.place(x=400,y=105)

        btn_create = Button(readCsvFrame,text="Accept",bg="#b0d46c",width=20,command=self.executed)
        btn_create.place(x=500, y=295)
        
    def deployFoxiReader(self,path_foxit):
        try:
            os.system(f'msiexrc","/i",{path_foxit},"/qn')
        except Exception as e:
            return None
        
    def executed(self):
        source = self.var_source.get()
        if source:
            self.deployFoxiReader(source)

if __name__ == "__main__":    
    root = Tk()
    obj = ReadCSV(root)
    root.mainloop()
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

        self.var_username= StringVar()
        self.var_password= StringVar()
        self.var_ou= StringVar()
        self.var_domain= StringVar()

        readCsvFrame = LabelFrame(self.root,text="Read CSV File",bg='white',bd=2,relief=RIDGE)
        readCsvFrame.place(x=10,y=20,width=1000,height=550)
        ten_lb=Label(readCsvFrame,text="Nhập file CSV",bg="white",font="22").place(x=200,y=100)
        ten_Entry=Entry(readCsvFrame,bg="lightgrey",width=80,textvariable=self.var_username)
        ten_Entry.place(x=400,y=105)

        btn_create = Button(readCsvFrame,text="Accept",bg="#b0d46c",width=20,command=self.readCSV)
        btn_create.place(x=500, y=295)
        
    def readCSV(file):
        user_data = []
        file_path = 'DSSV.csv'
        try: 
            with open(file_path, newline='', encoding='utf8') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if len(row) >= 3:
                        user = {
                            'user' : row[0],
                            'ou' : row[1],
                            'passwd' : row[2]
                        }
                        user_data.append(user)
                    sendCommand(print(user_data))
                return user_data
        except Exception as e:
            print(e)
            return None

if __name__ == "__main__":    
    root = Tk()
    obj = ReadCSV(root)
    root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
import PIL.Image

from CreateUser import *
from UpdatePassword import *
from DeleteUser import *
from Profile_Homedir import *
from InstallWeb import *
from InstallTelnet import *
from ReadCSVFile import *
from CreateOU import *
from CreateOUFromCSV import *
from CreateUserFromCSV import *
from CreateProfile import *
from ChangePassword import *
from RemoteDesktop import *
from CopyFile import *
from DeployFoxi import *
from Firewall import *
from EnableUser import *
class AAD(Tk):
        def __init__(self):
                super().__init__()

                self.geometry('1280x720+120+50')
                self.title('Automate Active Directory')
                self.resizable(False,False)

                headingFrame = Frame(self, width=1280, height=70, bg="#b0d46c")
                headingFrame.place(x=0, y=0)
                headingTitle = Label(self, text="HỆ THỐNG QUẢN LÝ SERVER", font=('bold',40), bg="#b0d46c", fg="white")
                headingTitle.place(x=250, y=0)

                leftMenu=Frame(self,bd=2,relief=RIDGE)
                leftMenu.place(x=0,y=70,width=250,height=650)

                cau1 = Button(leftMenu, text="Create User", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau1)
                cau1.place(x=0,y=0)
                cau2 = Button(leftMenu, text="Update Password", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau2)
                cau2.place(x=0,y=30)
                cau3 = Button(leftMenu, text="Create Profile & Homedir", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau3)
                cau3.place(x=0,y=60)
                cau4 = Button(leftMenu, text="Delete User", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau4)
                cau4.place(x=0,y=90)
                cau5 = Button(leftMenu, text="Install Web", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau5)
                cau5.place(x=0,y=120)
                cau6 = Button(leftMenu, text="Install Telnet", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau6)
                cau6.place(x=0,y=150)
                cau7 = Button(leftMenu, text="Read CSV File", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau7)
                cau7.place(x=0,y=180)
                cau8 = Button(leftMenu, text="Create OU", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau8)
                cau8.place(x=0,y=210)
                cau9 = Button(leftMenu, text="Create OU From CSV File", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau9)
                cau9.place(x=0,y=240)
                cau10 = Button(leftMenu, text="Create User From CSV File", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau10)
                cau10.place(x=0,y=270)
                cau11 = Button(leftMenu, text="Create Profile For User", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau11)
                cau11.place(x=0,y=300)
                cau12 = Button(leftMenu, text="Change Password Into QTM2023@", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau12)
                cau12.place(x=0,y=330)
                cau13 = Button(leftMenu, text="Remote Desktop", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau13)
                cau13.place(x=0,y=360)
                cau14 = Button(leftMenu, text="Copy File", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau14)
                cau14.place(x=0,y=390)
                cau15 = Button(leftMenu, text="Deploy Foxi Reader", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau15)
                cau15.place(x=0,y=420)
                cau16 = Button(leftMenu, text="User Setting", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau16)
                cau16.place(x=0,y=450)
                cau17 = Button(leftMenu, text="Firewall", fg="Black",bg="#b0d46c", font=('bold',11),width=26,height=1, command=self.showCau17)
                cau17.place(x=0,y=480)

        def showCau1(self):
               self.newForm = Toplevel(self)
               self.app = CreateUser(self.newForm)
        def showCau2(self):
               self.newForm = Toplevel(self)
               self.app = UpdatePassword(self.newForm)
        def showCau3(self):
               self.newForm = Toplevel(self)
               self.app = CreateProfile_Homedir(self.newForm)
        def showCau4(self):
               self.newForm = Toplevel(self)
               self.app = DeleteUser(self.newForm)   
        def showCau5(self):
               self.newForm = Toplevel(self)
               self.app = InstallWeb(self.newForm) 
        def showCau6(self):
               self.newForm = Toplevel(self)
               self.app = InstallTelnet(self.newForm) 
        def showCau7(self):
               self.newForm = Toplevel(self)
               self.app = ReadCSV(self.newForm)
        def showCau8(self):
               self.newForm = Toplevel(self)
               self.app = CreateOU(self.newForm) 
        def showCau9(self):
               self.newForm = Toplevel(self)
               self.app = CreateOUFromCSV(self.newForm) 
        def showCau10(self):
               self.newForm = Toplevel(self)
               self.app = CreateUserFromCSV(self.newForm) 
        def showCau11(self):
               self.newForm = Toplevel(self)
               self.app = CreateProfile(self.newForm) 
        def showCau12(self):
               self.newForm = Toplevel(self)
               self.app = ChangePassword(self.newForm) 
        def showCau13(self):
               self.newForm = Toplevel(self)
               self.app = RemoteDesktop(self.newForm)     
        def showCau14(self):
               self.newForm = Toplevel(self)
               self.app = CopyFile(self.newForm)  
        def showCau15(self):
               self.newForm = Toplevel(self)
               self.app = deployFoxiReader(self.newForm)
        def showCau16(self):
               self.newForm = Toplevel(self)
               self.app = EnableUser(self.newForm)
        def showCau17(self):
               self.newForm = Toplevel(self)
               self.app = Firewall(self.newForm)  
if __name__ == "__main__": 
    obj = AAD()
    obj.mainloop()
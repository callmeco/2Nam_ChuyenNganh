from tkinter import *
from tkinter import ttk
from AAD_CLIENT import *
class ServiceForm:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1080x560+320+185")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.title("Automate Active Directory")
        self.root.resizable(False,False)

        self.var_source=StringVar()
        self.var_dest = StringVar()

        createWebFrame = LabelFrame(self.root,text="Create Web Service",bg='white',bd=2,relief=RIDGE)
        createWebFrame.place(x=10,y=20,width=350,height=100)
        webService_lb=Label(createWebFrame,text="Cài đặt dịch vụ Web",bg="white")
        webService_lb.place(x=20,y=30)
        btn_webService = Button(createWebFrame,text="Install",width=15,bg="#b0d46c",command=installWebService)
        btn_webService.place(x=170,y=5)
        btn_webService = Button(createWebFrame,text="Uninstall",width=15,bg="#b0d46c",command=unistallWebService)
        btn_webService.place(x=170,y=40)

        createPnHFrame = LabelFrame(self.root,text="Create Telnet Service",bg='white',bd=2,relief=RIDGE)
        createPnHFrame.place(x=400,y=20,width=350,height=100) 
        telnetService_lb=Label(createPnHFrame,text="Cài đặt dịch vụ Telnet",bg="white")
        telnetService_lb.place(x=20,y=30)
        btn_telnetService = Button(createPnHFrame,text="Install",width=15,bg="#b0d46c",command=installTelnetService)
        btn_telnetService.place(x=170,y=5) 
        btn_telnetService = Button(createPnHFrame,text="Uninstall",width=15,bg="#b0d46c",command=unistallTelnetService)
        btn_telnetService.place(x=170,y=40)

        deployFoxiFrame = LabelFrame(self.root,text="Deploy FoxiReader",bg='white',bd=2,relief=RIDGE)
        deployFoxiFrame.place(x=10,y=150,width=350,height=150)
        source_lb=Label(deployFoxiFrame,text="Địa chỉ thư mục nguồn",bg="white")
        source_lb.place(x=20,y=30)
        source_Entry=Entry(deployFoxiFrame,bg="lightgrey",width=30)
        source_Entry.place(x=150,y=30) 
        dest_lb = Label(deployFoxiFrame,text="Địa chỉ thư mục đích",bg="white")
        dest_lb.place(x=20,y=60)
        dest_Entry=Entry(deployFoxiFrame,bg="lightgrey",width=30)
        dest_Entry.place(x=150,y=60)
        btn_confirm = Button(deployFoxiFrame,text="Confirm",bg="#b0d46c",cursor='hand2',width=10,command=self.caidatFoxiReader)
        btn_confirm.place(x=150,y=80)    

        firewallFrame = LabelFrame(self.root,text="Firewall Setting",bg='white',bd=2,relief=RIDGE)
        firewallFrame.place(x=400,y=150,width=350,height=100) 
        firewall_lb=Label(firewallFrame,text="Firewall",bg="white")
        firewall_lb.place(x=20,y=30)
        btn_turnoffFirewall = Button(firewallFrame,text="Turn Off",width=15,bg="#b0d46c",command=turnoffFirewall)
        btn_turnoffFirewall.place(x=170,y=5) 
        btn_turnonFirewall = Button(firewallFrame,text="Turn On",width=15,bg="#b0d46c",command=turnonFirewall)
        btn_turnonFirewall.place(x=170,y=40)


    def caidatFoxiReader(self):
        source = self.var_source.get()
        dest = self.var_dest.get()
        deployFoxiReader(source,dest)
if __name__ == "__main__":    
    root = Tk()
    obj = ServiceForm(root)
    root.mainloop()
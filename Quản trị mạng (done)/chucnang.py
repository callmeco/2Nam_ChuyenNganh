import os
import pandas as pd

def tachTen(ho_ten):
    tenm=ho_ten.split(" ")
    tam=tenm[-1]
    for i in range(len(tenm)-1):
        tam=tam+tenm[i][0]
    return tam
def taoUser(username, password, ou, domain):
    username = tachTen(username)
    command = "dsadd user " + chr(34) + "cn=" + username + ",ou=" + ou + "," + domain + chr(34) + " -pwd " + password
    print(command)
def taoOU(ou, domain):
    command = "dsadd ou "+chr(34)+"ou="+ou+","+domain+chr(34)
    print(command)
    os.system(command)
def doiMatKhau(username, password, ou, domain):
    username = tachTen(username)
    command = "dsmod user "+chr(34)+"cn="+username+",ou="+ou+","+domain+chr(34)+" -pwd "+password
    print(command)
    os.system(command)
def xoaUser(username, ou, domain):
    username = tachTen(username)
    command = "dsrm "+chr(34)+"cn="+username+",ou="+ou+","+domain+chr(34)
    print(command)
    os.system(command)
def taoProfile(username, ou, domain):
    username = tachTen(username)
    ipServer = input("Nhap IP cua Server: ")
    nameFolder = input("Nhap ten thu muc muon tao Profile: ")
    password = input("Nhap password moi: ")
    cmdMKDir = "mkdir C:\\"+nameFolder
    os.system(cmdMKDir)
    cmdShare = "net share "+nameFolder+"=C:\\"+nameFolder+" /grant:everyone,full"
    print(cmdShare)
    os.system(cmdShare)
    pathProfile =  " -profile "+chr(92)+chr(92)+ipServer+"\\profile\\"+username
    print(pathProfile)
    pathHomeDir = " -hmdir " + chr(92) + chr(92) + "192.168.65.136\\dungchung\\" + username + " -hmdrv Z: "
    command = "dsmod user "+ chr(34)+"cn="+username+",ou="+ou+","+domain+chr(34)+pathProfile
    print(command)
    print(pathHomeDir)
    os.system(command)
def installService():
    cmd1 = " powershell.exe Install-WindowsFeature - name Web-Server -IncludeManagementTools"
    cmd = " powershell.exe Install-WindowsFeature -name telnet-client"
    os.system(cmd)
def DocFile():
    file = pd.read_csv('DATASERVER1.csv')
    print(file)
def TaoOU():
    file = pd.read_csv('DATASERVER1.csv')
    a = file.iloc[:,1].unique()
    print("dsadd ou "+chr(34)+"ou="+a+",ou=QTM_CTY,dc=qlab,dc=com")
def Thoat():
    exit()
while True:
    print("Nhan 0: De thoat chuong trinh")
    print("Nhan 1: Tao User")
    print("Nhan 2: Doi mat khau User")
    print("Nhan 3: Tao profile và homedir cho User")
    print("Nhan 4: Xoa User")
    print("Nhan 5: Mo file CSV")
    print("Nhan 6: Tao OU")
    print("Nhan 7: ")
    print("Nhan 5: De doc User")
    chon = int(input("Nhap lua chon cua ban: "))
    if chon ==0:
        Thoat()
    elif chon == 1:
        username = input('Nhap ten user: ')
        password = input("Nhap mat khau: ")
        taoUser(username,password,"data","dc=qlab,dc=com")
    elif chon == 2:
        username = input("Nhap username: ")
        newpassword = input("Nhap mat khau moi: ")
        ou = input("Nhap OU: ")
        domain = "dc=qlab,dc=com"
        doiMatKhau(username,newpassword,domain)
    elif chon == 3:
        username = input("Nhap username: ")
        ou = input("Nhap OU: ")
        domain = "dc=qlab,dc=com"
        taoProfile(username,ou,domain)
    elif chon == 4:
        username = input("Nhap user can xoa: ")
        ou = input("Nhap OU: ")
        domain = "dc=qlab,dc=com"
        xoaUser(username, ou, domain)
    elif chon == 5:
        DocFile()    
    elif chon ==6:
        TaoOU()
    else:
        username = input("Nhap username: ")
        ou = input("Nhap OU: ")
        domain = ("dc=qlab,dc=com")
        xoaUser(username,ou,domain)
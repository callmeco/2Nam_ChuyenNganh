import rpyc
import pandas as pd
import os
from pandas import DataFrame
import shutil
import subprocess
from tkinter import messagebox

serverIP = '192.168.65.138'
port = 5900
domain = 'dc=qlab,dc=com'
def sendCommand(command):
    try:
        connection = rpyc.connect(serverIP, port)
        connection.root.run_command(command)
    except Exception as Err:
        print('Đã xảy ra lỗi: ', str(Err))

def splitName(ho_ten):
    ten=ho_ten.split(" ")
    ten_tam=ten[-1]
    for i in range(len(ten)-1):
        ten_tam=ten_tam+ten[i][0]
    return ten_tam

def changePassword(username, password, ou):
    username = splitName(username)
    command = "dsmod user "+chr(34)+"cn="+username+",ou="+ou+","+domain+chr(34)+" -pwd "+password
    print(command)
    os.system(command)
    sendCommand(command)

def createProfile_Homedir(username,ou,nameFolder):
    username = splitName(username)
    cmdMKDir = "mkdir C:\\"+nameFolder
    os.system(cmdMKDir)
    cmdShare = "net share "+nameFolder+"=C:\\"+ nameFolder
    os.system(cmdShare)
    pathProfile =  " -profile "+chr(92)+chr(92)+serverIP+"\\profile\\"+username
    command = "dsmod user "+ chr(34)+"cn="+username+",ou="+ou+","+domain+chr(34)+pathProfile
    pathHomeDir = " -hmdir " + chr(92) + chr(92) + "192.168.65.136\\dungchung\\" + username + " -hmdrv Z: "
    os.system(command)
    sendCommand(command)

def deleteUser(username, ou):
    username = splitName(username)
    command = "dsrm "+chr(34)+"cn="+username+",ou="+ou+","+domain+chr(34)
    print(command)
    os.system(command)
    sendCommand(command)

def installWebService():
    command = " powershell.exe Install-WindowsFeature - name Web-Server -IncludeManagementTools"
    os.system(command)
    sendCommand(command)

def installTelnetService():
    command = " powershell.exe Install-WindowsFeature -name telnet-client"
    os.system(command)
    sendCommand(command)

def unistallWebService():
    command = " powershell.exe Remove-WindowsFeature -name Web-Server"
    os.system(command)
    sendCommand(command) 

def unistallTelnetService():
    command = " powershell.exe Remove-WindowsFeature -name telnet-client"
    os.system(command)
    sendCommand(command)

def readCSV(file):
    command = pd.read_csv(file)
    print(command)

def createOU_fromCSV(file):
    f = pd.read_csv(file)
    ou = DataFrame(f, columns=['OU'])
    print("dsadd ou "+chr(34)+"ou="+ou+","+domain+chr(34))  

def createUser_fromCSV(file):
    f = pd.read_csv(file)
    us = DataFrame(f, columns=['Fullname'])
    ou = DataFrame(f, columns=['OU'])
    pwd = DataFrame(f, columns=['Password'])
    for i in range(len(us)):
        sendCommand("dsadd user " + chr(34) + "cn=" + splitName(us.iloc[i,0]) + ",ou=" + ou.iloc[i,0] + "," + domain + chr(34)+" -pwd "+pwd.iloc[i,0])    

def createProfile_fromUser(file):
    nameFolder = input("Nhập tên thư mục muốn tạo Profile: ")
    f = pd.read_csv(file)
    us = DataFrame(f, columns=['Fullname'])
    for i in range(len(us)):
        cmdMKDir = "mkdir C:\\"+nameFolder
        os.system(cmdMKDir)
        cmdShare = "net share "+nameFolder+"=C:\\"+nameFolder+" /grant:everyone,full"
        print(cmdShare)
        os.system(cmdShare)
        pathProfile =  " -profile "+chr(92)+chr(92)+serverIP+"\\profile\\"+splitName(us.iloc[i,0])
        print(pathProfile)
    
def createNewPassword(file,pwd):
    f = pd.read_csv(file)
    us = DataFrame(f, columns=['Fullname'])
    for i in range(len(us)):
        sendCommand("dsmod user" + chr(34) +"["+ splitName(us.iloc[i,0]) + "]"  + chr(34)+" -pwd "+pwd)

def remoteDesktop(username):
    sendCommand('NET LOCALGROUP "Remote Desktop Users"' + username + '/ADD')

def copyFile(source,dest):
    for file in os.listdir(source):
        if file.endswith('.txt'):
            shutil.copy(os.path.join(source, file),dest)

def deployFoxiReader(source,dest):
    shutil.copy(source,dest)
    sendCommand("msiexrc","/i",dest,"/qn")

def deployWebsite(name, root):
    sendCommand("inetmgr", "/createwebsite", "/name:%s" % name)
    sendCommand("inetmgr", "/editsite", "/name:%s" % name)
    sendCommand("inetmgr", "/bindings", "/add", "/name:http", "/protocol:http", "/port:80", "/site:%s" % name)
    sendCommand("inetmgr", "/homedirectory", "/apppool:DefaultAppPool", "/site:%s" % name, "/physicalpath:%s" % root)
    sendCommand("inetmgr", "/start", "/name:%s" % name)

def enableUser(username):
    command = "net user " + username + "/active:yes"
    sendCommand(command)

def disableUser(username):
    command = "net user " + username + "/active:no"
    sendCommand(command)

def turnoffFirewall():
    commmand = "netsh advfirewall set allprofiles state off"
    sendCommand(commmand)

def turnonFirewall():
    commmand = "netsh advfirewall set allprofiles state on"
    sendCommand(commmand)

def close():
    exit()


#///////////////////////////////////////////////////////////////////////////////////
#Tạo User
def createUsers_withOU(username, password, ou):
    try:
        if checkOU(ou):
            print("User này đã tồn tại")
        if not checkOU(ou):
            createParentOU(ou)
        return createUsers(username,password,ou)
    except Exception as es:
        messagebox.showwarning("Warning",f"Có sự cố đã xảy ra {str(es)}")

def createUsers(username, password, ou):
    username = splitName(username)
    command = "dsadd user " + chr(34) + "cn=" + username + ",ou=" + ou +","+ domain + chr(34) + " -pwd " + password
    sendCommand(command)
    return command != []

def checkOU(ou):
    output = sendCommand(f"dsquery ou OU={ou},DC=qlab,DC=com")
    return output == []

def createParentOU(ou):
    command = " dsadd ou " + chr(34) + "ou=" + ou +","+ domain +chr(34)
    sendCommand(command)
#///////////////////////////////////////////////////////////////////////////////////

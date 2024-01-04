import os
def TachTen(ho_ten):
    tenm=ho_ten.split(" ")
    tam=tenm[-1]
    for i in range(len(tenm)-1):
        tam=tam+tenm[i][0]
    return tam

ds = ["Nguyen Van Nam","Tran Le Chuan","Le Minh Hai"]
for ten in ds:
    TachTen(ten)


def tao1User(username, password, ou, domain):
    username = TachTen(username)
    pathProfile = " -profile " + chr(92)+ chr(92) + "192.168.65.129\\profiles\\" + username
    pathHomeDir = " -hmdir " + chr(92) + chr(92) + "192.168.65.129\\dungchung\\" + username + " -hmdrv Z: "
    pathScript = "-loscr " + chr(92) + chr(92) + "192.168.65.129\\Script\\map.bat"
    pwdneverexp = "-pwdnerverexpires yes"
    com = "dsadd user " + chr(34) + "cn=" + username + ",ou=" + ou + "," + domain + chr(34) + " -pwd " + password + pathHomeDir + pathScript + pathProfile
    os.system(com)
    print(com)
while True:
    linhnhapuservaoday = input("Nhap user")
    linhnhappassvoday = input("Nhap pass")
    tao1User(linhnhapuservaoday,linhnhappassvoday,"data","dc=qlab,dc=com")
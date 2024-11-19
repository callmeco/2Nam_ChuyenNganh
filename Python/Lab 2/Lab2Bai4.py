import math
class PhanSo:
    def __init__(self, tu =0, mau =1):
        self.tu = tu
        self.mau = mau
    
    def __str__(self) -> str:
        return "{}/{}".format(self.tu, self.mau)
    
    @staticmethod
    def UCLN(a, b):
        while(b):
            a, b = b, a % b
        return a

    def rutGon(self) -> None:
        ucln = self.UCLN(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu *other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu *other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.rutGon()
        return kq
    
class DanhSachPhanSo:
    def __init__(self) -> None:
        self.dsps = []

    def themPS(self, ps: PhanSo):
        self.dsps.append(ps)

    def xuatPS(self):
        for ps in self.dsps:
            print(ps)

    def laPSDuong(self, ps:PhanSo):
        if (ps.tu > 0 and ps.mau > 0) or (ps.tu < 0 and ps.mau < 0):
            return True
        return False
    
    def chiaPS(self, ps: PhanSo):
        return ps.tu / ps.mau

    def soSanhGiong(self, ps1: PhanSo, ps2: PhanSo):
        return (ps1.tu == ps2.tu and ps1.mau == ps2.mau)

    def mangPhanSoAm(self):
        return [ps for ps in self.dsps if not self.laPSDuong(ps)]

    def docFile(self):

        """file = 'D:\Đại Học Học Cũng Nhàn ;-;\Python\Lab 2\phanso.txt'
        docfile = open(file, "r")
        for x in docfile:
            s = x.split(",")
            ps = PhanSo(int(s[0]), int(s[1]))
            dsps.themPS(ps)"""

#câu 1
    def demSoPSAmTrongMang(self):
        dem = 0
        for ps in self.dsps:
            if(self.laPSDuong(ps)):
                pass
            else:
                dem += 1
        return dem

#câu 2
    def timPSDuongNhoNhat(self):
        min = 0
        kq = PhanSo()
        for ps in self.dsps:
            if(self.laPSDuong(ps)):
                min = self.chiaPS(ps)
                kq = ps
                break
        for ps in self.dsps:
            if (self.laPSDuong(ps) and self.chiaPS(ps) < min):
                min = self.chiaPS(ps)
                kq = ps
        return kq
#câu 3       
    def timVTPhanSo(self, phanso: PhanSo):
        vt = []
        for i in range(len(self.dsps)):
            if(self.soSanhGiong(self.dsps[i], phanso)):
                vt.append(i)
        return vt
#câu 4
    def tongPhanSoAm(self):
        sum = PhanSo(0, 1)
        for i in range(len(self.mangPhanSoAm())):
            sum = sum.__add__(self.mangPhanSoAm()[i])
        return sum
#câu 5    
    def xoaPSXTrongMang(self, phanso: PhanSo()):
        for i in range(len(self.dsps)):
            if self.timVTPhanSo(phanso):
                del self.dsps[i]
#câu 6                
    def xoaPSCoTuLaX(self, tuso: int):
        for ps in self.dsps:
            if (ps.tu == tuso):
                self.dsps.remove(ps)
#câu 7
    def sapXepPSTang(self, phanso: PhanSo()):
        return self.dsps.sort(key=lambda x: x.tu / x.mau)

    def sapXepGiam(self):
        return self.dsps.sort(key=lambda x: x.tu / x.mau, reverse=True)
    def tangTheoMau(self):
        return self.dsps.sort(key=lambda x: x.mau / x.tu)

    def giamTheoMau(self):
        return self.dsps.sort(key=lambda x: x.mau / x.tu, reverse=True)

ps1 = PhanSo(1, 2)
ps2 = PhanSo(3, 4)
ps3 = PhanSo(-3, 7)
ps4 = PhanSo(-4, 7)
ps5 = PhanSo(12, 5)
ps6 = PhanSo(-4, 7)

dsps = DanhSachPhanSo()
dsps.themPS(ps1)
dsps.themPS(ps2)
dsps.themPS(ps3)
dsps.themPS(ps4)
dsps.themPS(ps5)
dsps.themPS(ps6)
dsps.xuatPS()

demSoAm = dsps.demSoPSAmTrongMang()
print(f"Dem so am trong mang: {demSoAm}")

timPSDuong = dsps.timPSDuongNhoNhat()
print(f"Tim phan so duong nho nhat: {timPSDuong}")

timVT = dsps.timVTPhanSo(PhanSo(12, 5))
print(f"Tim vi tri cua phan so 12/5: {timVT}")

tongPSAm = dsps.tongPhanSoAm()
print(f"Tong tat cac cac phan so am trong mang: {tongPSAm}")

xoaPS = dsps.xoaPSXTrongMang(PhanSo(-3, 7))
print(f"Xoa phan so -3/7 trong mang thanh cong!")
dsps.xuatPS()

xoaPSTheoTu = dsps.xoaPSCoTuLaX(3)
print(f"Xoa phan so co tu la 3")
dsps.xuatPS()

"""dsps.sapXepPSTang()
print(f"Danh sach tang")
dsps.xuatPS()

dsps.sapXepGiam()
print(f"Danh sach giam")
dsps.xuatPS()

dsps.giamTheoMau()
print(f"Danh sach giam theo mau")
dsps.xuatPS()

dsps.tangTheoMau()
print(f"Danh sach tang theo mau")
dsps.xuatPS()"""


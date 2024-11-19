import math

class PhanSo:
    def __init__(self, tu =0, mau =1):
        self.tu = tu
        self.mau = mau
    
    """@property
    def tuSo(self):
        return self.tu
    
    @tuSo.setter
    def tuSo(self, tuso):
        self.tu = tuso
    
    @property
    def mauSo(self):
        return self.mau
    
    @mauSo.setter
    def mauSo(self, mauso):
        if mauso != 0:
            self.mau = mauso
        else:
            print("Khong hop le")"""
    
    def __str__(self) -> str:
        return "{}/{}".format(self.tu, self.mau)
    
    @staticmethod
    def UCLN(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def rutGon(self) -> None:
        """ucln = self.UCLN()
        tu = self._tu / ucln
        mau = self._mau / ucln
        phanso = PhanSo()
        phanso.tuSo=tu
        phanso.mauSo=mau
        return phanso"""
        ucln = self.UCLN(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def __add__(self, other):
        """tuThuNhat = self.tuSo
        mauThuNhat = self.mauSo
        tuThuHai = other.tuSo
        mauThuHai= other.mauSo
        phanso = PhanSo()
        phanso.tuSo = tuThuNhat * mauThuHai + tuThuHai * mauThuNhat
        phanso.mauSo = mauThuNhat * mauThuHai
        return phanso.rutGon()"""
        kq = PhanSo()
        kq.tu = self.tu *other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __sub__(self, other):
        """tuThuNhat = self.tuSo
        mauThuNhat = self.mauSo
        tuThuHai = other.tuSo
        mauThuHai= other.mauSo
        phanso = PhanSo()
        phanso.tuSo = tuThuNhat * mauThuHai - tuThuHai * mauThuNhat
        phanso.mauSo = mauThuNhat * mauThuHai
        return phanso.rutGon()"""
        kq = PhanSo()
        kq.tu = self.tu *other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __mul__(self, other):
        """tuThuNhat = self.tuSo
        mauThuNhat = self.mauSo
        tuThuHai = other.tuSo
        mauThuHai= other.mauSo
        phanso = PhanSo()
        phanso.tuSo = tuThuNhat * tuThuHai
        phanso.mauSo = mauThuNhat * mauThuHai
        return phanso.rutGon()"""
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __truediv__(self, other):
        """tuThuNhat = self.tuSo
        mauThuNhat = self.mauSo
        tuThuHai = other.tuSo
        mauThuHai= other.mauSo
        phanso = PhanSo()
        phanso.tuSo = tuThuNhat * mauThuHai
        phanso.mauSo = mauThuNhat * tuThuHai
        return phanso.rutGon()"""
        kq = PhanSo()
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.rutGon()
        return kq
    
a = PhanSo()
a.tu = 2
a.mau = 3
b = PhanSo(3, 5)
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
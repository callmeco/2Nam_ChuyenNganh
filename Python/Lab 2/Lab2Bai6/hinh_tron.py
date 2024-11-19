import math
from hinh_hoc import HinhHoc

class HinhTron(HinhHoc):
    def __init__(self, banKinh: float) -> None:
        self.__banKinh = banKinh
        super().__init__(banKinh)
    
    def HinhTron(self, banKinh: float):
        pass

    def tinhDienTich(self) -> float:
        return pow(self.__banKinh) * math.pi
    
    def xuat(self):
        print(self.__banKinh, self.tinhDienTich())

    @property
    def banKinh(self):
        return self._canh
    
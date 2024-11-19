from datetime import datetime

class SinhVien:
    truong = "Dai hoc Da Lat"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo=maSo
        self._hoTen=hoTen
        self._ngaySinh=ngaySinh
    
    @property
    def maSo(self):
        return self._maSo
    
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self._maSo=maso

    @property
    def hoTen(self):
        return self._hoTen
    
    @hoTen.setter
    def hoTen(self, hoTen):
        self._hoTen = hoTen

    @property
    def ngaySinh(self):
        return self._ngaySinh
    
    @ngaySinh.setter
    def ngaySinh(self, ngaySinh):
        self._ngaySinh = ngaySinh

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso))==7
    
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong=tenmoi
    
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"

    def xuat(self):
        print(f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}")
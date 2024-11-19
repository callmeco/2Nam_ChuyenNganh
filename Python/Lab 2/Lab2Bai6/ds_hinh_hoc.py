from hinh_chu_nhat import HinhChuNhat
from hinh_tron import HinhTron
from hinh_vuong import HinhVuong
from loai_hinh import LoaiHinh
from hinh_hoc import HinhHoc
import sys
class DanhSachHinhHoc:
    def __init__(self) -> None:
        self.dshh = []
    
    def themHH(self, hh: HinhHoc):
        self.dshh.append(hh)
        
    def xuat(self):
        for hh in self.dshh:
            print(hh)
    
    def readFile(self, fileName: str):
        f = open(fileName, 'r', encoding="utf8")
        lines = f.readlines()
        
        for line in lines:
            sp = line.split("*")
            if(int(sp[0]) == LoaiHinh.HinhVuong.value):
                hv = HinhVuong(float(sp[1]))
                self.themHH(hv)
            elif(int(sp[0]) == LoaiHinh.HinhChuNhat.value):
                hcn = HinhChuNhat(float(sp[1]), float(sp[2]))
                self.themHH(hcn)
            elif(int(sp[0]) == LoaiHinh.HinhTron.value):
                ht = HinhTron(float(sp[1]))
                self.themHH(ht)
        return self.dshh
    
    def timHinhCoDienTichLonNhat(self):
        max = 0
        result = HinhHoc(0)
        for hh in self.dshh:
            if(hh.dienTich > max):
                max = hh.dienTich
                result = hh
        return print(result)
    
    def timHinhCoDienTichNhoNhat(self):
        min = sys.maxsize
        result = HinhHoc(0)
        for hh in self.dshh:
            if(hh.dienTich < min):
                min = hh.dienTich
                result = hh
        return print(result)
    
    def timHinhCoDienTichLonNhatTheoLoai(self, loaiHinh: int):
        max = 0
        result = HinhHoc(0)
        if(loaiHinh == LoaiHinh.HinhTron):
            for hh in self.dshh:
                if(hh.dienTich > max and isinstance(hh, HinhTron)):
                    max = hh.dienTich
                    result = hh
        elif(loaiHinh == LoaiHinh.HinhVuong):
            for hh in self.dshh:
                if(hh.dienTich > max and isinstance(hh, HinhVuong)):
                    max = hh.dienTich
                    result = hh
        elif(loaiHinh == LoaiHinh.HinhChuNhat):
            for hh in self.dshh:
                if(hh.dienTich > max and isinstance(hh, HinhChuNhat)):
                    max = hh.dienTich
                    result = hh
        return print(result)
    
    def sapXepTheoDienTich(self):
        return self.dshh.sort(key= lambda x: x.dienTich, reverse=True)
    
    def demSoLuongHinhTheoLoai(self, loai: int):
        result = []
        if(loai == LoaiHinh.HinhTron):
            result = [hh for hh in self.dshh if isinstance(hh, HinhTron)]
        elif(loai == LoaiHinh.HinhVuong):
            result = [hh for hh in self.dshh if isinstance(hh, HinhVuong)]
        elif(loai == LoaiHinh.HinhChuNhat):
            result = [hh for hh in self.dshh if isinstance(hh, HinhChuNhat)]
        return f"Co {len(result)} {loai}"
    
    def tinhTongDienTich(self):
        sum = 0
        for hh in self.dshh:
            sum += hh.dienTich
        return f"Tong dien tich cac hinh la {sum}"
    
    def timViTriCuaHinh(self, h: HinhHoc):
        for hh in self.dshh:
            if(isinstance(hh, h) and hh.canh == h.canh):
                return hh
            
    def timHinhTheoDienTich(self, s: float):
        return [hh for hh in self.dshh if(hh.dienTich == s)]
    
    def xoa(self, hh: HinhHoc):
        self.dshh.remove(hh)
        
    def sapxep(self, t: bool):
        for hh in self.dshh:
            return sorted(self.dshh,key=str(type(hh).__name__), reverse=t)
            
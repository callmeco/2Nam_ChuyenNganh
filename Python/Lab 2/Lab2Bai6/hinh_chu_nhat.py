from hinh_hoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, chieuDai: float, chieuRong: float) -> None:
        self._chieuDai = chieuDai
        self._chieuRong = chieuRong
        
    def HinhChuNhat(self, dai: float, rong: float):
        pass

    def tinhDienTich(self) -> float:
        return self._chieuDai * self._chieuRong
    
    def xuat(self):
        print(f"Dien tich hinh chu nhat la: {self.tinhDienTich()}")
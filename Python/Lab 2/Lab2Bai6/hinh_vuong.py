from hinh_chu_nhat import HinhChuNhat

class HinhVuong(HinhChuNhat):
    def __init__(self, canh: float) -> None:
        super().__init__(canh)
    
    def HinhVuong(self, canh: float):
        pass

    def tinhDienTich(self) -> float:
        return super().tinhDienTich()
    
    def xuat(self):
        print(f"Hinh vuong co dien tich: {self.tinhDienTich()}")
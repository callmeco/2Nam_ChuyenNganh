from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien import SinhVien
from sv_phi_chinh_quy import SinhVienPhiCQ
from datetime import datetime

class DanhSachSinhVien:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timSVTheoMs(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ms:
                return i
        else:
            return -1
    
    def timSvTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]
    
    # tìm sinh viên có điểm rèn luyện từ 80 trở lên
    @staticmethod
    def kiemTraSvDRL80(sv: SinhVien):
        if not isinstance(sv, SinhVienChinhQuy):
            return False
        if sv.DiemRL >= 80:
            return True
        return False
    
    def timSvDRL80(self):
        return [sv for sv in self.dssv if self.kiemTraSvDRL80(sv)]
    
    #tìm sinh viên có trình độ cao đẳng sinh trước ngày 15/8/1999
    @staticmethod
    def kiemTraTDSvNgaySinh(sv: SinhVien):
        if not isinstance(sv, SinhVienPhiCQ):
            return False
        if sv.TrinhDo.lower() == "Cao đẳng".lower() and sv.ngaySinh < datetime.strptime("15/8/1999", "%d/%m/%Y"):
            return True
        return False
    
    def timSvTDNgaySinh(self):
        return [sv for sv in self.dssv if self.kiemTraTDSvNgaySinh(sv)]
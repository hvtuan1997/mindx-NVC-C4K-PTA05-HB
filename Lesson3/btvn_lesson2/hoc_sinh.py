class HocSinh:
    # ham khoi tao
    def __init__(self, ma=None, ten=None, toan=None, ly=None, hoa=None):
        self.ma_hs = ma
        self.ten_hs = ten
        self.diem_toan = toan
        self.diem_ly = ly
        self.diem_hoa = hoa
        if (toan == None) and (ly == None) and (hoa == None):
            self.diem_TB = 0
        else:
            self.diemTB = (self.diem_toan + self.diem_ly + self.diem_hoa) / 3

    # ham tinh diem trung binh cua 1 hoc sinh
    def tinh_DTB(self):
        return (self.diem_toan + self.diem_ly + self.diem_hoa) / 3

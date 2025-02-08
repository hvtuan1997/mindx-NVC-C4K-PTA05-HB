from hinh_tron import HinhTron


class HinhTru(HinhTron):
    # ham khoi tao
    def __init__(self, ban_kinh=None, chieu_cao=None):
        super().__init__(ban_kinh)
        self.H = chieu_cao

    # ham tinh the tich
    def tinh_the_tich(self):
        return super().tinh_DT() * self.H

    # ham tinh dien tich toan phan
    def tinh_dien_tich_TP(self):
        return super().tinh_CV() * (super().R + self.H)

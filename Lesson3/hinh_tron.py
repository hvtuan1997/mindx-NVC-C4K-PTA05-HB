import math


class HinhTron:
    # ham khoi tao
    def __init__(self, ban_kinh=None):
        self.R = ban_kinh

    # tinh chu vi
    def tinh_CV(self):
        return 2 * math.pi * self.R

    # ham tinh dien tich
    def tinh_DT(self):
        return math.pi*self.R*self.R

# khai bao thu vien
import math


# khai bao lop
class HinhTron:
    # ham khoi tao - contructor
    def __init__(self, bk=None):
        self.__ban_kinh = bk  # ban kinh la thuoc tinh duoc bao ve - private

    # ham tinh chu vi
    def Tinh_chu_vi(self):
        return 2 * math.pi * self.__ban_kinh

    # ham setter
    def Set_ban_kinh(self, bk=None):
        self.__ban_kinh = bk

    # ham getter
    def Get_ban_kinh(self):
        return self.__ban_kinh


# ===chuong trinh chinh===
if __name__ == "__main__":
    # khai bao doi tuong
    ht1 = HinhTron()

    ht1.Set_ban_kinh(float(input("Nhap vao ban kinh: ")))

    print("Ban kinh la:", ht1.Get_ban_kinh())

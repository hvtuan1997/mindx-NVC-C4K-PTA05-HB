# khai thu vien
import math

# khai bao lop
class HinhTron:
    # thuoc tinh
    ban_kinh = 0.0

    # phuong thuc
    def __init__(self): # ham khoi tao
        self.ban_kinh = 3.4
    
    def Tinh_dien_tich(self):
        return math.pi * self.ban_kinh * self.ban_kinh
    
    def Tinh_chu_vi(self):
        return 2 * math.pi * self.ban_kinh

# ===chuong trinh chinh===
if __name__ == "__main__":
    # khai bao doi tuong
    ht1 = HinhTron()
    ht2 = HinhTron()

    # gan gia tri cu the cho doi tuong ht1
    # ht1.ban_kinh = float(input("Nhap ban kinh: "))

    # hien thi
    print("Ban kinh cua ht1 la:", ht1.ban_kinh)
    print("Chu vi cua ht1 la:", ht1.Tinh_chu_vi())

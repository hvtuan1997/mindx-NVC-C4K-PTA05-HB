"""
Đề bài:
Xây dựng lớp NhanVien là lớp mô tả cho các
đối tượng nhân viên trong một công ty.
Biết mỗi nhân viên đều có:
- Họ và tên.
- Địa chỉ.
- Hệ số lương.
Hãy lập trình các phương thức cho lớp NhanVien:
- Khởi tạo để sinh ra nhân viên với tên,
địa chỉ, hệ số lương được cung cấp.
- Cập nhật địa chỉ khi nhân viên chuyển nhà.
- Cập nhật hệ số lương khi nhân viên có
kỳ xét tăng lương.
- Xuất ra thông tin của nhân viên.
"""


# khai bao lop
class NhanVien:
    # ham khoi tao
    def __init__(self, ho_ten, dia_chi, he_so_luong):
        self.ho_ten = ho_ten
        self.dia_chi = dia_chi
        self.he_so_luong = he_so_luong

    # ham cap nhat dia chi
    def update_dia_chi(self, dia_chi_moi):
        self.dia_chi = dia_chi_moi

    # ham cap nhat he so luong
    def update_he_so_luong(self, he_so_luong_moi):
        self.he_so_luong = he_so_luong_moi

    # ham hien thi thong tin
    def hien_thi_thong_tin(self):
        print("Thong tin nhan vien:")
        print("\tHo va ten: " + self.ho_ten)
        print("\tDia chi: " + self.dia_chi)
        print("\tHe so luong: " + str(self.he_so_luong))


# chuong trinh chinh
if __name__ == "__main__":
    nv1 = NhanVien("Minh Quan", "Hung Yen", 1.4)
    nv1.hien_thi_thong_tin()

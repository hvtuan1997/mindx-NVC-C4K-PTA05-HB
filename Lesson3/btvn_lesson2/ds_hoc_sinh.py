from hoc_sinh import HocSinh

# ===chuong trinh chinh===
if __name__ == "__main__":
    ds = []

    # tao cac hoc sinh
    hs1 = HocSinh(1, "Trung", 7, 8, 9)
    hs2 = HocSinh(2, "Quan", 8, 9, 10)
    hs3 = HocSinh(3, "The Anh", 9, 6, 7)

    # bo sung hoc sinh vao danh sach
    ds.append(hs1)
    ds.append(hs2)
    ds.append(hs3)

    # tim max
    max_tb = hs1.tinh_DTB()
    hs_max = HocSinh()
    for i in range(1, len(ds)):
        if max_tb < ds[i].diem_TB:
            max_tb = ds[i].diem_TB
            hs_max = ds[i]

    # hien thi ket qua
    print("Hoc sinh co diem trung binh lon nhat la:")
    print("\tMa: " + str(hs_max.ma_hs))
    print("\tTen: " + hs_max.ten_hs)
    print("\tDiem TB: " + str(hs_max.diemTB))

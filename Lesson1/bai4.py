# ham tinh tong cac so le
def tinh_tong_le(A):
    tong = 0
    for i in A:
        if (i % 2) != 0:
            tong += i
    return tong


# nhap du lieu
n = int(input("Nhap vao so luong phan tu n = "))
print("Nhap vao cac gia tri phan tu cho mang:")
A = []
for i in range(n):
    x = int(input("\tPhan tu thu " + str(i + 1) + " la: "))
    A.append(x)

# hien thi mang
print("Mang vua nhap la: " + str(A))

# hien thi tong
print("Tong cac so le trong A la: " + str(tinh_tong_le(A)))

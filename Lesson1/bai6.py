# ham tim uoc chung lon nhat cua 2 so
def tim_uscln(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


# nhap du lieu
a = int(input("Nhap vao so thu nhat: "))
b = int(input("Nhap vao so thu hai: "))
c = int(input("Nhap vao so thu ba: "))

# hien thi ket qua
print("Uoc chung lon nhat cua 3 so tren la: " + str(tim_uscln(tim_uscln(a, b), c)))

# ham tim uoc chung lon nhat cua 2 so nguyen duong
def tim_uscln(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


# nhap du lieu
s = input("Nhap phan so: ")

# hien thi
print("Phan so ban dau la: " + s)

# phan tach thanh tu va mau
tu_so = int(s.split("/")[0])
mau_so = int(s.split("/")[1])

# rut gon
uoc_chung_lon_nhat = tim_uscln(tu_so, mau_so)
tu_so = tu_so / uoc_chung_lon_nhat
mau_so = mau_so / uoc_chung_lon_nhat

# hien thi phan dang rut gon
print("Phan so sau khi rut gon la: " + str(tu_so) + "/" + str(mau_so))

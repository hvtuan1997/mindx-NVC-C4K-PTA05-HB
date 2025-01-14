# ham kiem tra so hoan hao
def kt_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False


# nhap so n
n = int(input("Nhap so can kiem tra n = "))

# kiem tra hoan hao
if kt_hoan_hao(n) == True:
    print("n la so hoan hao. Cac uoc thuc su la:")
    for i in range(1, n):
        if (n % i) == 0:
            print(i, end="\t")
else:
    print("n khong phai la so hoan hao!")

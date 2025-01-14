# ham kiem tra so nguyen to
def kt_nguyen_to(n):
    kt = True
    if n < 2:
        kt = False
    elif n == 2:
        kt = True
    elif (n % 2) == 0:
        kt = False
    else:
        for i in range(3, n, 2):
            if (n % i) == 0:
                kt = False
    return kt


s = ""
n = 2
while n <= 1000:
    for i in range(2, n):
        if (n % i) == 0 and (n % (i * i)) == 0:
            if kt_nguyen_to(i) == True:
                s += str(n) + "\t"
                break
    n += 1
print(s)

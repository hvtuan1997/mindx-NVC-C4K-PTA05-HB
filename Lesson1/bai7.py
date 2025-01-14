# ham kiem tra n co trong day fibonacci
def is_fibonacci(n):
    a, b = 1, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False


# nhap du lieu
n = int(input("Nhap vao so nguyen n = "))

# kiem tra
if is_fibonacci(n) == True:
    print("So n trong day Fibonacci!")
else:
    print("So n khong trong day Fibonacci!")

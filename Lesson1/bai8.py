# ham nhap mang
def nhap_mang(A, n):
    for i in range(n):
        x = int(input("\tPhan thu thu " + str(i + 1) + " la: "))
        A.append(x)


# ham hien thi mang
def hien_thi_mang(A):
    for i in A:
        print(str(i), end="\t")


# ham tim max trong mang
def tim_max(A):
    _max = A[0]
    for i in range(1, len(A)):
        if _max < A[i]:
            _max = A[i]
    return _max


# ham sap xep tang dan
def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


# nhap du lieu
n = int(input("Nhap vao so luong phan tu n = "))
print("Nhap vao cac phan tu trong mang:")
A = []
nhap_mang(A, n)

# hien thi mang
print("Mang vua nhap la:")
hien_thi_mang(A)

# hien thi ket qua
print("\nPhan tu lon nhat trong mang la: " + str(tim_max(A)))

print("Mang sau khi sap xep tang dan la:")
bubbleSort(A)
hien_thi_mang(A)

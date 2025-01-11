import math

# doc du lieu tu tep
f1 = open("ROOT.INP", "r")

# doc du lieu tu tep
a = int(f1.readline())
b = int(f1.readline())
c = int(f1.readline())

# tinh gia tri bieu thuc
S = (a*a+b*b+c*c)/(a*b*c) + math.sqrt(a*b*c)

# ghi vao tep dau ra
f2 = open("ROOT.OUT", "w")
f2.write(str(S))

# dong file
f1.close()
f2.close()

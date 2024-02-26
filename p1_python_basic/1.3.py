import math

def giai_phuong_trinh_bac_2(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x, x
    else:
        return "The equation has no real root."

a = int(input())
b = int(input())
c = int(input())

ket_qua = giai_phuong_trinh_bac_2(a, b, c)

if type(ket_qua) == tuple:
    x1, x2 = ket_qua
    if (x1 > x2):
        x1, x2 = x2, x1
    print("{0:.2f} {1:.2f}".format(x1, x2))
else:
    print(ket_qua)
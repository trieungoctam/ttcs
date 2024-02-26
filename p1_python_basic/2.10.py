from math import gcd

a = int(input())
b = int(input())

_gcd = gcd(a, b)
_lcm = a * b // _gcd

def snt(i):
    if i < 2:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

for i in range(1, _gcd + 1):
    if a % i == 0 and b % i == 0:
        if i != 1 and snt(i) == False:
            continue
        print(i, end=" ")
print()
print(_gcd)
print(_lcm)
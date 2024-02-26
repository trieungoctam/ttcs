n = int(input())

s1 = 1
s2 = 1
s3 = 1

check = True

for i in range(2, n):
    s1 += i
    s2 *= i
    s3 += 1/i
    if n % i == 0 :
        check = False

print(s1)
print(s2)
print("{0:.2f}".format(s3))

if check:
    print("Prime")
else:
    print("Not a prime")
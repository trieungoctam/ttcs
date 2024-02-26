n = int(input())
m = int(input())

for i in range(n, m + 1):
    j = str(i)
    if j == j[::-1]:
        print(j)
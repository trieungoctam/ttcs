a = int(input())

def recur(a):
    if a == 1:
        return 1
    else:
        return a + recur(a - 1)

print(recur(a))
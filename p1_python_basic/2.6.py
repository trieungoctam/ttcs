def chia(x,y):
    if (y == 0):
        return "Cannot divide by 0.\nNone"
    return x/y

x = int(input().strip())
y = int(input().strip())

print(chia(x,y))
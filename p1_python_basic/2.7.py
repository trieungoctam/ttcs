def check(x):
    x1 = x[::-1]
    if x1 == x:
        return True
    else:
        return False

print(check(input()))
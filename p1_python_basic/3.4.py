a = input()
b = input()
n1 = (len(a) - 4) // 2
a1 = a[n1: -n1]
n2 = (len(b) - 4) // 2
a2 = b[n2 : -n2]
print("1.",a1, a2)
print("2.",a[:len(a) // 2] + b + a[len(a)//2:])
print("3.", a[0] + b[0] + a[-1] + b[-1])


lowercase = ""
uppercase = ""
numbers = ""
symbols = ""

for char in a:
    if char.islower():
        lowercase += char
    elif char.isupper():
        uppercase += char
    elif char.isdigit():
        numbers += char
    else:
        symbols += char

a1 = lowercase + uppercase + numbers + symbols

lowercase = ""
uppercase = ""
numbers = ""
symbols = ""

for char in b:
    if char.islower():
        lowercase += char
    elif char.isupper():
        uppercase += char
    elif char.isdigit():
        numbers += char
    else:
        symbols += char

a2 = lowercase + uppercase + numbers + symbols

print("4." , a1, a2)

lowercase = 0
numbers = 0
symbols = 0

for char in a:
    if char.islower():
        lowercase += 1
    elif char.isupper():
        lowercase += 1
    elif char.isdigit():
        numbers += 1
    else:
        symbols += 1


print("5.", lowercase, numbers, symbols, end=" ")

lowercase = 0
numbers = 0
symbols = 0

for char in b:
    if char.islower():
        lowercase += 1
    elif char.isupper():
        lowercase += 1
    elif char.isdigit():
        numbers += 1
    else:
        symbols += 1

print(lowercase, numbers, symbols, end=" ")
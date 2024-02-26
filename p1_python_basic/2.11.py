n = input()

if (n.isdigit() == False and n[0] != '-') :
    print("Error: not a number")
elif (int(n) < 0) :
    print("Error: negative number")
else :
    print("{0:b}".format(int(n)))

    s = 0
    for i in n:
        s += int(i)
    print(s)

    n = int(n[::-1])

    print(n)
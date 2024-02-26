n = input()
dg = ""
for i in n:
    if i.isdigit():
        dg += i
print("1.", dg)
nsym = ""
for i in n:
    if i.isalpha() or i.isdigit() or i == ' ':
        nsym += i
print("2.", nsym)

n = n.split('-')
n = ''.join(n)
print('3.', n)
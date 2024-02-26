n = 6
ar = []
for i in range(n):
    ar.append(int(input()))

for i in ar[::-1]:
    print(i, end=" ")
print()
for i in ar :
    if (i > 150):
        continue
    if (i > 600):
        break
    if i % 5 == 0:
        print(i, end=" ")       
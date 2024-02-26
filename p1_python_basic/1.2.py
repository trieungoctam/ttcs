import math

PI = math.pi

radius = float(input())

cv = 2 * PI * radius

dt = PI * ( radius ** 2 )

print("{0:.2f} {1:.2f}".format(dt, cv))
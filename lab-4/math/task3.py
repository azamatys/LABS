import math

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

if sides > 2 and length > 0:
    S = (sides * length**2) / (4 * math.tan(math.pi / sides))
    print("The area of the polygon is:", round(S, 1))
else:
    print("error")
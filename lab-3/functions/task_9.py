from math import pi
def VolSphere(radius):
    return 4/3*pi*radius**3

radius = int(input())
print(VolSphere(radius))
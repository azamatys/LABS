# n = int(input())
# for i in range(1, n+1):
#     print(i**2)


def Squares(n):
    for i in range(1, n+1):
        yield i**2
    
n = int(input("squares of numbers up to: "))

for i in Squares(n):
    print(i, end = " ")
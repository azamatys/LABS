from functools import reduce

def multiply_list(numbers):
    res = reduce(lambda x, y: x * y, numbers)
    return res

numbers = [int(x) for x in input().split()]

res = multiply_list(numbers)
print("Multiplication of all numbers in the list: ", res)
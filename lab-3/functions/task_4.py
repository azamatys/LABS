from math import sqrt

def filter_prime(mylist):

    def IsPrime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    return [x for x in mylist if IsPrime(x)]

mylist = [int(x) for x in input().split()]
prime_Numbers = filter_prime(mylist)
print(prime_Numbers)
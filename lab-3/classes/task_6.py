def func():
    lis = [int(x) for x in input().split()]

    is_prime = lambda num: all(num%i!=0 for i in range(2, num)) and num > 1
    
    listik = filter(is_prime, lis)
    print(*listik)
func()
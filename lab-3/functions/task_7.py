def has_33(mylist):
    for i in range(1, len(mylist)):
        if mylist[i] == 3 and mylist[i-1] == 3:
            return True
    return False

mylist = [int(x) for x in input().split()]
print(has_33(mylist))
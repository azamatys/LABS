def spy_game(mylist):
    cnt = 0
    for x in mylist:
        if x == 0 and cnt == 0:
            cnt+=1
        elif x == 0 and cnt == 1:
            cnt+=1
        elif x == 7 and cnt == 2:
            return True
    return False

mylist = [int(x) for x in input().split()]
print(spy_game(mylist))


# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
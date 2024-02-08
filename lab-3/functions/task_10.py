def Unique(mylist):
    newlist = []
    for i in range(len(mylist)):
        isUnique = True
        for j in range(i+1, len(mylist)):
            if mylist[i] == mylist[j]:
                isUnique = False
                break
        if isUnique:
            newlist.append(mylist[i])

    print(newlist)

mylist = [int(x) for x in input().split()]
Unique(mylist)
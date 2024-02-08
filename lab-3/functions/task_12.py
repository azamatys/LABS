def histogram(mylist):
    for x in mylist:
        print(x*"*")

mylist = [int(x) for x in input().split()]
histogram(mylist)
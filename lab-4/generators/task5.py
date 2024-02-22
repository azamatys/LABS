def N_to_Zero(n):
    i = n
    while(i>=0):
        yield i
        i-=1

n = int(input())

for i in N_to_Zero(n):
    print(i, end=" ")
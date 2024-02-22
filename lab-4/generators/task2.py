def Even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())

for i in Even(n):
    print(i, end = " ")


# Even = [x for x in range(int(input())+1) if x%2==0]

# for i in Even:
#     print(i, end = " ")
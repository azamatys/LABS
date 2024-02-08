from itertools import permutations

def perm(soz):
    sozder = permutations(soz)
    for i in sozder:
        print("".join(i))

soz = input()
perm(soz)
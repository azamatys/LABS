def solve(numheads, numlegs):
    rabbits = int((numlegs - 2*numheads)/2)
    chickens = int((numheads - rabbits))
    print("Rabbits:", rabbits)
    print("Chickens:", chickens)

numheads = int(input("Num heads: "))
numlegs = int(input("Num legs: "))
solve(numheads, numlegs)
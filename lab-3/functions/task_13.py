import random

def GuessTheNumber():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    r = random.randrange(1, 20)
    cnt = 0

    print("Take a guess.")
    num = int(input())
    cnt+=1
    
    while num != r:
        print("Take a guess.")
        num = int(input())
        cnt+=1
        if num < r:
            print("Your guess is too low.")
        elif num == r:
            break
        elif num > r:
            print("Your guess is too high.")
    print(f"Good job, {name}! You guessed my number in {cnt} guesses!")

GuessTheNumber()
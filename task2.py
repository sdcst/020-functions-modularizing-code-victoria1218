"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""


def title():
    print("choose a random number between 1 and 100,guess the number in 10 turns")
title()
def game():
    x = 64
    c = 0 
    y = int(input("enter a number"))
    while x != y:
        if x < y :
            print("over")
            y = int(input("enter a number"))
            c += 1 
        else:
            print("under")
            y = int(input("enter a number"))
            c += 1
        if c == 10:
            print("You are out of chance!")
            break
    if x == y:
        print("You got it!")
game()

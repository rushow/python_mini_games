# Random Number Guessing Game
# Moman Khan

from curses.ascii import isdigit
from operator import truediv
import random


flag = True

while flag:
    num = input('Type a Number for the uppoer bound:  ')

    if num.isdigit():
        print("Let's Play!!")
        num = int(num)
        flag = False
    else:
        print('Invalid Input! Try Again!!')

secret = random.randint(1, num)
guess = None
count = 1

while guess != secret:
    guess = input("Type a number between 1 and " + str(num) + ":  ")

    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print("You got it!!")
    else:
        print("Please Try Again!")
        count += 1

print("It took you", count, "guesses!!")


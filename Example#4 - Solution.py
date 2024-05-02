# Example 4 - Guessing Game - Correct Solution
"""
import random

generate random num between 1 to 100 

ask user for a guess 
while guess is not correct:
  if guess is too hight
    print too high
  else:
    print too low.
ask user for a guess again

print congratualations
"""

import random

num = random.randrange(1,101)

guess = int(input("Enter a guess: "))

while guess != num:
    if guess > num:
        print("Guess is too high guess again!")
    else:
        print("Guess is too low guess again!")

    guess = int(input("Enter a guess: "))

print("Congratulations! you guessed correctly.")


# Example 4 - Guessing Game - Infinite Loop

my_num = 34

guess = int(input("Enter guess: "))

while guess != my_num:
  guess = int(input("Enter guess: "))
  print("Sorry, wrong number")
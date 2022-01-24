#This game lets you guess the number between 0 and the number initilized at the begenning
#Can you guess the random number
import random


def GuessNumber(number):
  random_number = random.randint(0, number)
  guess = 0
  while guess != random_number:
    guess = int(input(f"Guess a random number between 0 and {number} "))
    if guess < random_number:
      print("Sorry guess again. Too low ")
    elif guess > random_number:
      print("Sorry too high. Guess again! ")
  else:
      print(f"You guessed the crrect number which is: {random_number}")          

User_Number = int(input("Up to what number do you want to guess? >> "))
GuessNumber(User_Number)
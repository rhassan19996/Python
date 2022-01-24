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


def computerGuess(number):
  low = 1
  high = number
  feedback = ""
  while feedback != "c":
    if low!=high:
      guess = random.randint(low, high)
    else:
      guess = low 
    feedback = input(f"is {guess} too high (h) too low(l) or correct (c)? ").lower()
    if feedback == "h":
      high = guess -1
    if feedback == "l":
      low = guess + 1
  print(f"Yay the computer guessed the number, {guess} correctly! ")  
        
  
    
User_Number = int(input("Up to what number do you want to guess? >> "))
#GuessNumber(User_Number)

computerGuess(User_Number)
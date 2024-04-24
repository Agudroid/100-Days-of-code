#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint
from replit import clear

def game(random_number, attempts):
  is_correct = False
  while attempts > 0 and not is_correct:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == random_number:
      print(f"You got it! The answer was {random_number}.")
      is_correct = True
    elif guess > random_number:
      print("Too high.")
      attempts -= 1
    else:
      print("Too low")
      attempts -= 1
    
    if attempts == 0:
      print("You've run out of guesses, you lose.")

def main():
  random_number = randint(1, 100)
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  print(f"Psst the random number is {random_number}")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    attempts = 10
  else:
    attempts = 5


  game(random_number, attempts)
  start_over = input("Do you want to start over? Type 'y' or 'n': ") == "y"
  if start_over:
    clear()
    main()


if __name__ == "__main__":
  main()
  
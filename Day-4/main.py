rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to Rock, Paper, Scissors!")
print("What do you choose?")
user_choice = input("Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

if user_choice == "0":
  print(rock)
elif user_choice == "1":
  print(paper)
else:
  print(scissors)

game_list = [rock, paper, scissors]
print("Computer chose:")
computer_choice = random.randint(0,2)

print(game_list[computer_choice])
if int(user_choice) == computer_choice:
  print("It's a draw!")
if int(user_choice) == 0 and computer_choice == 1:
  print("You lose!")
if (int(user_choice) == 0 and computer_choice == 2):
  print("You win!!")
if (int(user_choice) == 1 and computer_choice == 0):
  print("You win!!")
if int(user_choice == 1) and computer_choice == 2:
  print("You lose!")
if int(user_choice) == 2 and computer_choice == 0:
  print("You lose!")
if int(user_choice) == 2 and computer_choice == 1:
  print("You win!!")
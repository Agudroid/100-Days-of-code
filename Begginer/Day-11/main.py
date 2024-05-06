from replit import clear
from art import logo
from random import randint

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []

def give_cards():
  if len(user_cards) == 0:
    user_cards.append(cards[randint(0,len(cards)-1)])
    for i in range(2):
      computer_cards.append(cards[randint(0,len(cards)-1)])

  user_cards.append(cards[randint(0,len(cards)-1)])

def calculate_score(card_list):
  score = 0
  for card in card_list:
    score += card

  if score > 21 and 11 in card_list:
    index = card_list.index(11)
    card_list[index] = 1
    score -= 10
    
  return score

def new_game():
  question = input('Do you want to play a game of Blackjack? Type "y" or "n": ')
  return question == 'y'

def result(user_score, computer_score):
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  if computer_score < user_score and user_score <= 21:
    print("You win!")
  elif computer_score == user_score:
    print("It´s a draw")
  else:
    print("You lose")

  user_cards.clear()
  computer_cards.clear()
  main()
  
def blackjack():
  give_cards()
  user_score = calculate_score(user_cards)
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Computer's first card: {computer_cards[0]}")
  if user_score > 21:
    computer_score = calculate_score(computer_cards)
    result(user_score, computer_score)
    print("You went over. You lose 😭")
  else:
    continue_game = input(f"Type 'y' to get another card, type 'n' to pass: ")
    if continue_game == 'y':
      blackjack()
    else:
      computer_score = calculate_score(computer_cards)
      result(user_score, computer_score)
  
def main():
  start_game = new_game()
  if start_game:
    clear()
    print(logo)
    blackjack()

main()
    
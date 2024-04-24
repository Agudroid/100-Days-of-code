from art import logo, vs
from random import randint
from game_data import data
from replit import clear

def calculate_answer(a, b):
  if a['follower_count'] >= b['follower_count']:
    return 'A'
  else:
    return 'B'

def main():
  is_lose = False
  score = 0
  
  while not is_lose:
    print(logo)
    random_a = randint(0,len(data)-1)
    random_b = randint(0,len(data)-1)
    character_a = data[random_a]
    character_b = data[random_b]
    if score > 0:
      print(f"Current score: {score}")
    
    print(f"""Compare A: {character_a['name']}, 
    a {character_a['description']},from {character_a['country']}""")

    print(vs)

    print(f"""Compare B: {character_b['name']}, 
    a {character_b['description']},from {character_b['country']}""")

    answer = calculate_answer(character_a, character_b)
    guess = input('Who has more followers Type "A" or "B": ')

    if answer == guess:
      score += 1
    else:
      is_lose = True
    clear()

  print(logo)
  print(f"Sorry, that´s wrong. Final score: {score}")

main()
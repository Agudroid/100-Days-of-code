from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

list_of_people = []
is_over = False

def add_new_person(name, bid):
  person = {
    "name" : name,
    "bid": bid
  }
  list_of_people.append(person)

def find_highest_bidder(list_of_people):
  max_bid = 0
  winner = {}
  for person in list_of_people:
    if person["bid"] > max_bid:
      winner = person
  return winner


print(logo)
while not is_over:
  name = input('What is your name?: ')
  bid = int(input('What is your bid?: $'))
  add_new_person(name, bid)
  answer = input('Are there any other bidders? Type "yes" or "no".\n')
  print(answer)
  if answer == 'no':
    is_over = True
  else:
    clear()

winner = find_highest_bidder(list_of_people)
print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")

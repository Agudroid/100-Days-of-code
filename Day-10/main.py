from art import logo
from replit import clear



def add(a,b):
  return a + b

def substract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a/b


is_exit = False
operators = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}
result = None

print(logo)
while not is_exit:
  if result is None:
    result = int(input("What's the first number? \n"))
  input2 = int(input("What's the second number? \n"))
  for key in operators:
    print(key)
  function = operators[input("Select your operation. \n")]
  result = function(result,input2)
  print()
  is_exit = input("do you wanna continue? \n").lower() != "yes"
  clear()
  
  


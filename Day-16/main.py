from menu import Menu
from coffemaker import CoffeeMaker
from moneymachine import MoneyMachine


def create_report(coffee, money):
    print(coffee.report())
    print(money.report())

def insert_money():
    quarter = int(input("Number of quarters: "))
    dimes = int(input("Number of dimes: "))
    nickles = int(input("Number of nickles: "))
    pennies = int(input("Number of pennies: "))
    money_machine.process_coins(quarter, dimes, nickles, pennies)


if __name__ == "__main__":
    machine_menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    is_on = True
    while is_on:
        instruction = input(f"What would you like ? ({machine_menu.get_items()}): ")
        if instruction == "off":
            is_on = False
        elif instruction == "report":
            create_report(coffee_maker, money_machine)
        else:
            drink = machine_menu.find_drink(instruction)
            if coffee_maker.is_resource_enough(drink):
                insert_money()
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                    print(f"Your change is: {money_machine.change}")
                else:
                    print("Not enough money")


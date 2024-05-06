class MoneyMachine:

    money = 0
    money_inserted = 0
    change = 0

    def report(self):
        print(f"Money: ${self.money}")

    def make_payment(self, cost):
        if cost < self.money_inserted:
            self.change = round(self.money_inserted - cost, 2)
            self.money += cost
            return True
        return False

    def process_coins(self, quarters, dimes, nickles, pennies):
        self.money_inserted = quarters * 0.5 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    def reset_money(self):
        self.money_inserted = 0
        self.change = 0

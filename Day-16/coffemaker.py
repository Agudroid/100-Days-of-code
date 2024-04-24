from menuitem import MenuItem


class CoffeeMaker:

    resources = {
        'water': 300,
        'milk': 200,
        'coffee': 100
    }

    def is_resource_enough(self, drink: MenuItem):
        for key in drink.ingredients.keys():
            if self.resources[key] < drink.ingredients[key]:
                print(f"Sorry there is not enough {str(key).capitalize()}")
                return False

        return True

    def make_coffee(self, order: MenuItem):
        for key in order.ingredients.keys():
            self.resources[key] -= order.ingredients[key]

    def report(self):
        report = ""
        for key in self.resources.keys():
            report += f"{key.capitalize()}: {self.resources[key]}"
            if key == "Coffee":
                report += "g"
            else:
                report += "ml"
            report += "\n"
        return report

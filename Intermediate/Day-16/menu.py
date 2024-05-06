from menuitem import MenuItem


class Menu:

    items_list = []

    def __init__(self):
        espresso = MenuItem("espresso", 1.5, {'water': 50, 'coffee': 18})
        latte = MenuItem("latte", 2.5, {'water': 200, 'milk': 150, 'coffee': 24})
        cappuccino = MenuItem("cappuccino", 3, {'water': 250, 'milk':100, 'coffee': 24})
        self.items_list.append(espresso)
        self.items_list.append(latte)
        self.items_list.append(cappuccino)

    def get_items(self):
        items_name = ""
        for i in self.items_list:
            items_name += i.name
            items_name += "/"

        items_name.rstrip()

        return items_name

    def find_drink(self, order_name):
        for i in self.items_list:
            if i.name == order_name:
                return i
        return None

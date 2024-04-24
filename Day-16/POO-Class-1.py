from turtle import Turtle, Screen
from prettytable import PrettyTable


# turtle_blueprint = Turtle()
# turtle_blueprint.shape("turtle")
# turtle_blueprint.color("green")
# turtle_blueprint.forward(100)
#
# my_screen = Screen()
#
# # Create Screen
# print(my_screen.canvwidth)
# my_screen.exitonclick()

pokemon_list = ['Pikachu', 'Squirtle', 'Bulbasaur', 'Charmander']
type_list = ['Electric', 'Water', "Grass", "Fire"]

table = PrettyTable()
table.add_column("Pokemon Name", pokemon_list)
table.add_column("Type", type_list)
table.align = "l"
print(table)

number_list = [1, 2, 3, 4, 5]

# To do a comprehension list the syntax is:
number2_list = [n * 2 for n in number_list]
print(number2_list)

number3_list = [n * 2 for n in range(1, 5)]
print(number3_list)

# You can add a condition if you want
a = 'x'

names_list = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
names_condition_list = [name.upper() for name in names_list if len(name) > 4]
print(names_condition_list)

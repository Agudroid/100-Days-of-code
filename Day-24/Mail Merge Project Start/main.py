if __name__ == '__main__':
    with open('Input/Letters/starting_letter.txt', mode='r') as file:
        letter = file.read()
        file.close()
    print(letter)

    with open('Input/Names/invited_names.txt') as file:
        name_string = file.read()
        file.close()

    print(name_string)
    name_list = name_string.split("\n")

    for name in name_list:
        letter = letter.replace("[name]", name)
        letter_name = f'Output/ReadyToSend/letter_for_{name}'
        with open(letter_name, 'w') as file:
            file.write(letter)
        file.close()

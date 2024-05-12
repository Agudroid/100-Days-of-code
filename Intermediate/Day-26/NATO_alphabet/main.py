import pandas as pd
from art import logo

def initialize_nato_dict():
    nato_data = pd.read_csv('nato_phonetic_alphabet.csv')

    nato_dict = {}
    for (index, row) in nato_data.iterrows():
        nato_dict[row.letter] = row.code

    return nato_dict


def convert_word():
    try:
        word = input('Enter a word (Type 0 to close): ').upper()
        nato_list = [nato[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the english alphabet')
        convert_word()
    else:
        print(nato_list)


if __name__ == '__main__':
    print(logo)
    nato = initialize_nato_dict()
    convert_word()


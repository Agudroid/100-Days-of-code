import pandas as pd


def initialize_nato_dict():
    nato_data = pd.read_csv('nato_phonetic_alphabet.csv')

    nato_dict = {}
    for (index, row) in nato_data.iterrows():
        nato_dict[row.letter] = row.code

    return nato_dict


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
if __name__ == '__main__':
    nato = initialize_nato_dict()
    word = input('Enter a word: ').upper()
    nato_list = [nato[letter] for letter in word]
    print(nato_list)

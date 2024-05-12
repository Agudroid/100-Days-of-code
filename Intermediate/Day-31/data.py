import pandas as pd
from random import choice


def load_flash_cards():
    fr_df = None
    try:
        fr_df = pd.read_csv('data/words_to_learn.csv')
    except FileNotFoundError:
        fr_df = pd.read_csv('data/french_words.csv')
    finally:
        return fr_df


class FlashCard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class FlashCardDeck:
    deck = []

    def __init__(self):
        cards_df = load_flash_cards()
        for (_, row) in cards_df.iterrows():
            card = FlashCard(row.French, row.English)
            self.deck.append(card)

    def show_all_cards(self):
        print(self.deck)

    def pick_card(self):
        return choice(self.deck)

    def remove_card(self, card):
        self.deck.remove(card)
        df = pd.DataFrame(vars(object_card) for object_card in self.deck)
        df.columns = ['French', 'English']
        print(df)
        df.to_csv('data/words_to_learn.csv')
        print('Word removed')

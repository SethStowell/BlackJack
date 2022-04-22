from random import random


class Deck(object):

    suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

    shortSuits = ['\u2663', '\u2660', '\u2665', '\u2666']

    names = ['King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'Ace']

    shortNames = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']

    hardValues = {"K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2,
                  "A": 1}

    softValues = {"K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2,
                  "A": 11}

    def __init__(self, deckType, size):
        self._cards = []
        self._deckType = deckType
        self._size = size

    def __str__(self):
        for card in self.cards:
            card.flip()
            string = f'{card}\n'
            card.flip()
        return string

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self):
        """Remove the top card from the deck (useful for dealing)"""
        card = self.cards[0]
        self.cards.remove(card)
        return card

    def get_cards(self):
        return self._cards

    cards = property(get_cards)

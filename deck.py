from random import random

class Deck(object):

    deck = []

    def __init__(self, card, suit, unit, deck):
        self.card = card

        with open('cardlist.txt') as CardList:
            for line in CardList:
                count = 0
                count += 1
                card = CardList[count]
                deck.append(card)

    def shuffle(self):
        random.deck()

    def pop(self, deck, card):
        deck.remove(card)



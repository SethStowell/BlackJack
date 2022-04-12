class Card(object):


    def __init__(self, card, suit, unit, hardValue, softValue):
        self.card = card
        self.suit = suit
        self.unit = unit
        self.hardValue = hardValue
        self.softValue = softValue

    def __str__(self):
        return f'{self.suit}{self.unit}'

    def flip(self):



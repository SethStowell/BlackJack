from deck import Deck

class Card(object):

    shortNames = {"Two of Hearts": "2-H", "Three of Hearts": "3-H", "Four of Hearts": "4-H", "Five of Hearts": "5-H",
                  "Six of Hearts": "6-H", "Seven of Hearts": "7-H", "Eight of Hearts": "8-H", "Nine of Hearts": "9-H",
                  "Ten of Hearts": "10-H", "Jack of Hearts": "J-H", "Queen of Hearts": "Q-H", "King of Hearts": "K-H",
                  "Ace of Hearts": "A-H", "Two of Diamonds": "2-D", "Three of Diamonds": "3-D", "Four of Diamonds": "4-D",
                  "Five of Diamonds": "5-D", "Six of Diamonds": "6-D", "Seven of Diamonds": "7-D", "Eight of Diamonds": "8-D",
                  "Nine of Diamonds": "9-D", "Ten of Diamonds": "10-D", "Jack of Diamonds": "J-D", "Queen of Diamonds": "Q-D",
                  "King of Diamonds": "K-D", "Ace of Diamonds": "A-D", "Two of Spades": "2-S", "Three of Spades": "3-S",
                  "Four of Spades": "4-S", "Five of Spades": "5-S", "Six of Spades": "6-S", "Seven of Spades": "7-S",
                  "Eight of Spades": "8-S", "Nine of Spades": "9-S", "Ten of Spades": "10-S", "Jack of Spades": "J-S",
                  "Queen of Spades": "Q-S", "King of Spades": "K-S", "Ace of Spades": "A-S","Two of Clubs": "2-C",
                  "Three of Clubs": "3-C", "Four of Clubs": "4-C", "Five of Clubs": "5-C", "Six of Clubs": "6-C",
                  "Seven of Clubs": "7-C", "Eight of Clubs": "8-C", "Nine of Clubs": "9-C", "Ten of Clubs": "10-C",
                  "Jack of Clubs": "J-C", "Queen of Clubs": "Q-C", "King of Clubs": "K-C", "Ace of Clubs": "A-C"}

    def __init__(self, card, suit, unit, hardValue, softValue):
        self.card = card
        self.hardValue = hardValue
        self.softValue = softValue

    def __str__(self):
        return f'{self.suit}{self.unit}'

    def flip(self):
        self.card.flip(self)



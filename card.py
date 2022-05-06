
class Card(object):

    fullNames = {"Two of Hearts": "2-H", "Three of Hearts": "3-H", "Four of Hearts": "4-H", "Five of Hearts": "5-H",
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

    names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    shortNames = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


    shortNameDict = dict(zip(names, shortNames))

    hardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    softValues = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    hardValueDict = dict(zip(names, hardValues))

    softValueDict = dict(zip(names, softValues))


    def __init__(self, name, shortName, suit, shortSuit, hardValue, softValue):
        self._name = name
        self._shortName = shortName
        self._suit = suit
        self._shortSuit = shortSuit
        self._hardValue = hardValue
        self._softValue = softValue
        self._isShowing = False

    def __str__(self):
        if self._isShowing:
            string = f'{self._name} of {self._suit} {self._shortSuit} {self._hardValue}'
        else:
            string = 'Card is face down'
        return string

    def get_hard_value(self):
        return self._hardValue

    def get_soft_value(self):
        return self._softValue

    def get_name(self):
        return self._name

    def get_short_name(self):
        return self._shortName

    def get_suit(self):
        return self._suit

    def get_short_suit(self):
        return self._shortSuit

    def get_visibility(self):
        return self._isShowing

    def pop(self):
        pass

    def flip(self):
        if self._isShowing == False:
            self._isShowing = True
        else:
            self._isShowing = False

    hardValue = property(get_hard_value)
    softValue = property(get_soft_value)
    name = property(get_name)
    shortName = property(get_short_name)
    suit = property(get_suit)
    shortSuit = property(get_short_suit)
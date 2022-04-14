from card import Card

class Hand(object):

    def __init__(self, bet):
        self._bet = bet
        self._isBusted = False
        self._isStanding = False
        self._isSplit = False
        self._isDoubled = False

    def __str__(self):
        pass

    def hard_value(self):
        value = 0
        for card in self:
            value += card.hardValue
        return value

    def soft_value(self):
        value = 0
        for card in self:
            value += card.softValue
        return value

    def get_value(self):
        return self.value

    def bet(self):
        pass

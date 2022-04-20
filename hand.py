from card import Card

class Hand(object):

    def __init__(self, bet):
        self._bet = bet
        self.isBusted = False
        self.isStanding = False
        self.isSplit = False
        self.isDoubled = False

    def __str__(self):
        pass

    def hard_value(self):
        """The hard value of an Ace = 1"""
        value = 0
        for card in self:
            value += card.hardValue
        return value

    def soft_value(self):
        """All cards have the same value, but Ace = 11"""
        value = 0
        for card in self:
            value += card.softValue
        return value

    def get_value(self):
        return self.value

    def hit(self, card):
        """Adds a card to a hand."""
        if self.can_hit():
            self.cards.append(card)
        else:
            raise CallError('Cannot hit a closed hand')

    def can_split(self):
        """Checks to see if a hand is able to split."""
        canSplit = False
        if len(self.cards) == 2 and self.cards[0].hardValue == self.cards[1].hardValue:
            canSplit = True
        return canSplit

    def split(self):
        """Splits a hand into two separate ones."""
        if self.can_split():
            card = self.cards.pop()
            self.isSplit = True
        else:
            raise CallError('Can only split 2 cards of the same value.')
        return card

    def stand(self):
        """Disables a hand from being played."""
        self.isDone = True

    def can_double(self):
        """Checks to see if a hand is able to double down."""
        canDouble = False
        if len(self.cards) == 2:
            canDouble = True
        return canDouble

    def double_down(self, card, bet):
        """Doubles down on a hand and hits one last time."""
        if self.can_double():
            self._bet += bet
            self.hit(card)
            self.isDoubled = True
        else:
            pass

    def is_blackjack(self):
        """Checks to see if a hand achieved blackjack"""
        isBlackjack = False
        if len(self.cards) == 2:
            if self.cards[0].shortName and self.cards[1].shortName in ['A', 'K', 'Q', 'J', '10']:
                if self.soft_value() == 21:
                    isBlackjack = True
        return isBlackjack

    def is_busted(self):
        """Checks to see if a hand is busted"""
        isBusted = False
        if self.hard_value() > 21:
            isBusted = True
        return isBusted

    def is_doubled(self):
        return self.isDoubled

    def is_split(self):
        return self.isSplit

    def get_bet(self):
        return self._bet

    bet = property(get_bet)




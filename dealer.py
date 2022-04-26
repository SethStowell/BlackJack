from deck import Deck
from hand import Hand

class Dealer(object):

    def __init__(self, name, money, table):
        self.name = name
        self.money = money
        self.table = table

    def __str__(self):
        pass

    def deal(self):
        for player in self.table.players():
            self.deck.pop()
            self.deck.pop()

    def shuffle(self):
        self.deck.shuffle()

    def pay_out(self, money):
        """Pay players after they win a hand"""
        #
        # Blackjack pays 3 to 2
        # ex: $10 bet + $15 winnings = $25 total
        #
        if self.hand.is_busted() == False and self.player.hand > self.dealer.hand:
            payout = True
            if payout == True:
                self.money = money - (self.player.hand.bet * 3/2)


    def rake_in(self, money):
        """Seize bets from all busted hands"""
        if self.hand.is_busted() == True:
            self.money = money + self.player.hand.bet

    def play(self):
        """Play round"""
        pass


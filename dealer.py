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

    def shuffle(self):
        self.deck.shuffle()

    def pay_out(self):
        """Pay players after they win a hand"""
        pass

    def rake_in(self):
        """Seize bets from all busted hands"""
        pass


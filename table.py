from deck import Deck
from hand import Hand
from card import Card
from player import Player
from dealer import Dealer
from toolbox import get_integer_between

class Table(object):

    def __init__(self):
        self._players = []
        self._dealer = Dealer('Lloyd', 1000, self)

    def __str__(self):
        return f'Table 1: Dealer {self._dealer} and {len(self._players)} player[s].'

    def manage_table(self):
        """Runs the blackjack program."""
        print("BLACKJACK!\n")
        numberOfPlayers = get_integer_between(1, 7, 'How many players will be participating?')
        #
        # Range from 1 to numberOfPlayers+1, so I don't ask for player 0's name
        #
        for number in range(1, numberOfPlayers+1):
            name = input(f"What is player {number}'s name? ")
            player = Player(name, 100, self)
            self._players.append(player)
        print('')
        self._dealer.take_bets()
        self._dealer.deck.shuffle()
        print('')
        while self._players:
            self._dealer.deal()
            self._dealer.play_hands()
            self._dealer.play_own()
            self._dealer.process_hands()
            self._dealer.cleanup()
            self._dealer.take_bets()
        print('Table is empty.')

    def add_player(self, player):
        self._players.append(player)

    def get_dealer(self):
        return self._dealer

    def get_players(self):
        return self._players

    players = property(get_players)
    dealer = property(get_dealer)

table = Table()
table.manage_table()



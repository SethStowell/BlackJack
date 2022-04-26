from hand import Hand

class Player(object):

    def __init__(self, name, money, table):
        self.name = name
        self._money = money
        self.table = table

    def buy_in(self):
        """A player can buy in as long as they have enough money"""
        bet = get_integer_between(0, self._money, f'How much would you like to bet on the next hand, {self._name}?')
        self._money -= bet
        hand = Hand(bet)
        self.hands.append(hand)
        return hand

    def join_table(self):
        pass

    def leave_table(self):
        pass

    def get_table(self):
        return self.table

    def get_money(self):
        return self.money

    table = property(get_table)
    money = property(get_money)
from hand import Hand

class Player(object):

    def __init__(self, name, money, table):
        self.name = name
        self._money = money
        self.table = table

    def __str__(self):
        string = f'Name: {self._name}\nMoney: {self._money}\n'
        for hand in self._hands:
            string += f'{hand}'
        return string

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

    def add_hand(self, hand):
        """Adds a hand to self._hands."""
        self._hands.append(hand)

    def play(self, hand):
        """Returns a players move (either hit, stand, double, or split)."""
        commandString = '[H]it      [S]tand     [D]ouble        s[P]lit\n'
        validCommands = 'HSDP'
        command = None
        if hand.isDone:
            print('Hand cannot be played.')
        else:
            print(commandString)
            print(hand)
            prompt = f"Your move {self._name}: "
            command = input(prompt).upper()
            while command not in validCommands:
                prompt += '(type the corresponding letter) '
                command = input(prompt).upper()
        return command

    def get_hands(self):
        return self._hands

    def get_name(self):
        return self._name

    def get_money(self):
        return self._money

    def set_money(self, money):
        self._money = money

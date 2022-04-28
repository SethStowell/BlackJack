from card import Card
from deck import Deck

def main():
    """
    test all of the objects for this project.
    :return: None
    """
    card_test()
    #deck_test()

def card_test():
    """
    test:
        Creating a new card
        Printing the card
        Getting the soft value of a card
        Getting the hard value of a card
        Getting the suit of a card
        Getting the name of a card
    :return: None
    """
    card = Card('Ace', 'A', 'Spades', '\u2660', '1', '11')
    print(f'card = {card}')
    print(f'card.softValue() = {card.softValue()}')
    print(f'card.hardValue() = {card.hardValue()}')
    print(f'card.suit() = {card.suit()}')
    print(f'card.name() = {card.name()}')

def deck_test():
    """
    test:
        Create a full deck of cards
        Print a deck of cards
        Shuffle a deck of cards
    :return: None
    """
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)

main()
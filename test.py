from hand import Hand
from errors import CallError

def informal_hand_test():
    from deck import Deck
    d = Deck(1)
    d.create_deck()
    h = Hand(10)
    h.isVerbose = True
    print(h)
    c = d.pop()
    c.flip()
    print(c)
    if h.can_hit():
        h.hit(c)
        print(h)
    c = d.pop()
    c.flip()
    print(c)
    if h.can_hit():
        h.hit(c)
        print(h)
    print('Can double:', h.can_double())
    print('Can hit:', h.can_hit())
    print('Can split:', h.can_split())
    c = d.pop()
    c.flip()
    h.double_down(c,h.bet)
    print(h)
    #should be busted now if first cards are A, K, Q
    try:
        c = d.pop()
        c.flip()
        h.hit(c)
    except CallError as error:
        print(error)
        print("tried and failed to hit. Invalid move.")

informal_hand_test()

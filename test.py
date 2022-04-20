from hand import Hand

def informal_hand_test():
    from deck import Deck
    d = Deck()
    h = Hand(10)
    h.isVerbose = True
    print(h)
    c = d.draw()
    c.flip()
    print(c)
    if h.can_hit():
        h.hit(c)
        print(h)
    c = d.draw()
    c.flip()
    print(c)
    if h.can_hit():
        h.hit(c)
        print(h)
    print('Can double:', h.can_double())
    print('Can hit:', h.can_hit())
    print('Can split:', h.can_split())
    c = d.draw()
    c.flip()
    h.double_down(c,h.bet)
    print(h)
    #should be busted now if first cards are A, K, Q
    try:
        c = s.draw()
        c.flip()
        h.hit(c)
    except RuleError as error:
        print(error)
        print("tried and failed to hit. Invalid move.")

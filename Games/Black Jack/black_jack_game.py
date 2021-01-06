# James hooper
# 1/6/2021
# Black Jack Game
import playing_cards as pc
import game_functions as gf

class BJ_Cards(pc.Pos_Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.faceup:
            v = BJ_Cards.RANKS.index((self.rank)) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(pc.Deck):
    def populate(self):
        for suit in BJ_Cards.SUITS:
            for rank in BJ_Cards.RANKS:
                self.add(BJ_Cards(rank,suit))

class BJ_Hand(pc.Hand):
    def __init__(self,name):
        super(BJ_Hand, self).__init__()
        self.name = name

# testing Area
deck = BJ_Deck()
deck.populate()
deck.shuffle()

card = deck.cards[0]
print(card)
print(card.value)
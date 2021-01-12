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

    def __str__(self):
        print("##################################################################")
        for card in self.cards:
            print(card)
        rep = "##################################################################"
        rep += "/n " + self.name
        rep += "/n " + self.total
        return rep

    @property
    def total(self):
        # if a card in the and has a value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None

        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value

        # determine if hand contains an Ace
        has_ace = False
        for card in self.cards:
            if card.value == BJ_Cards.ACE_VALUE:
                has_ace = True

        # if hand contains Ace and total is low enough, treat Ace as 11
        if has_ace and total <= 11:
            t += 10 #  add only 10 since we've already added 1 for the Ace
        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):

    def bust(self):
        print(self.name, "busts. ")
    def lose(self):
        print(self.name, "loses. ")
    def win(self):
        print(self.name, "wins. ")
    def push(self):
        print(self.name, "pushes. ")
    def is_drawing(self):
        response = gf.ask_yes_no("\n" + self.name + ", do you want to draw a card? (Y/N): ")
        return response == "y"

class BJ_Dealer(BJ_Hand):
    def is_drawing(self):
        return self.total < 17
    def bust(self):
        print(self.name, "busts. ")
    def flip_first_card(self):
        self.cards[0].flip()

class Game(object):
    def __init__(self,names):
        self.deck = BJ_Deck
        self.deck.populate()
        self.deck.shuffle()
        self.dealer = BJ_Dealer("The Dealer")
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp



# testing Area
deck = BJ_Deck()
deck.populate()
deck.shuffle()

card = deck.cards[0]
print(card)
print(card.value)
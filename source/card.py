import globals

class Card:
    def __init__(self, rank, suit):
        if(isinstance(rank, str)):
            self.rank = globals.LUT_RANK.index(rank)
        else:
            self.rank = rank
        if(isinstance(suit, str)):
            self.suit = globals.LUT_SUIT.index(suit)
        else:
            self.suit = suit
        self.is_locked = False
        self.is_held = False

    # returns card value (2-14)
    def getValue(self):
        return globals.DICT_VALUE[globals.LUT_RANK[self.rank]]

    def toString(self):
        return globals.LUT_RANK[self.rank] + globals.LUT_SUIT[self.suit]

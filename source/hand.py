import globals
from card import Card
from deck import Deck
import csv

class Hand:
    def __init__(self):
        self.cards = []
        self.hand_rank = globals.HAND_RANK_ERROR

        for index_card in range(globals.NUM_CARDS_HAND):
            self.cards.append(Card(globals.CARD_ERROR, globals.CARD_ERROR))

    def evaluate(self):
        self.sort()
        return self.getRank()

    def sort(self):
        for index_primary in range(len(self.cards) - 1):
            for index_secondary in range(index_primary + 1, len(self.cards)):
                if(self.cards[index_primary].rank > self.cards[index_secondary].rank):
                    card_temp = self.cards[index_primary]
                    self.cards[index_primary] = self.cards[index_secondary]
                    self.cards[index_secondary] = card_temp

    def getRank(self):
        if self.isFlush():
            if self.isStraight():
                return globals.HAND_RANK_STRAIGHT_FLUSH
            return globals.HAND_RANK_FLUSH
        
        if self.isStraight():
            return globals.HAND_RANK_STRAIGHT
        
        counter = []
        pairs = 0
        triples = 0

        # create a counter array to keep track of the number of instances of each card value
        for index_counter in range(globals.NUM_VALUES):
            counter.append(0)

        # count each value
        for index_card in range(len(self.cards)):
            counter[self.cards[index_card].rank] += 1

        #check for four of a kind, three of a kind, and pairs
        for index_counter in range(len(counter)):
            if counter[index_counter] == 4:
                return globals.HAND_RANK_FOUR_OF_A_KIND
            if counter[index_counter] == 3:
                triples += 1
            if counter[index_counter] == 2:
                pairs += 1

        if triples == 1 and pairs == 1:
            return globals.HAND_RANK_FULL_HOUSE
        
        if triples == 1:
            return globals.HAND_RANK_THREE_OF_A_KIND
        
        if pairs == 2:
            return globals.HAND_RANK_TWO_PAIR
        
        if pairs == 1:
            return globals.HAND_RANK_PAIR

        return globals.HAND_RANK_HIGH_CARD
    
    # args - monster_suit: the suit of the monster who the hand belongs to
    # returns the sum of the int values (2-14) of the cards in hand
    def getValue(self, monster_suit):
        value = 0
        for index_hand in range(len(self.cards)):
            print(self.cards[index_hand].getValue())
            if(self.cards[index_hand].suit == monster_suit):
                value += (globals.HAND_SAME_SUIT_BONUS * self.cards[index_hand].getValue())
            else:
                value += self.cards[index_hand].getValue()
        return value

    def isFlush(self):
        if ((self.cards[0].suit == self.cards[1].suit) and
            (self.cards[0].suit == self.cards[2].suit) and
            (self.cards[0].suit == self.cards[3].suit) and
            (self.cards[0].suit == self.cards[4].suit)):
            return True
        
        return False

    def isStraight(self):
        if ((self.cards[0].rank == globals.CARD_VALUE_ACE) and
            (self.cards[1].rank == globals.CARD_VALUE_TEN) and
            (self.cards[2].rank == globals.CARD_VALUE_JACK) and
            (self.cards[3].rank == globals.CARD_VALUE_QUEEN) and
            (self.cards[4].rank == globals.CARD_VALUE_KING)):
            return True
        
        for index_cards in range(len(self.cards) - 1):
            if self.cards[index_cards].rank != (self.cards[index_cards + 1].rank - 1):
                return False
            
        return True

    def toString(self):
        output = ""

        for index_card in range(len(self.cards)):
            output += self.cards[index_card].toString()

        return output

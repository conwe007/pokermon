import random
import json
import uuid
import globals
from card import Card

class Deck:
    def __init__(self):
        random.seed()
        self.cards = []
        self.index = 0

        for suit in range(globals.NUM_SUITS):
            for value in range(globals.NUM_VALUES):
                self.cards.append(Card(value, suit))
        
        return
    
    # arg deck_json - json object containing monster deck data
    def load(self, monster_deck_json):
        self.cards = []
        self.index = 0

        for index_deck_json in range(len(monster_deck_json)):
            value = monster_deck_json[index_deck_json]["value"]
            suit = monster_deck_json[index_deck_json]["suit"]
            self.cards.append(Card(value, suit))
        
        return

    # returns the next card in the deck and increments the deck index
    def deal(self):
        self.index += 1
        return self.cards[self.index - 1]
    
    # shuffle the deck and reset the deck index
    def shuffle(self):
        self.index = 0

        for index_current in range(len(self.cards)):
            index_new = random.randrange(index_current, len(self.cards))
            card_temp = self.cards[index_current]
            self.cards[index_current] = self.cards[index_new]
            self.cards[index_new] = card_temp
        
        return
    
    # sort the deck and reset the deck index
    def sort(self):
        self.index = 0
        
        # first sort by suit
        for index_cards_primary in range(len(self.cards) - 1):
            for index_cards_secondary in range(index_cards_primary, len(self.cards)):
                if self.cards[index_cards_primary].suit > self.cards[index_cards_secondary].suit:
                    card_temp = self.cards[index_cards_primary]
                    self.cards[index_cards_primary] = self.cards[index_cards_secondary]
                    self.cards[index_cards_secondary] = card_temp
        
        # next sort by value within each suit
        index_cards = 0
        for index_suit in range(globals.NUM_SUITS):
            for index_cards_primary in range(index_cards, index_cards + self.numCardsSuit(index_suit) - 1):
                for index_cards_secondary in range(index_cards_primary, index_cards + self.numCardsSuit(index_suit)):
                    if self.cards[index_cards_primary].value > self.cards[index_cards_secondary].value:
                        card_temp = self.cards[index_cards_primary]
                        self.cards[index_cards_primary] = self.cards[index_cards_secondary]
                        self.cards[index_cards_secondary] = card_temp
            index_cards += self.numCardsSuit(index_suit)
        
        return
    
    # return the number of cards of a given suit in the deck
    def numCardsSuit(self, suit):
        num_cards_suit = 0

        for index_cards in range(len(self.cards)):
            if(self.cards[index_cards].suit == suit):
                num_cards_suit += 1
        
        return num_cards_suit
    
    # return the number of cards of a given value in the deck
    def numCardsValue(self, value):
        num_cards_value = 0

        for index_cards in range(len(self.cards)):
            if(self.cards[index_cards].value == value):
                num_cards_value += 1
        
        return num_cards_value

    def toString(self):
        output = ""
        index_cards = 0

        for index_suit in range(globals.NUM_SUITS):
            for index_cards_suit in range(index_cards, index_cards + self.numCardsSuit(index_suit)):
                output += self.cards[index_cards].toString()
                index_cards += 1
            output += "\n"

        return output

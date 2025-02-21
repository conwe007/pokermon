import uuid
import json
import globals
from deck import Deck
from hand import Hand

class Monster:
    def __init__(self, pokerdex_json, monster_id):
        self.instance_id = uuid.uuid4()
        self.name = pokerdex_json[monster_id]["name"]
        self.level = 1
        self.deck = Deck()
        self.deck.load(pokerdex_json[monster_id]["deck"])
        self.hand = Hand()
        self.type = pokerdex_json[monster_id]["type"]
        self.speed = pokerdex_json[monster_id]["speed"]
        self.hitpoints_max = pokerdex_json[monster_id]["hitpoints_max"]
        self.hitpoints_current = self.hitpoints_max
        return
    
    # populate full hand from deck
    def dealHand(self):
        self.deck.shuffle()
        for index_hand in range(len(self.hand.cards)):
            if(not self.hand.cards[index_hand].is_held):
                self.hand.cards[index_hand] = self.deck.deal()
            self.hand.cards[index_hand].is_held = False
        return

    # deal card to specified hand index
    def dealCard(self, index_hand):
        self.hand.cards[index_hand] = self.deck.deal()
        return

    # return hand value
    def handValue(self):
        return

    # load monster data from saved data in a json object
    def load(self, monster_json):
        self.name = monster_json["name"]
        self.level = monster_json["level"]
        self.type = monster_json["type"]
        self.speed = monster_json["speed"]
        self.hitpoints_max = monster_json["hitpoints_max"]
        self.hitpoints_current = monster_json["hitpoints_current"]
        return

    # save monster data into a json object
    def save(self):
        monster_json = json.dumps(self)
        return monster_json

    # initialize monster based on data present in file
    def initialize(filename):
        return
        
    def isAlive(self):
        return self.hitpoints_current > 0

    def toJSON(self):
        output = json.dumps(
            
        )
        return output

    def toStringHand(self):
        return self.hand.toString()

    def toString(self):
        output = "ID: "+ str(self.instance_id) + "\n"
        output += "Name: " + self.name + "\n"
        output += "Level: " + str(self.level) + "\n"
        output += "Type: " + self.type + "\n"
        output += "Speed: " + str(self.speed) + "\n"
        output += "Current Hitpoints: " + str(self.hitpoints_current) + "\n"
        output += "Max Hitpoints: " + str(self.hitpoints_max) + "\n"
        output += "Deck:\n" + self.deck.toString() + "\n"
        output += "Hand: " + self.hand.toString() + "\n"
        return output

import uuid
import json
import globals
from deck import Deck

class Monster:
    def __init__(self, pokerdex_json, monster_id):
        self.instance_id = uuid.uuid4()
        self.name = pokerdex_json[monster_id]["name"]
        self.level = 1
        self.deck = Deck()
        self.deck.load(pokerdex_json[monster_id]["deck"])

        # for index_moves_json in range(len(moves_json)):
        #     self.moves[index_moves_json].load(moves_json[index_moves_json])

        self.type = pokerdex_json[monster_id]["type"]
        self.attack = pokerdex_json[monster_id]["base"]["attack"]
        self.defense = pokerdex_json[monster_id]["base"]["defense"]
        self.speed = pokerdex_json[monster_id]["base"]["speed"]
        self.hitpoints_max = pokerdex_json[monster_id]["base"]["hitpoints_max"]
        self.hitpoints_current = self.hitpoints_max

        return
    
    # load monster data from saved data in a json object
    def load(self, monster_json):
        self.name = monster_json["name"]
        self.level = monster_json["level"]
        # self.deck.load(deck_json)

        # for index_moves_json in range(len(moves_json)):
            # self.moves[index_moves_json].load(moves_json[index_moves_json])

        self.type = monster_json["type"]
        self.attack = monster_json["attack"]
        self.defense = monster_json["defense"]
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
    
    def actionAttack(self):
        
        return
    
    def actionDefend(self):
        return
    
    def actionDraw(self):
        return
    
    def actionSpecial(self):

        return
    
    def isAlive(self):
        return self.hitpoints_current > 0

    def toJSON(self):
        output = json.dumps(
            
        )
        return output
    
    def toString(self):
        output = "ID: "+ str(self.instance_id) + "\n"
        output += "Name: " + self.name + "\n"
        output += "Level: " + str(self.level) + "\n"
        output += "Type: " + self.type + "\n"
        output += "Attack: " + str(self.attack) + "\n"
        output += "Defense: " + str(self.defense) + "\n"
        output += "Speed: " + str(self.speed) + "\n"
        output += "Current Hitpoints: " + str(self.hitpoints_current) + "\n"
        output += "Max Hitpoints: " + str(self.hitpoints_max) + "\n"
        output += "Deck:\n" + self.deck.toString() + "\n"
        return output


with open("./assets/monsters/pokerdex.json", mode="r") as pokerdex:
    pokerdex_data = pokerdex.read()
    pokerdex_json = json.loads(pokerdex_data)
    m = Monster(pokerdex_json, 0)
    print(m.toString())

q = m.save()
print(q)


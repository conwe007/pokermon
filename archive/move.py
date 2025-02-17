import globals
import json

# Move
# type - type of move (spade, heart, etc.), affects damage against weak types
# power - how much damage the move does
# accuracy - chance of move hitting
# special - which special effect the move triggers, if any

class Move:
    def __init__(self):
        self.type = globals.TYPE_ERROR
        self.power = globals.MOVE_POWER_ERROR
        self.accuracy = globals.MOVE_ACCURACY_ERROR
        self.special = globals.MOVE_SPECIAL_NONE
    
    def load(self, move_json):
        self.type = move_json["type"]
        self.power = move_json["power"]
        self.accuracy = move_json["accuracy"]
        self.special = move_json["special"]


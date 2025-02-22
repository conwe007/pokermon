import uuid
import json
import globals
from monster import Monster

class Player:
    def __init__(self):
        self.name = "Randy"
        self.monster = None
        self.money = 0
        return
    
    def chooseAIAction(self):

        return
    
    def setMonster(self, monster):
        self.monster = monster
        return
    
    def isAlive(self):
        return self.monster.isAlive()

    def toString(self):
        output = "Name: " + self.name + "\n"
        output += "Money: " + str(self.money) + "\n"
        output += "Monster:\n" + self.monster.toString()
        return output
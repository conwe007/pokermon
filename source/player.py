import uuid
import json
import globals
from monster import Monster

class Player:
    def __init__(self):
        self.name = "Randy"
        self.monsters = []
        self.money = 0
        return
    
    def chooseAIAction(self):

        return
    
    def addMonster(self, monster):
        self.monsters.append(monster)
        return
    
    def hasLivingMonsters(self):
        for index_monster in range(len(self.monsters)):
            if(self.monsters[index_monster].isAlive()):
                return True
        return False

    def toString(self):
        output = "Name: " + self.name + "\n"
        output += "Money: " + str(self.money) + "\n"
        for index_monster in range(len(self.monsters)):
            output += "Monster[" + str(index_monster) + "]:\n" + self.monsters[index_monster].toString()
        return output
import random
import globals
from player import Player
from user_interface import UI




class Battle:
    def __init__(self, player, opponent):
        random.seed()
        self.player = player
        self.player_index_monster = 0 # index of the player monster currently in play
        self.opponent = opponent
        self.opponent_index_monster = 0 # index of the opponent monster currently in play
        self.turn = globals.TURN_UNDETERMINED
        return

    def run(self):
        while(not self.isFinished()):
            if(self.turn == globals.TURN_UNDETERMINED):
                # player's monster is faster
                if(self.player.monsters[self.player_index_monster].speed > self.opponent.monsters[self.opponent_index_monster].speed):
                    self.turn = globals.TURN_PLAYER
                # opponent's monster is faster
                elif(self.opponent.monsters[self.opponent_index_monster].speed > self.player.monsters[self.player_index_monster].speed):
                    self.turn = globals.TURN_OPPONENT
                # player's and opponents monsters are equally fast, randomly determine whose turn it is
                else:
                    self.turn = random.choice([globals.TURN_OPPONENT, globals.TURN_PLAYER])
            elif(self.turn == globals.TURN_PLAYER):
                player_action = UI.battleSelectAction()
                match player_action:
                    case globals.ACTION_ATTACK:
                        player_damage = self.calculateDamage(self.player.monsters[self.player_index_monster], self.opponent.monsters[self.opponent_index_monster])
                        print(str(player_damage))
                    case globals.ACTION_DEFEND:
                        print("player action defend")
                    case globals.ACTION_DRAW:
                        print("player action draw")
                    case globals.ACTION_SPECIAL:
                        print("player action special")
                    case globals.ACTION_SWITCH:
                        print("player action switch")
                    case globals.ACTION_ERROR:
                        print("error: invalid player action")
                self.turn = globals.TURN_OPPONENT
            elif(self.turn == globals.TURN_OPPONENT):
                opponent_action = self.opponentSelectAction()
                print(str(opponent_action))
                match opponent_action:
                    case globals.ACTION_ATTACK:
                        print("opponent action attack")
                    case globals.ACTION_DEFEND:
                        print("opponent action defend")
                    case globals.ACTION_DRAW:
                        print("opponent action draw")
                    case globals.ACTION_SPECIAL:
                        print("opponent action special")
                    case globals.ACTION_ERROR:
                        print("error: invalid opponent action")
                self.turn = globals.TURN_PLAYER
            else:
                print("error, unexpected turn variable")
    
    @staticmethod
    def opponentSelectAction():
        action = random.choice([globals.ACTION_ATTACK, globals.ACTION_DEFEND, globals.ACTION_DRAW, globals.ACTION_SPECIAL])
        return action

    @staticmethod
    def calculateDamage(monster_attacker, monster_defender):
        type_effectiveness = 0
        if(monster_attacker.type == globals.TYPE_CLUB and monster_defender.type == globals.TYPE_DIAMOND or \
            monster_attacker.type == globals.TYPE_SPADE and monster_defender.type == globals.TYPE_HEART or \
            monster_attacker.type == globals.TYPE_HEART and monster_defender.type == globals.TYPE_CLUB or \
            monster_attacker.type == globals.TYPE_DIAMOND and monster_defender.type == globals.TYPE_SPADE):
            type_effectiveness = 1.1
        elif(monster_attacker.type == globals.TYPE_CLUB and monster_defender.type == globals.TYPE_DIAMOND or \
            monster_attacker.type == globals.TYPE_SPADE and monster_defender.type == globals.TYPE_HEART or \
            monster_attacker.type == globals.TYPE_HEART and monster_defender.type == globals.TYPE_CLUB or \
            monster_attacker.type == globals.TYPE_DIAMOND and monster_defender.type == globals.TYPE_SPADE):
            type_effectiveness = 0.9
        else:
            type_effectiveness = 1.0
        damage = ((monster_attacker.attack / monster_defender.defense) + 2) * type_effectiveness
        return damage

    # returns true if the battle is over because one player has no more monsters with HP, false otherwise
    def isFinished(self):
        if(self.player.hasLivingMonsters() or self.opponent.hasLivingMonsters()):
            return False
        return True

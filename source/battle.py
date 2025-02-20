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
            ### START OF BATTLE
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
            ### PLAYER'S TURN
            elif(self.turn == globals.TURN_PLAYER):
                player_action = UI.battleSelectAction()
                match player_action:
                    case globals.ACTION_DRAW:
                        print("player action draw")
                        UI.battleSelectPlayerCards()
                    case globals.ACTION_CASHOUT:
                        print("player action cashout")
                    case globals.ACTION_ERROR:
                        print("error: invalid player action")
                self.turn = globals.TURN_OPPONENT
            ### OPPONENT'S TURN
            elif(self.turn == globals.TURN_OPPONENT):
                opponent_action = self.opponentSelectAction()
                print(str(opponent_action))
                match opponent_action:
                    case globals.ACTION_DRAW:
                        print("opponent action draw")
                    case globals.ACTION_CASHOUT:
                        print("opponent action cashout")
                    case globals.ACTION_ERROR:
                        print("error: invalid opponent action")
                self.turn = globals.TURN_PLAYER
            ### TURN ERROR
            else:
                print("error: unexpected turn variable\n")
    
    # calculate monster_attack hand value and apply hand value * multiplier damage to monster_defender
    def attack(monster_attacker, monster_defender, multiplier):
        return
    
    # calcualte monster_healer hand value and heal hand value * multiplier HP
    def heal(monster_healer, multiplier):
        return
    
    # randomly select quantity of monster_defender's hand cards and redraw them
    def forceDrawRandom(monster_defender, quantity):
        return
    
    # prompt UI to select quanity of monster_defender's hand cards redraw them
    def forceDrawTarget(monster_defender, quantity):
        return
    
    # randomly select quantity of monster_defender's hand cards and mark them as locked
    def lockRandom(monster_defender, quantity):
        return
    
    # prompt UI to select quantity of monster_defender's hand cards and mark them as locked
    def lockTarget(monster_defender, quantity):
        return
    
    # prompt UI to select quantity of monster_holder's hand cards and mark them as held
    def holdPlayer(monster_holder, quantity):
        return
    
    # AI selects quantity of monster_holder's hand cards and mark them as held
    def holdOpponent(monster_holder, quantity):
        return

    @staticmethod
    def opponentSelectAction():
        action = random.choice([globals.ACTION_ATTACK, globals.ACTION_DEFEND, globals.ACTION_DRAW, globals.ACTION_SPECIAL])
        return action

    # returns true if the battle is over because one player has no more monsters with HP, false otherwise
    def isFinished(self):
        if(self.player.hasLivingMonsters() or self.opponent.hasLivingMonsters()):
            return False
        return True

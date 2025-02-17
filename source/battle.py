import random
from player import Player

TURN_UNDETERMINED = -1
TURN_PLAYER = 0
TURN_OPPONENT = 1


class Battle:
    def __init__(self, player, opponent):
        random.seed()
        self.player = player
        self.player_index_monster = 0 # index of the player monster currently in play
        self.opponent = opponent
        self.opponent_index_monster = 0 # index of the opponent monster currently in play
        self.turn = TURN_UNDETERMINED
        return

    def run(self):
        if(self.turn == TURN_UNDETERMINED):
            # player's monster is faster
            if(self.player.monsters[self.player_index_monster].speed > self.opponent.monsters[self.opponent_index_monster].speed):
                self.turn = TURN_PLAYER
            # opponent's monster is faster
            elif(self.opponent.monsters[self.opponent_index_monster].speed > self.player.monsters[self.player_index_monster].speed):
                self.turn - TURN_OPPONENT
            # player's and opponents monsters are equally fast, randomly determine whose turn it is
            else:
                self.turn = random.choice([TURN_OPPONENT, TURN_PLAYER])
        elif(self.turn == TURN_PLAYER):

            self.turn = TURN_OPPONENT
        elif(self.turn == TURN_OPPONENT):

            self.turn = TURN_PLAYER
        else:
            print("error, unexpected turn variable")
        return
    
    # returns true if the battle is over because one player has no more monsters with HP, false otherwise
    def isFinished(self):
        if(self.player.hasLivingMonsters() or self.opponent.hasLivingMonsters()):
            return False
        return True

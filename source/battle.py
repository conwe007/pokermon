import random
import globals
from player import Player
from monster import Monster
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
            print(self.isFinished())
            ### START OF BATTLE ###
            if(self.turn == globals.TURN_UNDETERMINED):
                # deal each monster a hand
                self.player.monsters[self.player_index_monster].dealHand()
                self.opponent.monsters[self.opponent_index_monster].dealHand()
                # player's monster is faster
                if(self.player.monsters[self.player_index_monster].speed > self.opponent.monsters[self.opponent_index_monster].speed):
                    self.turn = globals.TURN_PLAYER
                # opponent's monster is faster
                elif(self.opponent.monsters[self.opponent_index_monster].speed > self.player.monsters[self.player_index_monster].speed):
                    self.turn = globals.TURN_OPPONENT
                # player's and opponents monsters are equally fast, randomly determine whose turn it is
                else:
                    self.turn = random.choice([globals.TURN_OPPONENT, globals.TURN_PLAYER])

            ### PLAYER'S TURN ###
            elif(self.turn == globals.TURN_PLAYER):
                print("Player Monster Hand: " + self.player.monsters[self.player_index_monster].hand.toString())
                is_valid_action = False
                # keep prompting until a valid action is selected
                while(not is_valid_action):
                    player_action = UI.battleSelectAction()
                    if(player_action == globals.ACTION_DRAW or player_action == globals.ACTION_CASHOUT):
                        is_valid_action = True
                    else:
                        print("invalid action")
                match player_action:
                    ### PLAYER DRAW ###
                    case globals.ACTION_DRAW:
                        is_valid_selection = False
                        selected_card_indicies = []
                        while(not is_valid_selection):
                            selected_card_indicies = UI.battleSelectPlayerCards()
                            is_valid_selection = True
                            for index in selected_card_indicies:
                                if(index < 0 or index >= len(self.player.monsters[self.player_index_monster].hand.cards)):
                                    is_valid_selection = False
                                    print("invalid selection")
                        selected_cards = []
                        for index_card in range(len(self.player.monsters[self.player_index_monster].hand.cards)):
                            if(index_card in selected_card_indicies):
                                selected_cards.append(self.player.monsters[self.player_index_monster].hand.cards[index_card])
                                self.player.monsters[self.player_index_monster].dealCard(index_card)
                        print("Player Monster Hand: " + self.player.monsters[self.player_index_monster].hand.toString())
                    ### PLAYER CASHOUT ###
                    case globals.ACTION_CASHOUT:
                        player_hand_rank = self.player.monsters[self.player_index_monster].handRank()
                        print(globals.LUT_HAND_RANK[player_hand_rank])
                        # initialize mechanic multipliers/quantities
                        multiplier_attack = 0
                        multiplier_healing = 0
                        quantity_force_draw_random = 0
                        quantity_force_draw_target = 0
                        quantity_lock_random = 0
                        quantity_lock_target = 0
                        quantity_hold = 0
                        # assign mechanic values based on hand rank
                        match player_hand_rank:
                            case globals.HAND_RANK_HIGH_CARD:
                                multiplier_attack = globals.MULTIPLIER_HIGH_CARD_ATTACK
                                multiplier_healing = globals.MULTIPLIER_HIGH_CARD_HEALING
                                quantity_force_draw_random = globals.QUANTITY_HIGH_CARD_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_HIGH_CARD_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_HIGH_CARD_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_HIGH_CARD_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_HIGH_CARD_HOLD
                            case globals.HAND_RANK_PAIR:
                                multiplier_attack = globals.MULTIPLIER_PAIR_ATTACK
                                multiplier_healing = globals.MULTIPLIER_PAIR_HEALING
                                quantity_force_draw_random = globals.QUANTITY_PAIR_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_PAIR_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_PAIR_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_PAIR_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_PAIR_HOLD
                            case globals.HAND_RANK_TWO_PAIR:
                                multiplier_attack = globals.MULTIPLIER_TWO_PAIR_ATTACK
                                multiplier_healing = globals.MULTIPLIER_TWO_PAIR_HEALING
                                quantity_force_draw_random = globals.QUANTITY_TWO_PAIR_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_TWO_PAIR_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_TWO_PAIR_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_TWO_PAIR_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_TWO_PAIR_HOLD
                            case globals.HAND_RANK_THREE_OF_A_KIND:
                                multiplier_attack = globals.MULTIPLIER_THREE_OF_A_KIND_ATTACK
                                multiplier_healing = globals.MULTIPLIER_THREE_OF_A_KIND_HEALING
                                quantity_force_draw_random = globals.QUANTITY_THREE_OF_A_KIND_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_THREE_OF_A_KIND_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_THREE_OF_A_KIND_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_THREE_OF_A_KIND_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_THREE_OF_A_KIND_HOLD
                            case globals.HAND_RANK_STRAIGHT:
                                multiplier_attack = globals.MULTIPLIER_STRAIGHT_ATTACK
                                multiplier_healing = globals.MULTIPLIER_STRAIGHT_HEALING
                                quantity_force_draw_random = globals.QUANTITY_STRAIGHT_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_STRAIGHT_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_STRAIGHT_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_STRAIGHT_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_STRAIGHT_HOLD
                            case globals.HAND_RANK_FLUSH:
                                multiplier_attack = globals.MULTIPLIER_FLUSH_ATTACK
                                multiplier_healing = globals.MULTIPLIER_FLUSH_HEALING
                                quantity_force_draw_random = globals.QUANTITY_FLUSH_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_FLUSH_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_FLUSH_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_FLUSH_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_FLUSH_HOLD
                            case globals.HAND_RANK_FULL_HOUSE:
                                multiplier_attack = globals.MULTIPLIER_FULL_HOUSE_ATTACK
                                multiplier_healing = globals.MULTIPLIER_FULL_HOUSE_HEALING
                                quantity_force_draw_random = globals.QUANTITY_FULL_HOUSE_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_FULL_HOUSE_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_FULL_HOUSE_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_FULL_HOUSE_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_FULL_HOUSE_HOLD
                            case globals.HAND_RANK_FOUR_OF_A_KIND:
                                multiplier_attack = globals.MULTIPLIER_FOUR_OF_A_KIND_ATTACK
                                multiplier_healing = globals.MULTIPLIER_FOUR_OF_A_KIND_HEALING
                                quantity_force_draw_random = globals.QUANTITY_FOUR_OF_A_KIND_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_FOUR_OF_A_KIND_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_FOUR_OF_A_KIND_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_FOUR_OF_A_KIND_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_FOUR_OF_A_KIND_HOLD
                            case globals.HAND_RANK_STRAIGHT_FLUSH:
                                multiplier_attack = globals.MULTIPLIER_STRAIGHT_FLUSH_ATTACK
                                multiplier_healing = globals.MULTIPLIER_STRAIGHT_FLUSH_HEALING
                                quantity_force_draw_random = globals.QUANTITY_STRAIGHT_FLUSH_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_STRAIGHT_FLUSH_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_STRAIGHT_FLUSH_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_STRAIGHT_FLUSH_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_STRAIGHT_FLUSH_HOLD
                            case globals.HAND_RANK_FIVE_OF_A_KIND:
                                multiplier_attack = globals.MULTIPLIER_FIVE_OF_A_KIND_ATTACK
                                multiplier_healing = globals.MULTIPLIER_FIVE_OF_A_KIND_HEALING
                                quantity_force_draw_random = globals.QUANTITY_FIVE_OF_A_KIND_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_FIVE_OF_A_KIND_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_FIVE_OF_A_KIND_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_FIVE_OF_A_KIND_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_FIVE_OF_A_KIND_HOLD
                            case globals.HAND_RANK_FLUSH_HOUSE:
                                multiplier_attack = globals.MULTIPLIER_FLUSH_HOUSE_ATTACK
                                multiplier_healing = globals.MULTIPLIER_FLUSH_HOUSE_HEALING
                                quantity_force_draw_random = globals.QUANTITY_FLUSH_HOUSE_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_FLUSH_HOUSE_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_FLUSH_HOUSE_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_FLUSH_HOUSE_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_FLUSH_HOUSE_HOLD
                            case globals.HAND_RANK_FLUSH_FIVE:
                                multiplier_attack = globals.MULTIPLIER_FLUSH_FIVE_ATTACK
                                multiplier_healing = globals.MULTIPLIER_FLUSH_FIVE_HEALING
                                quantity_force_draw_random = globals.QUANTITY_FLUSH_FIVE_FORCE_DRAW_RANDOM
                                quantity_force_draw_target = globals.QUANTITY_FLUSH_FIVE_FORCE_DRAW_TARGET
                                quantity_lock_random = globals.QUANTITY_FLUSH_FIVE_LOCK_RANDOM
                                quantity_lock_target = globals.QUANTITY_FLUSH_FIVE_LOCK_TARGET
                                quantity_hold = globals.QUANTITY_FLUSH_FIVE_HOLD
                            case globals.HAND_RANK_ERROR:
                                multiplier_attack = 0
                                multiplier_healing = 0
                                quantity_force_draw_random = 0
                                quantity_force_draw_target = 0
                                quantity_lock_random = 0
                                quantity_lock_target = 0
                                quantity_hold = 0
                        if(multiplier_attack != 0):
                            damage = self.attack(self.player.monsters[self.player_index_monster], self.opponent.monsters[self.opponent_index_monster], multiplier_attack)
                            print("Dealt " + str(damage) + " damage")
                            if(self.opponent.monsters[self.opponent_index_monster].hitpoints_current <= 0):
                                print("Opponent monster defeated")
                            else:
                                print("Opponent monster [" + str(self.opponent_index_monster) + "] has " + self.opponent.monsters[self.opponent_index_monster].toStringHitpoints() + " hitpoints left")
                        if(multiplier_healing != 0):
                            healing = self.heal(self.player.monsters[self.player_index_monster], multiplier_healing)
                            print("Healed " + str(healing) + " damage")
                            print("Player monster [" + str(self.opponent_index_monster) + "] has " + self.player.monsters[self.player_index_monster].toStringHitpoints() + " hitpoints left")
                        if(quantity_force_draw_random != 0):
                            pass
                        if(quantity_force_draw_target != 0):
                            pass
                        if(quantity_lock_random != 0):
                            pass
                        if(quantity_lock_target != 0):
                            pass
                        if(quantity_hold != 0):
                            pass
                    ### PLAYER ACTION ERROR ###
                    case globals.ACTION_ERROR:
                        print("error: invalid player action")
                self.turn = globals.TURN_OPPONENT

            ### OPPONENT'S TURN ###
            elif(self.turn == globals.TURN_OPPONENT):
                opponent_action = self.opponentSelectAction()
                match opponent_action:
                    ### OPPONENT DRAW ###
                    case globals.ACTION_DRAW:
                        print("opponent action draw")
                    ### OPPONENT CASHOUT ###
                    case globals.ACTION_CASHOUT:
                        print("opponent action cashout")
                    ### OPPONENT ACTION ERROR ###
                    case globals.ACTION_ERROR:
                        print("error: invalid opponent action")
                self.turn = globals.TURN_PLAYER
            ### TURN ERROR
            else:
                print("error: unexpected turn variable\n")
        print("battle finished")

    # calculate monster_attack hand value and apply hand value * multiplier damage to monster_defender
    # returns the amount of damage dealt
    def attack(self, monster_attacker : Monster, monster_defender : Monster, multiplier : int) -> int:
        damage = monster_attacker.handValue() * multiplier
        monster_defender.hitpoints_current -= damage
        return damage
    
    # calcualte monster_healer hand value and heal hand value * multiplier HP
    # returns the amount of hitpoints healed
    def heal(self, monster_healer : Monster, multiplier : int) -> int:
        healing = monster_healer.handValue() * multiplier
        monster_healer.hitpoints_current += healing
        if(monster_healer.hitpoints_current > monster_healer.hitpoints_max):
            monster_healer.hitpoints_current = monster_healer.hitpoints_max
        return healing
    
    # randomly select quantity of monster_defender's hand cards and redraw them
    def forceDrawRandom(self, monster_defender : Monster, quantity : int) -> None:
        
        return
    
    # prompt UI to select quanity of monster_defender's hand cards redraw them
    def forceDrawTarget(self, monster_defender : Monster, quantity : int) -> None:
        return
    
    # randomly select quantity of monster_defender's hand cards and mark them as locked
    def lockRandom(self, monster_defender : Monster, quantity : int) -> None:
        return
    
    # prompt UI to select quantity of monster_defender's hand cards and mark them as locked
    def lockTarget(self, monster_defender : Monster, quantity : int) -> None:
        return
    
    # prompt UI to select quantity of monster_holder's hand cards and mark them as held
    def holdPlayer(self, monster_holder : Monster, quantity : int) -> None:
        return
    
    # AI selects quantity of monster_holder's hand cards and mark them as held
    def holdOpponent(self, monster_holder : Monster, quantity : int) -> None:
        return

    # prompts UI to select from player cards, then returns an array of indicies
    def playerSelectCards() -> list[int]:
        is_valid_selection = False
        selected_card_indicies = []
        while(not is_valid_selection):
            selected_card_indicies = UI.battleSelectPlayerCards()
            is_valid_selection = True
            for index in selected_card_indicies:
                if(index < 0 or index >= globals.NUM_CARDS_HAND):
                    is_valid_selection = False
                    print("invalid selection")
        return selected_card_indicies

    @staticmethod
    def opponentSelectAction() -> int:
        action = random.choice([globals.ACTION_DRAW, globals.ACTION_CASHOUT])
        return action

    # returns true if the battle is over because one player has no more monsters with HP, false otherwise
    def isFinished(self) -> bool:
        if(self.player.hasLivingMonsters() and self.opponent.hasLivingMonsters()):
            return False
        return True

import random
import globals
from player import Player
from monster import Monster
from user_interface import UI
from modifiers import Modifiers



class Battle:
    def __init__(self, player, opponent):
        random.seed()
        self.player = player
        self.opponent = opponent
        self.turn = globals.TURN_UNDETERMINED
        self.modifiers = Modifiers()
        return

    def run(self):
        while(not self.isFinished()):
            ### START OF BATTLE ###
            if(self.turn == globals.TURN_UNDETERMINED):
                # deal each monster a hand
                self.player.monster.dealHand()
                self.player.monster.hand.cards[0].is_locked = True
                self.opponent.monster.dealHand()
                # player's monster is faster
                if(self.player.monster.speed > self.opponent.monster.speed):
                    self.turn = globals.TURN_PLAYER
                # opponent's monster is faster
                elif(self.opponent.monster.speed > self.player.monster.speed):
                    self.turn = globals.TURN_OPPONENT
                # player's and opponents monsters are equally fast, randomly determine whose turn it is
                else:
                    self.turn = random.choice([globals.TURN_OPPONENT, globals.TURN_PLAYER])

            ### PLAYER'S TURN ###
            elif(self.turn == globals.TURN_PLAYER):
                print("Player Monster Hand: " + self.player.monster.hand.toString())
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
                        selected_card_indexes = self.selectCards(self.player, globals.MECHANIC_DRAW)
                        selected_cards = []
                        for index_card in range(globals.NUM_CARDS_HAND):
                            if(index_card in selected_card_indexes):
                                selected_cards.append(self.player.monster.hand.cards[index_card])
                                self.player.monster.dealCard(index_card)
                        print("Player Monster Hand: " + self.player.monster.hand.toString())
                    ### PLAYER CASHOUT ###
                    case globals.ACTION_CASHOUT:
                        player_hand_rank = self.player.monster.handRank()
                        print(globals.LUT_HAND_RANK[player_hand_rank])
                        # clear locks on cards in hand
                        for index_hand in range(globals.NUM_CARDS_HAND):
                            self.player.monster.hand.cards[index_hand].is_locked = False
                        # initialize mechanic multipliers/quantities
                        self.modifiers.set(player_hand_rank)
                        # apply battle mechanics
                        if(self.modifiers.multiplier_attack != 0):
                            damage = self.attack(self.player.monster, self.opponent.monster, self.modifiers.multiplier_attack)
                            print("Dealt " + str(damage) + " damage")
                            if(self.opponent.monster.hitpoints_current <= 0):
                                print("Opponent monster defeated")
                            else:
                                print("Opponent monster has " + self.opponent.monster.toStringHitpoints() + " hitpoints left")
                        if(self.modifiers.multiplier_healing != 0):
                            healing = self.heal(self.player.monster, self.modifiers.multiplier_healing)
                            print("Healed " + str(healing) + " damage")
                            print("Player monster has " + self.player.monster.toStringHitpoints() + " hitpoints left")
                        if(self.modifiers.quantity_force_draw_random != 0):
                            card_indexes_force_draw = self.forceDrawRandom(self.opponent.monster, self.modifiers.quantity_force_draw_random)
                            print("Forced draw at index(es): " + str(card_indexes_force_draw))
                            pass
                        if(self.modifiers.quantity_force_draw_target != 0):
                            pass
                        if(self.modifiers.quantity_lock_random != 0):
                            pass
                        if(self.modifiers.quantity_lock_target != 0):
                            pass
                        if(self.modifiers.quantity_hold != 0):
                            pass
                    ### PLAYER ACTION ERROR ###
                    case globals.ACTION_ERROR:
                        print("error: invalid player action")
                self.turn = globals.TURN_OPPONENT

            ### OPPONENT'S TURN ###
            elif(self.turn == globals.TURN_OPPONENT):
                print("Opponent Monster Hand: " + self.opponent.monster.hand.toString())
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
        print("Battle finished")

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
    # returns the indexes of the cards that were drawn
    def forceDrawRandom(self, monster_defender : Monster, quantity : int) -> None:
        cards_indexes_already_chosen = [] # this keeps track of what cards have already been chosen so we don't choose at the same index twice
        # we only can draw as many cards as are free (not locked or held)
        num_draws = quantity
        num_free_cards = monster_defender.hand.numFree()
        if(num_free_cards < quantity):
            num_draws = num_free_cards
        for index_draw in range(num_draws):
            index_card_draw_is_valid = False
            while(not index_card_draw_is_valid):
                index_card_draw = random.randint(0, globals.NUM_CARDS_HAND - 1)
                if(not monster_defender.hand.cards[index_card_draw].is_locked and
                   not index_card_draw in cards_indexes_already_chosen):
                    index_card_draw_is_valid = True
                    cards_indexes_already_chosen.append(index_card_draw)
            monster_defender.dealCard(index_card_draw)
        return cards_indexes_already_chosen
    
    # prompt UI to select quanity of monster_defender's hand cards redraw them
    def forceDrawTarget(self, monster_defender : Monster, quantity : int) -> None:
        return
    
    # randomly select quantity of monster_defender's hand cards and mark them as locked
    # returns the indexes of the cards that were locked
    def lockRandom(self, monster_defender : Monster, quantity : int) -> None:
        cards_indexes_already_chosen = [] # this keeps track of what cards have already been chosen so we don't choose again at the same index twice
        # we only can lock as many cards as are free (not already locked or held)
        num_locks = quantity
        num_free_cards = monster_defender.hand.numFree()
        if(num_free_cards < quantity):
            num_locks = num_free_cards
        for index_lock in range(num_locks):
            index_card_lock_is_valid = False
            while(not index_card_lock_is_valid):
                index_card_lock = random.randint(0, globals.NUM_CARDS_HAND - 1)
                if(not monster_defender.hand.cards[index_card_lock].is_locked and
                   not index_card_lock in cards_indexes_already_chosen):
                    index_card_lock_is_valid = True
                    cards_indexes_already_chosen.append(index_card_lock)
            monster_defender.hand.cards[index_card_lock].is_locked = True
        return cards_indexes_already_chosen
    
    # prompt UI to select quantity of monster_defender's hand cards and mark them as locked
    def lockTarget(self, monster_defender : Monster, quantity : int) -> None:
        return
    
    # prompt UI to select quantity of monster_holder's hand cards and mark them as held
    def holdPlayer(self, monster_holder : Monster, quantity : int) -> None:

        return
    
    # AI selects quantity of monster_holder's hand cards and mark them as held
    def holdOpponent(self, monster_holder : Monster, quantity : int) -> None:
        return

    # prompts UI to select from specified player's cards, then returns an array of indexes
    # checks for whether selection is valid depends on selected mechanic
    def selectCards(self, player : Player, mechanic : int) -> list[int]:
        is_valid_selection = False
        selected_card_indexes = []
        while(not is_valid_selection):
            selected_card_indexes = UI.battleSelectPlayerCards()
            is_valid_selection = True
            for index in selected_card_indexes:
                match mechanic:
                    case globals.MECHANIC_DRAW:
                        # cannot draw a card that is locked
                        if(index < 0 or index >= globals.NUM_CARDS_HAND or player.monster.hand.cards[index].is_locked):
                            is_valid_selection = False
                            print("invalid selection")
                    case globals.MECHANIC_FORCE_DRAW:
                        # cannot force draw a card that is locked
                        if(index < 0 or index >= globals.NUM_CARDS_HAND or player.monster.hand.cards[index].is_locked):
                            is_valid_selection = False
                            print("invalid selection")
                    case globals.MECHANIC_LOCK:
                        # cannot lock a card that is already locked
                        if(index < 0 or index >= globals.NUM_CARDS_HAND or player.monster.hand.cards[index].is_locked):
                            is_valid_selection = False
                            print("invalid selection")
                    case globals.MECHANIC_HOLD:
                        # can hold any card
                        if(index < 0 or index >= globals.NUM_CARDS_HAND):
                            is_valid_selection = False
                            print("invalid selection")
        return selected_card_indexes

    @staticmethod
    def opponentSelectAction() -> int:
        action = random.choice([globals.ACTION_DRAW, globals.ACTION_CASHOUT])
        return action

    # returns true if the battle is over because one player has no more monsters with HP, false otherwise
    def isFinished(self) -> bool:
        if(self.player.isAlive() and self.opponent.isAlive()):
            return False
        return True

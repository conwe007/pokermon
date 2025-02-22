import globals

class Modifiers:
    def __init__(self) -> None:
        self.multiplier_attack = 0
        self.multiplier_healing = 0
        self.quantity_force_draw_random = 0
        self.quantity_force_draw_target = 0
        self.quantity_lock_random = 0
        self.quantity_lock_target = 0
        self.quantity_hold = 0
        return
    
    # sets each modifier value based on the hand rank
    def set(self, hand_rank : int) -> None:
        match hand_rank:
            case globals.HAND_RANK_HIGH_CARD:
                self.multiplier_attack = globals.MULTIPLIER_HIGH_CARD_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_HIGH_CARD_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_HIGH_CARD_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_HIGH_CARD_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_HIGH_CARD_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_HIGH_CARD_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_HIGH_CARD_HOLD
            case globals.HAND_RANK_PAIR:
                self.multiplier_attack = globals.MULTIPLIER_PAIR_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_PAIR_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_PAIR_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_PAIR_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_PAIR_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_PAIR_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_PAIR_HOLD
            case globals.HAND_RANK_TWO_PAIR:
                self.multiplier_attack = globals.MULTIPLIER_TWO_PAIR_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_TWO_PAIR_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_TWO_PAIR_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_TWO_PAIR_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_TWO_PAIR_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_TWO_PAIR_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_TWO_PAIR_HOLD
            case globals.HAND_RANK_THREE_OF_A_KIND:
                self.multiplier_attack = globals.MULTIPLIER_THREE_OF_A_KIND_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_THREE_OF_A_KIND_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_THREE_OF_A_KIND_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_THREE_OF_A_KIND_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_THREE_OF_A_KIND_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_THREE_OF_A_KIND_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_THREE_OF_A_KIND_HOLD
            case globals.HAND_RANK_STRAIGHT:
                self.multiplier_attack = globals.MULTIPLIER_STRAIGHT_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_STRAIGHT_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_STRAIGHT_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_STRAIGHT_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_STRAIGHT_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_STRAIGHT_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_STRAIGHT_HOLD
            case globals.HAND_RANK_FLUSH:
                self.multiplier_attack = globals.MULTIPLIER_FLUSH_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_FLUSH_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_FLUSH_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_FLUSH_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_FLUSH_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_FLUSH_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_FLUSH_HOLD
            case globals.HAND_RANK_FULL_HOUSE:
                self.multiplier_attack = globals.MULTIPLIER_FULL_HOUSE_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_FULL_HOUSE_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_FULL_HOUSE_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_FULL_HOUSE_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_FULL_HOUSE_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_FULL_HOUSE_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_FULL_HOUSE_HOLD
            case globals.HAND_RANK_FOUR_OF_A_KIND:
                self.multiplier_attack = globals.MULTIPLIER_FOUR_OF_A_KIND_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_FOUR_OF_A_KIND_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_FOUR_OF_A_KIND_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_FOUR_OF_A_KIND_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_FOUR_OF_A_KIND_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_FOUR_OF_A_KIND_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_FOUR_OF_A_KIND_HOLD
            case globals.HAND_RANK_STRAIGHT_FLUSH:
                self.multiplier_attack = globals.MULTIPLIER_STRAIGHT_FLUSH_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_STRAIGHT_FLUSH_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_STRAIGHT_FLUSH_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_STRAIGHT_FLUSH_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_STRAIGHT_FLUSH_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_STRAIGHT_FLUSH_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_STRAIGHT_FLUSH_HOLD
            case globals.HAND_RANK_FIVE_OF_A_KIND:
                self.multiplier_attack = globals.MULTIPLIER_FIVE_OF_A_KIND_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_FIVE_OF_A_KIND_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_FIVE_OF_A_KIND_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_FIVE_OF_A_KIND_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_FIVE_OF_A_KIND_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_FIVE_OF_A_KIND_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_FIVE_OF_A_KIND_HOLD
            case globals.HAND_RANK_FLUSH_HOUSE:
                self.multiplier_attack = globals.MULTIPLIER_FLUSH_HOUSE_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_FLUSH_HOUSE_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_FLUSH_HOUSE_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_FLUSH_HOUSE_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_FLUSH_HOUSE_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_FLUSH_HOUSE_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_FLUSH_HOUSE_HOLD
            case globals.HAND_RANK_FLUSH_FIVE:
                self.multiplier_attack = globals.MULTIPLIER_FLUSH_FIVE_ATTACK
                self.multiplier_healing = globals.MULTIPLIER_FLUSH_FIVE_HEALING
                self.quantity_force_draw_random = globals.QUANTITY_FLUSH_FIVE_FORCE_DRAW_RANDOM
                self.quantity_force_draw_target = globals.QUANTITY_FLUSH_FIVE_FORCE_DRAW_TARGET
                self.quantity_lock_random = globals.QUANTITY_FLUSH_FIVE_LOCK_RANDOM
                self.quantity_lock_target = globals.QUANTITY_FLUSH_FIVE_LOCK_TARGET
                self.quantity_hold = globals.QUANTITY_FLUSH_FIVE_HOLD
            case globals.HAND_RANK_ERROR:
                self.multiplier_attack = 0
                self.multiplier_healing = 0
                self.quantity_force_draw_random = 0
                self.quantity_force_draw_target = 0
                self.quantity_lock_random = 0
                self.quantity_lock_target = 0
                self.quantity_hold = 0
        return
    
    # reset all modifiers to 0
    def reset(self) -> None:
        self.multiplier_attack = 0
        self.multiplier_healing = 0
        self.quantity_force_draw_random = 0
        self.quantity_force_draw_target = 0
        self.quantity_lock_random = 0
        self.quantity_lock_target = 0
        self.quantity_hold = 0
        return
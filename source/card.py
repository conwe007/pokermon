import globals

class Card:
    def __init__(self, value, suit):
        if(isinstance(value, str)):
            self.value = globals.LUT_VALUE.index(value)
        else:
            self.value = value
        
        if(isinstance(suit, str)):
            self.suit = globals.LUT_SUIT.index(suit)
        else:
            self.suit = suit

    def getCardCode(self):
        return self.suit * globals.NUM_VALUES + self.value
    
    # arg - 0-51 card code
    # return - tuple (value, suit)
    @staticmethod
    def getCardFromCode(card_code):
        value = card_code % globals.NUM_VALUES
        suit = card_code // globals.NUM_VALUES
        return [value, suit]
    
    # arg - 0-51 card code
    # return - 0-12 value
    @staticmethod
    def getCardValueFromCode(card_code):
        value = card_code % globals.NUM_VALUES
        return value
    
    # arg - 0-51 card code
    # return - 0-3 suit
    @staticmethod
    def getCardSuitFromCode(card_code):
        suit = card_code // globals.NUM_VALUES
        return suit

    # arg - card text code (ex. Ah, Kd, 5s)
    # return - tuple (value, suit)
    @staticmethod
    def getCardFromText(card_text):
        if len(card_text) != 2:
            return [-1, -1]
        
        match card_text[0]:
            case "A":
                value = 0
            case "2":
                value = 1
            case "3":
                value = 2
            case "4":
                value = 3
            case "5":
                value = 4
            case "6":
                value = 5
            case "7":
                value = 6
            case "8":
                value = 7
            case "9":
                value = 8
            case "T":
                value = 9
            case "J":
                value = 10
            case "Q":
                value = 11
            case "K":
                value = 12
            case _:
                value = -1
        
        match card_text[1]:
            case "c":
                suit = 0
            case "d":
                suit = 1
            case "s":
                suit = 2
            case "h":
                suit = 3
            case _:
                suit = -1
        
        return [value, suit]
    
    # arg - card text code (ex. Ah, Kd, 5s)
    # return - 0-12 value
    @staticmethod
    def getCardValueFromText(card_text):
        if len(card_text) != 2:
            return -1
        
        match card_text[0]:
            case "A":
                value = 0
            case "2":
                value = 1
            case "3":
                value = 2
            case "4":
                value = 3
            case "5":
                value = 4
            case "6":
                value = 5
            case "7":
                value = 6
            case "8":
                value = 7
            case "9":
                value = 8
            case "T":
                value = 9
            case "J":
                value = 10
            case "Q":
                value = 11
            case "K":
                value = 12
            case _:
                value = -1
        
        return value

    # arg - card text code (ex. Ah, Kd, 5s)
    # return - suit
    @staticmethod
    def getCardSuitFromText(card_text):
        if len(card_text) != 2:
            return [-1, -1]
        
        match card_text[1]:
            case "c":
                suit = 0
            case "d":
                suit = 1
            case "s":
                suit = 2
            case "h":
                suit = 3
            case _:
                suit = -1
        
        return suit

    def toString(self):
        return globals.LUT_VALUE[self.value] + globals.LUT_SUIT[self.suit]

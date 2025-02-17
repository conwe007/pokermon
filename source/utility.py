import globals

def generateCardCodes():
    for suit in range(globals.NUM_SUITS):
        for value in range(globals.NUM_VALUES):
            print(value, suit, suit * globals.NUM_VALUES + value)

def getCardCode(value, suit):
    return suit * globals.NUM_VALUES + value

def getCard(card_code):
    value = card_code % globals.NUM_VALUES
    suit = card_code // globals.NUM_VALUES
    return [value, suit]

import globals

class UI:
    def __init__(self):
        return
    
    @staticmethod
    def battleSelectAction():
        action = input("action: ")
        match action:
            case "draw":
                return globals.ACTION_DRAW
            case "special":
                return globals.ACTION_CASHOUT
            case _:
                return globals.ACTION_ERROR
        return

    # returns array of indicies of selected cards
    @staticmethod
    def battleSelectPlayerCards():
        cards_index_input = input("enter card indicies [0-4]: ")
        cards_index_str = cards_index_input.split()
        cards_index_int = []
        for index in range(len(cards_index_str)):
            cards_index_int.append(int(cards_index_str[index]))
        return cards_index_int


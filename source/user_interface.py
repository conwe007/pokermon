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

    @staticmethod
    def battleSelectPlayerCards():
        
        return

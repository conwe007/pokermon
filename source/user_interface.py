import globals

class UI:
    def __init__(self):

        return
    
    def battleSelectAction():
        action = input("action: ")

        match action:
            case "attack":
                return globals.ACTION_ATTACK
            case "defend":
                return globals.ACTION_DEFEND
            case "draw":
                return globals.ACTION_DRAW
            case "special":
                return globals.ACTION_SPECIAL
            case "switch":
                return globals.ACTION_SWITCH
            case _:
                return globals.ACTION_ERROR
        return
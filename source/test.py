# test file containing tests of functions in other classes
import json
import globals
from battle import Battle
from card import Card
from deck import Deck
# from game import Game
from hand import Hand
from monster import Monster
from player import Player

with open("./assets/monsters/pokerdex.json", mode="r") as pokerdex:
    pokerdex_data = pokerdex.read()
    pokerdex_json = json.loads(pokerdex_data)
    m1 = Monster(pokerdex_json, 0)
    m2 = Monster(pokerdex_json, 1)

p1 = Player()
p1.setMonster(m1)
p2 = Player()
p2.setMonster(m2)
b = Battle(p1, p2)
b.run()

# m1.dealHand()
# m1.hand.cards[1].is_locked = True
# m1.hand.cards[3].is_held = True
# print(m1.toStringHand())
# m1.dealHand()
# print(m1.toStringHand())

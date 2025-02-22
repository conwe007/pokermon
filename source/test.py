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
p1.addMonster(m1)
p2 = Player()
p2.addMonster(m2)
b = Battle(p1, p2)
b.run()


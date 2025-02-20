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

# with open("./assets/monsters/pokerdex.json", mode="r") as pokerdex:
#     pokerdex_data = pokerdex.read()
#     pokerdex_json = json.loads(pokerdex_data)
#     m1 = Monster(pokerdex_json, 0)
#     print(m.toString())

# q = m.save()
# print(q)

# with open("deck_text.txt", newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',',)
#     deck_text = spamreader.__next__()

# d = Deck()
# d.load(deck_text)

# h = Hand()
# ranks = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# for i in range (10000):
#     d.shuffle()
#     for index_hand in range(len(h.cards)):
#         h.cards[index_hand] = d.deal()
#     ranks[h.evaluate()] += 1

# print(ranks)

# with open("./assets/monsters/pokerdex.json", mode="r") as pokerdex:
#     pokerdex_data = pokerdex.read()
#     pokerdex_json = json.loads(pokerdex_data)
#     m1 = Monster(pokerdex_json, 0)
#     m2 = Monster(pokerdex_json, 1)

# p1 = Player()
# # print(p1.toString())
# p2 = Player()
# # print(p1.hasLivingMonsters())
# p1.addMonster(m1)
# # print(p1.toString())
# # print(p1.hasLivingMonsters())
# p2.addMonster(m2)
# # print(p2.toString())

# b = Battle(p1, p2)
# b.run()
d = Deck()
h = Hand()
d.shuffle()
for index_hand in range(len(h.cards)):
    h.cards[index_hand] = d.deal()
print(h.toString())
print(h.value(0))


from card import Card
from barrel import Barrel
from player import MachinePlayer, MeatBag


# 1. Generate list of barrels
# 2. Get users and their types
# 3. Play:
#         loop while all the barrels are not used or user not won
#         take new Barrel
#         ask user strike out number in his card
# check the answer, check if number exists, return result

# generating pool of barrels
pool = {}
for i in range(1, 91):
    barrel = Barrel()
    barrel.set_value(i)
    pool[i] = barrel

users_count = input("Please enter amount of players: ")
# print(pool)

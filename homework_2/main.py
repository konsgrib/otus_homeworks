from classes.card import Card
from classes.barrel import Barrel
from classes.player import MachinePlayer, MeatBag


def main():
    player = MachinePlayer("Bender")
    card = Card(player.name)
    barrel = Barrel()
    barrel.set_value(10)

    print(player)
    print(barrel)
    print(card)
    player.move(barrel, card)
    print(card)


if __name__ == "__main__":
    main()

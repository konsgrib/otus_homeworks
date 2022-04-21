from random import shuffle
from time import sleep

from classes.card import Card
from classes.barrel import Barrel
from classes.player import MachinePlayer, MeatBag


# generating pool of barrels
def pool_of_barrels() -> list:
    pool = {}
    rands = [i for i in range(1, 91)]
    shuffle(rands)
    for i in range(1, len(rands)):
        barrel = Barrel()
        barrel.set_value(rands[i])
        pool[i] = barrel
    return pool


def create_users_and_cards():
    players = []
    while True:
        username = input("Input Player name or hit Enter to start the game: ")
        if username == "":
            return players

        type = input("Is player human? y/n [Y] ") or "y"
        if type == "y":
            player = MeatBag(username)
        else:
            player = MachinePlayer(username)
        # Generating and assigning a card for each new user.
        card = Card(player.name)
        card.generate_fields()
        player.card = card
        players.append(player)


def play():
    barrels = pool_of_barrels()
    users = create_users_and_cards()

    i = 0
    j = 1
    while j < len(barrels):

        user = users[i]
        bar = barrels[j]
        # User move
        print(user.card)
        print(bar)
        if isinstance(user, MeatBag):
            move = input("Cross out number? y/n: [Y]") or "y"
            if (move == "y" and user.move(bar, user.card)) or (
                move == "n" and not user.move(bar, user.card)
            ):
                barrels.pop(
                    j
                )  # Removing barrel from list if it was used to cross out the number
                print("OK")
            else:
                print(f"User, {user.name} lose!!!")
                users.pop(i)
        else:
            # Robot type of user will always choose the right step
            # To do this he'll use a Barrel.check_if_exists methog first
            # added just to do some visible delay between robot's steps
            user.move(bar, user.card)
            sleep(1)
        # Choose next user
        i += 1
        j += 1
        # Dropping counters if not all cards are closed
        #  and users are still in the game
        if i > len(users) - 1:
            i = 0
        if j > len(barrels) - 1:
            j = 1


if __name__ == "__main__":
    play()

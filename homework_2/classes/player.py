from time import sleep
from .barrel import Barrel
from .card import Card


class GenericPlayer:
    def __init__(self, name):
        self.name = name
        self.card = None
        self.greeting()

    def greeting(self):
        pass

    def __str__(self) -> str:
        return f"{self.name}"


class MachinePlayer(GenericPlayer):
    def move(self, barrel: Barrel, card: Card):
        if card.check_if_exists(barrel.number):
            sleep(1)
            print(f"{self.name}: Yeah, lucky me!")
            return card.replace_if_exists(barrel.number)
        sleep(1)
        print(f"{self.name}: I am not going to make a bet here!!!")
        return False

    def greeting(self):
        return f"{self.name}: Hello, I am a robot!"


class MeatBag(GenericPlayer):
    def move(self, barrel: Barrel, card: Card):
        return card.replace_if_exists(barrel.number)

    def greeting(self):
        return f"{self.name}: Hello, I am a meat bag!"

from barrel import Barrel
from card import Card


class GenericPlayer:
    def __init__(self, name):
        self.name = name
        self._games_won = 0
        self._total_played = 0

    def win(self):
        self._games_won += 1

    def play(self):
        self._total_played += 1

    @property
    def games_won(self):
        return self._games_won

    @property
    def total_played(self):
        return self._total_played

    def __str__(self) -> str:
        return f"{self.name} total played: {self.total_played}, total won: {self.games_won}"


class MachinePlayer(GenericPlayer):
    def move(self, barrel: Barrel, card: Card):
        if card.check_if_exists(barrel.number):
            return card.replace_if_exists(barrel.number)
        print("I am not going to make a bet here!!!")
        return False


class MeatBag(GenericPlayer):
    def move(self, barrel: Barrel, card: Card):
        return card.replace_if_exists(barrel.number)

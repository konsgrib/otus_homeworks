class Player:
    def __init__(self, name, type):
        self.name = name
        self.type = type
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

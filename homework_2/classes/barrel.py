class Barrel:
    def __init__(self):
        self._number = None
        self.used = False

    def __str__(self):
        return f"Number: {self.number}"

    def __repr__(self) -> str:
        return f"Number: {self.number}, used: {self.used}"

    @property
    def number(self):
        return self._number

    def set_value(self, value: int):
        if isinstance(value, int) and (0 < value < 91):
            self._number = value
            return True
        else:
            print("Incorrect value set, try again")
            return False

    def use(self):
        self.used = True

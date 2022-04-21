from random import randint, sample, shuffle


class Card:
    def __init__(self, username):
        self.username = username
        self.fields = self.generate_fields()

    def generate_fields(self):
        field = {}
        rands = [i for i in range(1, 91)]
        shuffle(rands)
        for x in range(3):
            line = []
            items = sample(range(9), 5)

            for i in range(9):
                line.append(rands.pop())

            line = sorted(line)
            for i in range(len(line)):
                if i in items:
                    line[i] = " "
            field[x] = line
        return field

    def _build_str(self):
        half_header = "-" * int((64 - len(self.username)) / 2)
        header = f"\n{half_header} {self.username} {half_header}\n"
        footer = "-" * 66
        out = header
        for i in self.fields:
            line = "\t".join(str(l) for l in self.fields[i])
            out += f"\n{line}\n"
        out += f"\n{footer}\n"
        return out

    def replace_if_exists(self, value) -> bool:
        for i in self.fields:
            for x in range(len(self.fields[i])):
                if self.fields[i][x] == value:
                    self.fields[i][x] = "-"
                    print(f"Number {value} exists at y: {i}, x: {x}!")
                    if (
                        self.fields[i].count("-") == 5
                    ):  # Game over if user has crossed out one line
                        print(f"********The winner is: {self.username}!!!*********")
                        exit()
                    return True
        return False

    def check_if_exists(self, value) -> bool:
        for i in self.fields:
            for x in range(len(self.fields[i])):
                if self.fields[i][x] == value:
                    return True
        return False

    def __str__(self):
        return self._build_str()

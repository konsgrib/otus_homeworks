from random import randint, sample


class Card:
    def __init__(self, username):
        self.username = username
        self.fields = self.generate_fields()

    def generate_fields(self):
        field = {}

        for x in range(3):
            items = sample(range(9), 5)
            line = sorted([randint(1, 90) for _ in range(9)])
            new_line = []
            for i in range(9):
                if i in items:
                    new_line.append(line[i])
                else:
                    new_line.append(" ")
            field[x] = new_line
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
                    print(f"Bingo! number {value} exists!")
                    return True
        print(f"Woops! The number {value} does not exists!")
        return False

    def __str__(self):
        return self._build_str()


def main():
    card = Card("Vasily Pupkin")
    print(card)
    card.replace_if_exists(10)
    print(card)


if __name__ == "__main__":
    main()

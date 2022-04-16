from random import randint, sample, choice


class Card:
    def __init__(self):
        self.fields = self.generate_fields()

    def generate_fields(self):
        field = {}

        for x in range(3):
            items = sample(range(9), 5)
            line = [randint(1, 90) for _ in range(9)]
            new_line = []
            for i in range(9):
                if i in items:
                    new_line.append(line[i])
                else:
                    new_line.append("_")
            field[x] = new_line
        return field

    def __str__(self):
        return f"{self.fields}"


def main():
    card = Card()
    print(card)
    print(card)


if __name__ == "__main__":
    main()

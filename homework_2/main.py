from classes.card import Card


def main():
    card = Card("Vasily Pupkin")
    print(card)
    card.replace_if_exists(10)
    print(card)


if __name__ == "__main__":
    main()

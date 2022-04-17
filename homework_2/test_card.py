from classes.card import Card
import pytest


def test_create_card():
    card = Card("User")
    assert isinstance(card, Card)


def test_generate_fields():
    card = Card("User")
    field = card.generate_fields()
    assert isinstance(field, dict)


def test_dict_contains_tree_lists():
    card = Card("User")
    field = card.generate_fields()
    assert len(field) == 3


def test_each_list_of_dict_has_length_9():
    card = Card("User")
    field = card.generate_fields()
    for i in field:
        assert len(field[i]) == 9


def test_each_list_of_dict_contains_five_digits():
    card = Card("User")
    field = card.generate_fields()
    for i in field:
        assert field[i].count(" ") == 4

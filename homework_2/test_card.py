from classes.card import Card
import pytest


def test_create_card():
    card = Card()
    assert isinstance(card, Card)


def test_generate_fields():
    card = Card()
    field = card.generate_fields()
    assert isinstance(field, dict)


def test_dict_contains_tree_lists():
    card = Card()
    field = card.generate_fields()
    assert len(field) == 3


def test_each_list_of_dict_contains_five_digits():
    card = Card()
    field = card.generate_fields()
    for i in field:
        assert len(field[i]) == 9

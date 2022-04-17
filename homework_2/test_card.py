from unittest import mock
from classes.card import Card
from pytest import fixture, mark, param, raises
from mock import patch, Mock


@fixture
def card_instance() -> Card:
    card = Card("TestUser")
    return card


class TestCard:
    def test_create_card(self, card_instance):
        assert isinstance(card_instance, Card)

    def test_generate_fields(self, card_instance):
        field = card_instance.generate_fields()
        assert isinstance(field, dict)

    def test_dict_contains_tree_lists(self, card_instance):
        field = card_instance.generate_fields()
        assert len(field) == 3

    def test_each_list_of_dict_has_length_9(self, card_instance):
        field = card_instance.generate_fields()
        for i in field:
            assert len(field[i]) == 9

    def test_each_list_of_dict_contains_four_spaces(self, card_instance):
        field = card_instance.generate_fields()
        for i in field:
            assert field[i].count(" ") == 4


@patch.object(Card, "generate_fields")
def test_replace_if_exists(mock_generate_fields):
    mock_generate_fields.return_value = {
        0: ["_", 83, "_", "_", 5, 20, "_", 58, "_"],
        1: ["_", 34, 87, "_", 79, "_", 8, 6, "_"],
        2: ["_", 78, "_", "_", 78, 20, "_", 58, "_"],
    }
    card = Card("TestUser")
    res = card.replace_if_exists(5)
    assert res == True
    res = card.replace_if_exists(7)
    assert res == False

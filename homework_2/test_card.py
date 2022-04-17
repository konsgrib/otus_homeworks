from classes.card import Card
from pytest import fixture


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

    def test_replace_if_exists(self, card_instance):
        res = card_instance.replace_if_exists(5)
        assert isinstance(res, bool)

from unittest import mock
from classes.player import MachinePlayer, MeatBag
from classes.barrel import Barrel
from classes.card import Card
from pytest import fixture, mark, param, raises
from mock import patch, Mock


@fixture
@patch.object(Card, "generate_fields")
def test_barrel_instance(mock_generate_fields):
    mock_generate_fields.return_value = {
        0: ["_", 83, "_", "_", 5, 20, "_", 58, "_"],
        1: ["_", 34, 87, "_", 79, "_", 8, 6, "_"],
        2: ["_", 78, "_", "_", 78, 20, "_", 58, "_"],
    }
    card = Card("TestUser")
    card.generate_fields()
    return card


@fixture
def player_instance() -> MeatBag:
    player = MeatBag("TestUser")
    return player


@fixture
def barrel_instance() -> Barrel:
    barrel = Barrel()
    barrel.set_value(87)
    return barrel


@fixture
def virtual_player_instance() -> MachinePlayer:
    virtual_player = MachinePlayer("TestUser")
    return virtual_player


class TestMeatBag:
    def test_greeting(self, player_instance):
        assert (
            player_instance.greeting()
            == f"{player_instance.name}: Hello, I am a meat bag!"
        )

    def test_move(self, player_instance, test_barrel_instance, barrel_instance):
        assert player_instance.move(barrel_instance, test_barrel_instance) == True


class TestMachinePlayer:
    def test_virt_greeting(self, virtual_player_instance):
        assert (
            virtual_player_instance.greeting()
            == f"{virtual_player_instance.name}: Hello, I am a robot!"
        )

    def test_virt_move(
        self, virtual_player_instance, test_barrel_instance, barrel_instance
    ):
        result = virtual_player_instance.move(barrel_instance, test_barrel_instance)
        assert result == True

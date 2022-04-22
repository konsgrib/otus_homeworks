from unittest import mock
from classes.card import Card
from pytest import fixture, mark, param, raises
from mock import patch, Mock

from classes.barrel import Barrel


@fixture
def barrel_instance() -> Barrel:
    barrel = Barrel()
    return barrel


class TestBarrel:
    def test_create_barrel(self, barrel_instance):
        assert isinstance(barrel_instance, Barrel)

    def test_set_incorrect_value(self, barrel_instance):
        assert barrel_instance.set_value(99) == False
        assert barrel_instance.set_value("some_string") == False
        assert barrel_instance.set_value(19) == True

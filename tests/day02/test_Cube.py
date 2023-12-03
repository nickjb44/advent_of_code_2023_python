import pytest

from src.day02.models.Cube import Cube, Color


def test_cube_initialization():
    # Testing initialization of Cube
    cube = Cube(Color.RED, 4)

    assert cube.color == Color.RED
    assert cube.count == 4


def test_cube_color_enum():
    # Testing the Color Enum values
    assert Color.RED.value == 1
    assert Color.GREEN.value == 2
    assert Color.BLUE.value == 3


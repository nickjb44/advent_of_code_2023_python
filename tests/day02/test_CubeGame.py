import pytest
from src.day02.models.Cube import Color, Cube
from src.day02.models.CubeBag import CubeBag
from src.day02.models.CubeGame import CubeGame


# Assuming a helper class for Round
class Round:
    def __init__(self, color_to_cube):
        self.color_to_cube = color_to_cube


@pytest.fixture
def sample_rounds():
    return [
        Round({Color.RED: Cube(Color.RED, 3), Color.GREEN: Cube(Color.GREEN, 2)}),
        Round({Color.RED: Cube(Color.RED, 4), Color.GREEN: Cube(Color.GREEN, 5)})
    ]


@pytest.fixture
def sample_cube_bag():
    return CubeBag([
        Cube(Color.RED, 6),
        Cube(Color.GREEN, 7)
    ])


def test_cube_game_initialization(sample_rounds):
    game = CubeGame(sample_rounds, game_id=1)
    assert game.game_id == 1
    assert game.rounds == sample_rounds


def test_set_cube_bag(sample_rounds, sample_cube_bag):
    game = CubeGame(sample_rounds).set_cube_bag(sample_cube_bag)
    assert game.cube_bag == sample_cube_bag


def test_get_fewest_cubes_to_be_valid(sample_rounds, sample_cube_bag):
    game = CubeGame(sample_rounds).set_cube_bag(sample_cube_bag)
    result = game.get_fewest_cubes_to_be_valid()
    assert result.color_to_cube[Color.RED].count == 4
    assert result.color_to_cube[Color.GREEN].count == 5

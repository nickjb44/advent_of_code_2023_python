import pytest

from src.day02.models.Cube import Color, Cube
from src.day02.models.CubeGameLine import CubeGameLine, chunk_to_n_of_color
from src.day02.models.CubeRound import CubeRound


def test_get_game_id():
    content = "Game 1: afejof"
    line = CubeGameLine(content)
    assert line.get_game_id() == "1"


def test_get_game_id():
    content = "Game 123: afejof"
    line = CubeGameLine(content)
    assert line.get_game_id() == "123"


def test_get_game_id():
    content = "Game a: afejof"
    line = CubeGameLine(content)
    with pytest.raises(ValueError):
        line.get_game_id()


def test_get_chunks():
    content = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    line = CubeGameLine(content)
    expected = [
        ' 3 blue, 4 red',
        ' 1 red, 2 green, 6 blue',
        ' 2 green'
    ]
    assert line.get_chunks() == expected


def test_chunk_to_color():
    chunk = "10 red, 20 blue, 30 green"

    n_red = chunk_to_n_of_color(Color.RED.name.lower(), chunk)
    n_green = chunk_to_n_of_color(Color.GREEN.name.lower(), chunk)
    n_blue = chunk_to_n_of_color(Color.BLUE.name.lower(), chunk)

    assert n_red == '10'
    assert n_blue == '20'
    assert n_green == '30'


def test_chunk_to_color():
    chunk = "10 blue, 30 green"

    n_red = chunk_to_n_of_color(Color.RED.name.lower(), chunk)

    assert n_red == "0"


def test_chunk_to_round():
    chunk = "10 red, 20 blue, 30 green"

    cube_round = CubeGameLine.chunk_to_round(chunk)

    assert isinstance(cube_round, CubeRound)

    red_cube = cube_round.color_to_cube[Color.RED]
    assert isinstance(red_cube, Cube)
    assert red_cube.color == Color.RED
    assert red_cube.count == 10

    blue_cube = cube_round.color_to_cube[Color.BLUE]
    assert isinstance(blue_cube, Cube)
    assert blue_cube.color == Color.BLUE
    assert blue_cube.count == 20

    green_cube = cube_round.color_to_cube[Color.GREEN]
    assert isinstance(green_cube, Cube)
    assert green_cube.color == Color.GREEN
    assert green_cube.count == 30


def test_to_round_list():
    content = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game_line = CubeGameLine(content)

    round_list = game_line.to_round_list()

    # Assertions to check if round_list is correctly formed
    assert isinstance(round_list, list)
    assert len(round_list) == 3  # There are 3 rounds in the content

    # Testing the first round
    first_round = round_list[0]
    assert isinstance(first_round, CubeRound)
    first_round = round_list[1]
    assert isinstance(first_round, CubeRound)
    first_round = round_list[2]
    assert isinstance(first_round, CubeRound)
    # too lazy to test each cube

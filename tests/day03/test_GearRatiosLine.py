from re import Match

import pytest

from src.day03.models.GearRatiosLine import GearRatiosLine


@pytest.fixture
def sample_line_one_number():
    return '..23..'


@pytest.fixture
def sample_line_two_numbers():
    return '..23..10'


@pytest.fixture
def sample_line_just_one_symbol():
    return '..#..'


@pytest.fixture
def sample_line_two_symbols():
    return '..#..@.'


@pytest.fixture
def sample_line_two_symbols_and_a_number():
    return '..#..@10'


def test_match_schematic_numbers_one(sample_line_one_number):
    line = GearRatiosLine(sample_line_one_number, 1)
    matches = list(line.match_schematic_numbers())
    assert len(matches) == 1

    first_match: Match = matches[0]
    assert first_match.group() == "23"
    assert first_match.start() == 2
    assert first_match.end() == 4


def test_match_schematic_numbers_two(sample_line_two_numbers):
    line = GearRatiosLine(sample_line_two_numbers, 1)
    matches = list(line.match_schematic_numbers())
    assert len(matches) == 2

    first_match: Match = matches[0]
    assert first_match.group() == "23"
    assert first_match.start() == 2
    assert first_match.end() == 4

    second_match: Match = matches[1]
    assert second_match.group() == "10"
    assert second_match.start() == 6
    assert second_match.end() == 8

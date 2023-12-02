import os

import pytest
from unittest.mock import mock_open, patch

import src.day01.part2 as solution


# Test for read_lines function
def test_read_lines():
    mock_file_content = "line1\nline2\nline3"
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        result = solution.read_lines("dummy_path")
    assert result == ["line1\n", "line2\n", "line3"]


def test_given_example():
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    # Construct the relative path to the input file
    file_path = os.path.join(script_dir, "input", "example_2.txt")
    answer = solution.calculate_calibration_total(
        solution.read_lines(file_path)
    )
    assert answer == 281

import os
from unittest.mock import mock_open, patch

import src.day03.part1 as solution


def test_read_lines():
    mock_file_content = "line1\nline2\nline3"
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        result = solution.read_lines("dummy_path")
    assert result == ["line1\n", "line2\n", "line3"]


def test_given_example():
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    # Construct the relative path to the input file
    file_path = os.path.join(script_dir, "input", "example.txt")
    answer = solution.main(
        file_path
    )
    assert answer == 4361

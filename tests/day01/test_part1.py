import pytest
from unittest.mock import mock_open, patch

import src.day01.part1 as solution


# Test for read_lines function
def test_read_lines():
    mock_file_content = "line1\nline2\nline3"
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        result = solution.read_lines("dummy_path")
    assert result == ["line1\n", "line2\n", "line3"]


# Test for calculate_calibration_total function
@patch('src.day01.models.CalibrationLine.CalibrationLine.to_calibration_info')
def test_calculate_calibration_total(mock_to_calibration_info):
    # Mock the to_calibration_info method
    mock_calib_info = mock_to_calibration_info.return_value
    mock_calib_info.calculate_calibration_value.return_value = 10

    # Assuming each line leads to a calibration value of 10
    lines = ["line1", "line2", "line3"]
    total = solution.calculate_calibration_total(lines)

    assert total == 30  # 10 per line * 3 lines

def test_given_example():
    file_path = "/Users/nickbuser/Projects/Personal/advent_of_code_2023_python/tests/day01/input/example.txt"
    answer = solution.calculate_calibration_total(
        solution.read_lines(file_path)
    )
    assert answer == 142


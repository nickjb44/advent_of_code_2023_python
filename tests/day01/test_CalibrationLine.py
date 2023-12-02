import pytest

from src.day01.models.CalibrationInfo import CalibrationInfo
from src.day01.models.CalibrationLine import CalibrationLine


def test_get_numbers_with_just_numbers():
    line = CalibrationLine("12")
    assert line.get_numbers() == ['1', '2']


def test_get_numbers_with_no_numbers():
    line = CalibrationLine("abcdef")
    with pytest.raises(ValueError):
        line.get_numbers()


def test_line_to_calibration_info():
    line = CalibrationLine("123abc56")
    calibration_info = line.to_calibration_info()
    assert isinstance(calibration_info, CalibrationInfo)
    assert calibration_info.first_value == '1'
    assert calibration_info.second_value == '6'


def test_line_with_numbers_in_middle():
    line = CalibrationLine("ad1df2s")
    calibration_info = line.to_calibration_info()
    assert isinstance(calibration_info, CalibrationInfo)
    assert calibration_info.first_value == '1'
    assert calibration_info.second_value == '2'


def test_line_with_just_one_number():
    line = CalibrationLine("ad1dfs")
    calibration_info = line.to_calibration_info()
    assert isinstance(calibration_info, CalibrationInfo)
    assert calibration_info.first_value == '1'
    assert calibration_info.second_value == '1'

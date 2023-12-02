import pytest

from src.day01.models.CalibrationInfo import CalibrationInfo


def test_calibration_info_returns_correct_sum():
    calibration_info = CalibrationInfo("1", "3")
    assert calibration_info.calculate_calibration_value() == 13

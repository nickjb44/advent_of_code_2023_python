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


def test_get_numbers_and_number_words_with_digits():
    content = "There are 2 apples and 3 oranges."
    line = CalibrationLine(content)
    assert line.get_numbers_and_number_words() == ["2", "3"]


def test_get_numbers_and_number_words_with_words():
    content = "I have one cat and two dogs."
    line = CalibrationLine(content)
    assert line.get_numbers_and_number_words() == ["one", "two"]


def test_get_numbers_and_number_words_with_no_numbers():
    content = "This line has no numbers."
    line = CalibrationLine(content)
    with pytest.raises(ValueError):
        line.get_numbers_and_number_words()


def test_get_numbers_and_number_words_with_mixed_content():
    content = "I saw 3 birds and two trees."
    line = CalibrationLine(content)
    assert line.get_numbers_and_number_words() == ["3", "two"]


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


def test_with_words_1():
    line = CalibrationLine("two1nine")
    calibration_info = line.to_calibration_info_with_number_words()
    assert isinstance(calibration_info, CalibrationInfo)
    assert calibration_info.first_value == '2'
    assert calibration_info.second_value == '9'


def test_with_words_2():
    line = CalibrationLine("abcone2threexyz")
    calibration_info = line.to_calibration_info_with_number_words()
    assert isinstance(calibration_info, CalibrationInfo)
    assert calibration_info.first_value == '1'
    assert calibration_info.second_value == '3'


def test_calibration_info_with_number_words():
    for word, number in valid_number_words.items():
        line = CalibrationLine(f"This is a test line with the word {word} in it")
        calib_info = line.to_calibration_info_with_number_words()
        assert calib_info.first_value == number, f"Failed for word: {word}"


def test_calibration_info_with_no_number_words():
    line = CalibrationLine("This line has no number or word")
    with pytest.raises(ValueError):
        _ = line.to_calibration_info_with_number_words()


def test_calibration_info_with_mixed_numbers_and_words():
    line = CalibrationLine("There are three apples and 2 oranges")
    calib_info = line.to_calibration_info_with_number_words()
    assert calib_info.first_value == '3' and calib_info.second_value == '2'

def test_words_overlap():
    line = CalibrationLine("7fiveonedzbmblrtqfoneightkc")
    calib_info = line.to_calibration_info_with_number_words()
    assert calib_info.first_value == '7' and calib_info.second_value == '8'

valid_number_words = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

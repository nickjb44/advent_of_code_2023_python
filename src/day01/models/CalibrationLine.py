from src.day01.models.CalibrationInfo import CalibrationInfo
from src.utils.models.Line import Line
import re


class CalibrationLine(Line):

    def get_numbers(self):
        numbers = re.findall(r'\d', self.content)
        if len(numbers) == 0:
            raise ValueError("Line doesn't have any numbers, panic!")
        return numbers

    def to_calibration_info(self):
        numbers = self.get_numbers()
        return CalibrationInfo(
            first_value=numbers[0],
            second_value=numbers[-1]
        )

    def get_numbers_and_number_words(self):
        digit_regex = r'\d'
        word_regex = '|'.join(re.escape(word) for word in valid_number_words.keys())
        combined_regex = f"{digit_regex}|{word_regex}"

        numbers = re.findall(combined_regex, self.content)
        if not numbers:
            raise ValueError("Line doesn't have any numbers, panic!")
        return numbers

    def to_calibration_info_with_number_words(self):

        numbers = self.get_numbers_and_number_words()

        digit_numbers = list(map(
            lambda number: valid_number_words[number] if number in valid_number_words else number,
            numbers
        ))
        return CalibrationInfo(
            first_value=digit_numbers[0],
            second_value=digit_numbers[-1]
        )


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

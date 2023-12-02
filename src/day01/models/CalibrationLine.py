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

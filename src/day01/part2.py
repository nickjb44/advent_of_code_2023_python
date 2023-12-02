from functools import reduce

from src.day01.models.CalibrationInfo import CalibrationInfo
from src.day01.models.CalibrationLine import CalibrationLine


def read_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def calculate_calibration_total(lines):
    calibration_info_sums = map(
        lambda line: CalibrationLine(line).to_calibration_info_with_number_words().calculate_calibration_value(),
        lines
    )

    return reduce(
        lambda x, y: x + y,
        calibration_info_sums
    )


def main():
    file_path = "input/input.txt"
    calibration_value = calculate_calibration_total(
        read_lines(file_path)
    )

    print(f"the calibration value is {calibration_value}")


if __name__ == "__main__":
    main()

class CalibrationInfo:

    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value

    def calculate_calibration_value(self):
        return int(self.first_value + self.second_value)

class OASIS:

    def __init__(self, measurements):
        self.measurements = measurements

    def calculate_next_in_sequence(self):
        return OASIS.recursive_sequence_constructor(self.measurements)[-1]

    def calculate_previous_in_sequence(self):
        return OASIS.reverse_recursive_sequence_constructor(self.measurements)[0]

    def alternate_calculate_previous_in_sequence(self):
        return OASIS.recursive_sequence_constructor(list(reversed(self.measurements)))[-1]


    @staticmethod
    def recursive_sequence_constructor(sequence):
        if all([num == 0 for num in sequence]):
            sequence.append(0)
            return sequence
        diff_sequence = []
        l = 0
        r = 1
        while r < len(sequence):
            diff = sequence[r] - sequence[l]
            diff_sequence.append(diff)
            r += 1
            l += 1

        next_sequence_down = OASIS.recursive_sequence_constructor(diff_sequence)
        sequence.append(sequence[-1] + next_sequence_down[-1])

        return sequence

    @staticmethod
    def reverse_recursive_sequence_constructor(sequence):
        if all([num == 0 for num in sequence]):
            sequence.append(0)
            return sequence
        diff_sequence = []
        r = len(sequence) - 1
        l = r - 1
        while l >= 0:
            diff = sequence[r] - sequence[l]
            diff_sequence.append(diff)
            r -= 1
            l -= 1

        next_sequence_down = OASIS.recursive_sequence_constructor(diff_sequence)
        previous_number = sequence[0] - next_sequence_down[0]
        sequence.insert(0, previous_number)

        return sequence


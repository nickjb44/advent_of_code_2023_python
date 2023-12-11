from src.day09.models.OASIS import OASIS


def test_recursive_sequence_constructor():
    example = "0 3 6 9 12 15"
    oasis = OASIS([int(num) for num in example.split()])
    assert oasis.calculate_next_in_sequence() == 18

def test_reverse_recursive_sequence_constructor():
    example = "10  13  16  21  30  45"
    oasis = OASIS([int(num) for num in example.split()])
    assert oasis.alternate_calculate_previous_in_sequence() == 5


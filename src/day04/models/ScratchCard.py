from typing import Set


class ScratchCard:

    def __init__(self, card_id, winning_numbers, your_numbers):
        self.card_id: int = card_id
        self.winning_numbers: Set[int] = winning_numbers
        self.matching_numbers: Set[int] = your_numbers

    def get_matched_numbers(self) -> Set[int]:
        return self.winning_numbers & self.matching_numbers

import re
from typing import Set

from src.day04.models.ScratchCard import ScratchCard
from src.utils.models.Line import Line


class ScratchCardLine(Line):

    def __init__(self, content):
        super().__init__(content)
        self.card_number: int = self.get_card_number()
        self.winning_numbers: Set[int] = self.get_winning_numbers()
        self.your_numbers: Set[int] = self.get_your_numbers()

    def get_card_number(self):
        return int(
            re.search(r'\d+', self.content.split(':')[0]).group()
        )

    def get_winning_numbers(self):
        winning_numbers_string = self.content.split(':')[1].split('|')[0]
        winning_numbers = re.findall(r'\d+', winning_numbers_string)
        return {int(winning_number) for winning_number in winning_numbers}

    def get_your_numbers(self):
        winning_numbers_string = self.content.split(':')[1].split('|')[1]
        winning_numbers = re.findall(r'\d+', winning_numbers_string)
        return {int(winning_number) for winning_number in winning_numbers}

    def to_scratch_card(self):
        return ScratchCard(
            card_id=self.card_number,
            winning_numbers=self.winning_numbers,
            your_numbers=self.your_numbers
        )


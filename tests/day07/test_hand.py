from src.day07.models.Hand import Hand
from src.day07.models.HandRank import HandRank


def test_hand_rank_five_of_a_kind():
    hand = Hand("AAAAA", 10)
    assert hand.get_hand_rank() == HandRank.FIVE_OF_A_KIND


def test_hand_rank_four_of_a_kind():
    hand = Hand("AKAAA", 10)
    assert hand.get_hand_rank() == HandRank.FOUR_OF_A_KIND


def test_hand_rank_full_house():
    hand = Hand("AKAAK", 10)
    assert hand.get_hand_rank() == HandRank.FULL_HOUSE


def test_hand_rank_three_of_a_kind():
    hand = Hand("AAAQK", 10)
    assert hand.get_hand_rank() == HandRank.THREE_OF_A_KIND


def test_hand_rank_two_pair():
    hand = Hand("AAQQK", 10)
    assert hand.get_hand_rank() == HandRank.TWO_PAIR


def test_hand_rank_one_pair():
    hand = Hand("AAQJK", 10)
    assert hand.get_hand_rank() == HandRank.ONE_PAIR


def test_hand_rank_high_card():
    hand = Hand("2AQJK", 10)
    assert hand.get_hand_rank() == HandRank.HIGH_CARD


def test_hand_eq():
    hand_one = Hand("AAAAA", 10)
    hand_two = Hand("AAAAA", 10)
    assert hand_one == hand_two


def test_hand_le():
    hand_one = Hand("AAAAA", 10)
    hand_two = Hand("AAAAA", 10)
    assert hand_one <= hand_two


def test_hand_ge():
    hand_one = Hand("AAAAA", 10)
    hand_two = Hand("AAAAA", 10)
    assert hand_one >= hand_two


def test_hand_lt():
    hand_one = Hand("AAAAJ", 10)
    hand_two = Hand("AAAAA", 10)
    assert hand_one < hand_two


def test_hand_gt():
    hand_one = Hand("AAAAA", 10)
    hand_two = Hand("AAAAJ", 10)
    assert hand_one > hand_two


def test_hand_not_eq():
    hand_one = Hand("AAAAJ", 10)
    hand_two = Hand("AAAAA", 10)
    assert not (hand_one == hand_two)


def test_hand_not_le():
    hand_one = Hand("AAAAA", 10)
    hand_two = Hand("AAAAJ", 10)
    assert not (hand_one <= hand_two)


def test_hand_not_ge():
    hand_one = Hand("AAAAJ", 10)
    hand_two = Hand("AAAAA", 10)
    assert not (hand_one >= hand_two)


def test_hand_not_lt():
    hand_one = Hand("AAAAA", 10)
    hand_two = Hand("AAAAA", 10)
    assert not (hand_one < hand_two)


def test_hand_not_gt():
    hand_one = Hand("AAAAA", 10)
    hand_two = Hand("AAAAA", 10)
    assert not (hand_one > hand_two)


def test_hand_sort():
    hand_one = Hand("AAAAA", 10)
    hand_three = Hand("AAAJJ", 10)
    hand_two = Hand("AAAAJ", 10)
    sorted = [hand_three, hand_one, hand_two]
    sorted.sort()
    assert sorted[0] is hand_three
    assert sorted[1] is hand_two
    assert sorted[2] is hand_one


def test_gt_example():
    hand_one = Hand("9A563", 10)
    hand_two = Hand("72689", 10)
    assert not (hand_two > hand_one)

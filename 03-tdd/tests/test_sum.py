from utils.sum import sum


def test_sum_two_numbers():
    excepted = 3

    result = sum(1, 2)

    assert result == excepted


def test_sum_two_numbers_2():
    excepted = 7

    result = sum(3, 4)

    assert result == excepted

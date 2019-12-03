import pytest

from source.awesome_list import sum, bubbleSort, sum_lists


def test_assert_true():
    assert True

# AAA: Arrange, Act and Assert
# Arrange: Preparamos el ecosistema para realizar el text
# Act: usamos el ecosistema para ejecutar el test
# Assert: hacemos las comprobaciones para ver si el test pasa correctamente.


def test_sum_list():
    # Arrange
    expected = 15
    numbers = [1, 2, 3, 4, 5]

    # Act
    result = sum(numbers)

    # Assert
    assert result == expected


def test_sum_empty_list_should_be_zero():
    # Arrange
    expected = 0
    numbers = []

    # Act
    result = sum(numbers)

    # Assert
    assert result == expected


def test_sum_with_negative_numbers():
    # Arrange
    expected = -3
    numbers = [6, -3, -3, 2, -5]

    # Act
    result = sum(numbers)

    # Assert
    assert result == expected


def test_sort_lists():
    # Arrange
    expected = [1, 2, 3, 4, 5]
    numbers = [5, 3, 1, 2, 4]

    # Act
    result = bubbleSort(numbers)

    # Assert
    assert result == expected, "The list must be sorted"


def test_sum_two_lists_with_different_length_raise_error():
    # Arrange
    list1 = [1, 2, 3, 4]
    list2 = [5, 3, 1, 2, 4]

    # Act
    with pytest.raises(Exception):
        sum_lists(list1, list2)


def test_sum_two_lists_with_different_length_raise_error_check_message():
    # Arrange
    list1 = [1, 2, 3, 4]
    list2 = [5, 3, 1, 2, 4]

    # Act
    with pytest.raises(Exception) as e:
        sum_lists(list1, list2)

    assert str(e.value) == "Same size is required to sum two lists"

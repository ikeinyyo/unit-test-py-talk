# Se pide hacer un método que:
# - devuelve Bi cuando el número de entrada es múltiplo de 3
# - Zum cuando es múltiplo de 5
# - BiZum cuando es múltiplo de 3 y de 5
# - El número (como string) en cualquier otro caso
# Nota: Si el número no es entero, lanza una excepción.
import pytest
from utils.bizum import bizum


def test_parameter_is_not_int_raise_exception():
    with pytest.raises(Exception) as e:
        bizum("hola")

    assert str(e.value) == "num"


def test_number_is_multple_of_3_but_not_of_5():
    excepted = "Bi"

    result = bizum(9)

    assert result == excepted


def test_number_is_multple_of_5_but_not_of_3():
    excepted = "Zum"

    result = bizum(10)

    assert result == excepted


def test_number_is_multple_of_3_and_5():
    excepted = "BiZum"

    result = bizum(45)

    assert result == excepted


def test_number_is_not_multple_of_3_or_5():
    excepted = "8"

    result = bizum(8)

    assert result == excepted


def test_number_is_0_return_0():
    excepted = "BiZum"

    result = bizum(0)

    assert result == excepted

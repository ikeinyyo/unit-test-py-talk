# Se pide hacer un método que:
# - devuelve Bi cuando el número de entrada es múltiplo de 3
# - Zum cuando es múltiplo de 5
# - BiZum cuando es múltiplo de 3 y de 5
# - El número en cualquier otro caso
# Nota: Si el número no es entero, lanza una excepción.
import pytest
from utils.bizum import bizum


def test_first_parameter_is_not_int_raise_exception():
    with pytest.raises(Exception) as e:
        bizum("hola", 1)

    assert str(e.value) == "num1"


def test_second_parameter_is_not_int_raise_exception():
    with pytest.raises(Exception) as e:
        bizum(1, 4.5)

    assert str(e.value) == "num2"

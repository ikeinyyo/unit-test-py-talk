# Asserts

Es importante seguir las convenciones de pytest.

```
file: test_*.py
method: test_*
```

## Assert True

Implementamos un test de `assert True`.

```py
from source.awesome_list import sum, bubbleSort, sum_lists

def test_assert_true():
    assert True
```

## Ejecutar los tests

Para ejecutar los tests debemos usar el siguiente comando desde la raíz del proyecto.

```bash
python -m pytest
```

## Test sum

Implementamos los test de sum:

```py
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
```

Ahora hay que implementar los test para los casos extremos:

```py
def test_sum_empty_list_should_be_zero():
    # Arrange
    expected = 0
    numbers = []

    # Act
    result = sum(numbers)

    # Assert
    assert result == expected
```

Si ejecutamos, vemos que el test falla, porque no se puede hacer el `reduce` sobre una lista vacía. Así que vamos a cambiar el código para hacer una comprobación.

```py
def sum(numbers):
    if not len(numbers):
        return 0
    return reduce(lambda number, acc: acc + number, numbers)
```

Por último, añadimos un test más:

```py
def test_sum_with_negative_numbers():
    # Arrange
    expected = -3
    numbers = [6, -3, -3, 2, -5]

    # Act
    result = sum(numbers)

    # Assert
    assert result == expected
```

## Test bubbleSort

Podemos hacer asserts sobre listas y añadir un mensaje al assert.

```py
def test_sort_lists():
    # Arrange
    expected = [1, 2, 3, 4, 5]
    numbers = [5, 3, 1, 2, 4]

    # Act
    result = bubbleSort(numbers)

    # Assert
    assert result == expected, "The list must be sorted"
```

Podemos comprobar que falla al devolver `numbers` en el código del bubble sort.

```py
def bubbleSort(numbers):
    sorted_list = numbers.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j +
                                            1] = sorted_list[j+1], sorted_list[j]
    return numbers # Cambio para hacer que falle el test
```

## Test sum_list

Hacemos un test que compruebe que se lanza una excepción cuando se intentan sumar dos listas de distinta longitud.

```py
def test_sum_two_lists_with_different_length_raise_error():
    # Arrange
    list1 = [1, 2, 3, 4]
    list2 = [5, 3, 1, 2, 4]

    # Act
    with pytest.raises(ZeroDivisionError):
        sum_lists(list1, list2)
```

Tenemos que cambiar el tipo de la excepción.

```py
def test_sum_two_lists_with_different_length_raise_error():
    # Arrange
    list1 = [1, 2, 3, 4]
    list2 = [5, 3, 1, 2, 4]

    # Act
    with pytest.raises(Exception):
        sum_lists(list1, list2)
```

Podemos validar que el mensaje de la Excepción sea el correcto:

```py
def test_sum_two_lists_with_different_length_raise_error_check_message():
    # Arrange
    list1 = [1, 2, 3, 4]
    list2 = [5, 3, 1, 2, 4]

    # Act
    with pytest.raises(Exception) as e:
        sum_lists(list1, list2)

    assert str(e.value) == "Same size is required to sum two lists"
```

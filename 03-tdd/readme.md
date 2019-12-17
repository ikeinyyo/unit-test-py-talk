# TDD

Es importante seguir las convenciones de pytest.

```
file: test_*.py
method: test_*
```

## Ejecutar los tests

Para ejecutar los tests debemos usar el siguiente comando desde la raíz del proyecto.

```bash
python -m pytest
```

## Importancia de un código modular = más fácil de testear

Comparación de los dos ficheros en samples

## TDD - SUM

Implementar el método sum para que cumpla el test

```py
def sum(num1, num2):
    return 3
```

Crear un nuevo test para evaluar el código.

```py
def test_sum_two_numbers_2():
    excepted = 7

    result = sum(3, 4)

    assert result == excepted
```

Y cambiamos la implementación de `sum`:

```py
def sum(num1, num2):
    return 3 if num1 == 1 else 7
```

## TDD - BiZum

Primero es asegurarse de que los dos números son enteros

```py
def test_first_parameter_is_not_int_raise_exception():
    with pytest.raises(Exception):
        sum_lists(list1, list2)
```

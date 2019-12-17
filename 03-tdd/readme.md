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

Primero es asegurarse de que el parametro es un entero

```py
def test_parameter_is_not_int_raise_exception():
    with pytest.raises(Exception) as e:
        bizum("hola")

    assert str(e.value) == "num"
```

Ahora vamos a implementar el método:

```py
def bizum(num):
    if not isinstance(num, int):
        raise Exception("num")
```

Seguimos, qué pasa si es múltiplo de 3 o de 5:

```py
def test_number_is_multple_of_3_but_not_of_5():
    excepted = "Bi"

    result = bizum(9)

    assert result == excepted


def test_number_is_multple_of_5_but_not_of_3():
    excepted = "Zum"

    result = bizum(10)

    assert result == excepted
```

Implementamos el método:

```py
def bizum(num):
    if not isinstance(num, int):
        raise Exception("num")

    if num % 3 == 0:
        return "Bi"
    if num % 5 == 0:
        return "Zum"
```

Ahora, vamos a implementar el caso en que sea múltiplo de 3 y 5

```py
def test_number_is_multple_of_3_and_5():
    excepted = "BiZum"

    result = bizum(45)

    assert result == excepted
```

```py
def bizum(num):
    if not isinstance(num, int):
        raise Exception("num")

    if num % 3 == 0 and num % 5 == 0:
        return "BiZum"
    if num % 3 == 0:
        return "Bi"
    if num % 5 == 0:
        return "Zum"
```

Por último, vamos a ver si el caso en que el número no sea múltiplo de ninguno

```py
def test_number_is_not_multple_of_3_or_5():
    excepted = "8"

    result = bizum(8)

    assert result == excepted
```

```py
def bizum(num):
    if not isinstance(num, int):
        raise Exception("num")

    if num % 3 == 0 and num % 5 == 0:
        return "BiZum"
    if num % 3 == 0:
        return "Bi"
    if num % 5 == 0:
        return "Zum"

    return str(num)
```

Por último, sería interesante probar el caso del 0.

```py
def test_number_is_0_return_0():
    excepted = "0"

    result = bizum(0)

    assert result == excepted
```

Al ejecutarlo, vemos que nos devuelve BiZum, es decir es múltiplo de 3 y 5. Podemos evaluar si nos interesa o no. En principio, aceptamos el cambio.

```py
def test_number_is_0_return_0():
    excepted = "BiZum"

    result = bizum(0)

    assert result == excepted
```

Por último, llega la etapa de Refactorización:

```py
def bizum(num):
    if not isinstance(num, int):
        raise Exception("num")

    result = ""
    if num % 3 == 0:
        result += "Bi"
    if num % 5 == 0:
        result += "Zum"

    return result if result else str(num)
```

Ahora podemos hacer un refactor y asegurarnos de que todo cumple con la especificación, ya que tenemos los tests.

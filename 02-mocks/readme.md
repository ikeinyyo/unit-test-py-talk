# Mock

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

## Mock con inyección de dependencias

Hacemos un mock del servicio de API que se le pasa al get_games_from_service. Hacemos que devuelva un 401 en el estado.

```py
def test_get_games_with_error_500_from_api():
    api_mock = Mock()
    api_mock.make_bgg_api_request.return_value = {'status': 401}

    with pytest.raises(Exception) as e:
        get_games_from_service(api_mock)

    assert str(e.value) == "500"
```

Ahora comprobamos que ante una lista vacía, devuelve un 404.

```py
def test_get_games_with_empty_list_from_api():
    api_mock = Mock()
    api_mock.make_bgg_api_request.return_value = {'status': 200, "games": []}

    with pytest.raises(Exception) as e:
        get_games_from_service(api_mock)

    assert str(e.value) == "404"
```

Por último, probamos el caso donde sí devuelve una lista con juegos:

```py
def test_get_games_with_list_from_api():
    expected = ["7 Wonders", "Terraforming Mars"]
    api_mock = Mock()
    api_mock.make_bgg_api_request.return_value = {
        'status': 200, "games": expected}

    results = get_games_from_service(api_mock)

    assert results == expected
```

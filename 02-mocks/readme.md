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

## Patch del servicio

Podemos hacer un patch con decoradores y obtener un objeto.

```py
from unittest.mock import patch
```

```py
@patch('utils.bgg.make_bgg_api_request')
def test_get_games_sdk_with_error_500_from_api(bgg_mock):
    bgg_mock.return_value = {'status': 401}
    with pytest.raises(Exception) as e:
        get_games()

    assert str(e.value) == "500"
```

Con el Context Manager y definir el valor que queremos que devuelva.

```py
def test_get_games_sdk_with_empty_list_from_api():
    with patch('utils.bgg.make_bgg_api_request',
               return_value={'status': 200, 'games': []}):
        with pytest.raises(Exception) as e:
            get_games()

    assert str(e.value) == "404"
```

E incluso una mezcla de las dos anteriores. Usando el Context Manager obteniendo el mock o con el decorador y indicando el objeto de retorno.

```py
def test_get_games_sdk_with_list_from_api():
    expected = ["7 Wonders", "Terraforming Mars"]

    with patch('utils.bgg.make_bgg_api_request') as bgg_mock:
        bgg_mock.return_value = {'status': 200, 'games': expected}
        results = get_games()

    assert results == expected
```

## Mock Open

```py
from unittest.mock import mock_open
```

Hacemos un test simulando que abrimos y leemos un fichero de texto:

```py
def test_get_settings_successful():
    expected = "Galladoconsell"
    data = f'{{"mejor_consejo": "{expected}"}}'

    with patch("builtins.open", mock_open(read_data=data)):
        setting = get_setting('mejor_consejo', 'default')

    assert setting == expected
```

También, probamos qué pasa si el fichero no existe.

```py
def test_get_settings_with_not_exist_file():
    expected = "default"
    data = f'{{"mejor_consejo": "Galladoconsell"}}'

    with patch("builtins.open", mock_open(read_data=data)) as open_mock:
        open_mock.side_effect = FileNotFoundError
        setting = get_setting('mejor_consejo', expected)

    assert setting == expected
```

Podemos hacer el mock/patch en el momento que nosotros queramos. Teniendo una certeza de que el resto está testeado.

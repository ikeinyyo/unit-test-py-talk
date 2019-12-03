import pytest
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

from utils.awesome_sdk import get_games, get_games_from_service
from utils.settings import get_setting


def test_get_games_with_error_500_from_api():
    api_mock = Mock()
    api_mock.make_bgg_api_request.return_value = {'status': 401}

    with pytest.raises(Exception) as e:
        get_games_from_service(api_mock)

    assert str(e.value) == "500"


def test_get_games_with_empty_list_from_api():
    api_mock = Mock()
    api_mock.make_bgg_api_request.return_value = {'status': 200, "games": []}

    with pytest.raises(Exception) as e:
        get_games_from_service(api_mock)

    assert str(e.value) == "404"


def test_get_games_with_list_from_api():
    expected = ["7 Wonders", "Terraforming Mars"]
    api_mock = Mock()
    api_mock.make_bgg_api_request.return_value = {
        'status': 200, "games": expected}

    results = get_games_from_service(api_mock)

    assert results == expected


@patch('utils.bgg.make_bgg_api_request')
def test_get_games_sdk_with_error_500_from_api(bgg_mock):
    bgg_mock.return_value = {'status': 401}
    with pytest.raises(Exception) as e:
        get_games()

    assert str(e.value) == "500"


def test_get_games_sdk_with_empty_list_from_api():
    with patch('utils.bgg.make_bgg_api_request',
               return_value={'status': 200, 'games': []}):
        with pytest.raises(Exception) as e:
            get_games()

    assert str(e.value) == "404"


def test_get_games_sdk_with_list_from_api():
    expected = ["7 Wonders", "Terraforming Mars"]

    with patch('utils.bgg.make_bgg_api_request') as bgg_mock:
        bgg_mock.return_value = {'status': 200, 'games': expected}
        results = get_games()

    assert results == expected


def test_get_settings_successful():
    expected = "Galladoconsell"
    data = f'{{"mejor_consejo": "{expected}"}}'

    with patch("builtins.open", mock_open(read_data=data)):
        setting = get_setting('mejor_consejo', 'default')

    assert setting == expected


def test_get_settings_with_not_exist_file():
    expected = "default"
    data = f'{{"mejor_consejo": "Galladoconsell"}}'

    with patch("builtins.open", mock_open(read_data=data)) as open_mock:
        open_mock.side_effect = FileNotFoundError
        setting = get_setting('mejor_consejo', expected)

    assert setting == expected

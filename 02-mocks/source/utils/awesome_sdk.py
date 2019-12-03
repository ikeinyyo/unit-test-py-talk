# from utils.bgg import make_bgg_api_request
import utils.bgg as bgg


def get_games_from_service(service):
    result = service.make_bgg_api_request()

    if result['status'] != 200:
        raise Exception('500')
    if not len(result['games']):
        raise Exception('404')

    return result['games']


def get_games():
    result = bgg.make_bgg_api_request()

    if result['status'] != 200:
        raise Exception('500')
    if not len(result['games']):
        raise Exception('404')

    return result['games']

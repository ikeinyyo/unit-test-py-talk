from utils.settings import get_setting
from utils.awesome_sdk import get_games_from_service, get_games
from utils.bgg import BggApi


if __name__ == "__main__":
    print(get_games_from_service(BggApi()))
    print(get_games())
    print(get_setting('best_developer_ever'))

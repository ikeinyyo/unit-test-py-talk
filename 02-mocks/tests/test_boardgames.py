import pytest
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

from utils.awesome_sdk import get_games, get_games_from_service
from utils.settings import get_setting

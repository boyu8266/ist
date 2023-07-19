from configparser import ConfigParser
from typing import List

from pydantic import BaseModel


class Config(BaseModel):
    telegram_token: str
    telegram_userid: str
    numbers: List[str]
    strategies: List[str]
    periods: List[str]

    @classmethod
    def from_config_file(cls):
        config = ConfigParser()
        config.read('config.ini')

        numbers = [num.strip() for num in config.get('Strategy', 'numbers').split(',')]
        strategies = [strategy.strip() for strategy in config.get('Strategy', 'strategies').split(',')]
        periods = [period.strip() for period in config.get('Strategy', 'periods').split(',')]

        return cls(
            telegram_token=config.get('Telegram', 'token'),
            telegram_userid=config.get('Telegram', 'userid'),
            numbers=numbers,
            strategies=strategies,
            periods=periods
        )

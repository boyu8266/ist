import os
from configparser import ConfigParser
from pathlib import Path
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
        
        config_paths = [
            'config.ini',
            os.path.expanduser('~/.config/ist/config.ini'),
        ]
        
        config_file = None
        for path in config_paths:
            if os.path.exists(path):
                config_file = path
                break
        
        if not config_file:
            raise FileNotFoundError(
                f"Config file not found. Please create one at:\n"
                f"  - Current directory: ./config.ini\n"
                f"  - User config: ~/.config/ist/config.ini\n"
                f"Reference: config.example.ini"
            )
        
        config.read(config_file)

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

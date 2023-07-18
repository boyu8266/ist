from configparser import ConfigParser

from pydantic import BaseModel


class Config(BaseModel):
    telegram_token: str

    @classmethod
    def from_config_file(cls):
        config = ConfigParser()
        config.read('config.ini')

        return cls(
            telegram_token=config.get('Telegram', 'token')
        )

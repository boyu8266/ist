import os
import random
import time

from logging_service import LoggingService

from .__version__ import __version__
from .config import Config
from .pipeline import DayDataPipeline, MonthDataPipeline, WeekDataPipeline
from .strategy import Strategy

__all__ = [
    '__version__',

    'Strategy',

    'DayDataPipeline',
    'WeekDataPipeline',
    'MonthDataPipeline'
]

# instance
config: Config = Config.from_config_file()
logs: LoggingService = LoggingService()
if logs.log_file == None:
    folder = 'logs'
    if not os.path.exists(folder):
        os.makedirs(folder)
    logs.log_file = os.path.join(folder, f'{time.strftime("%Y%m%d_%H%M%S")}.txt')


def sleep(lower: float = 1.0, upper: float = 3.0):
    delay = random.uniform(lower, upper)
    time.sleep(delay)

import logging
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from logging_service import LoggingService
from tpdp import Pipeline, Step

from ist.state import IstState
from ist.step import *
from ist.strategy import Strategy

fetchdata = FetchData('fetch data')
weeklystock = WeeklyStock('weekly stock')
monthlystock = MonthlyStock('monthly stock')
addmacddata = AddMACDData('add macd data')
addkddata = AddKDData('add kd data')
verifystrategy = VerifyStrategy('verify stratrgy')
telegramnotify = TelegramNotify('telegram notify')


class PeriodDataPipeline(ABC):
    def __init__(self, name: str = 'pipeline', logger: logging.Logger = LoggingService().logger) -> None:
        self.__pipeline: Pipeline = self.__init_pipeline(name, logger)

    def __init_pipeline(self, name: str, logger: logging.Logger) -> Pipeline:
        pipeline = Pipeline(logger=logger, name=name)
        for step in self.get_steps():
            pipeline.registry_step(step)
        return pipeline

    @abstractmethod
    def get_steps(self) -> List[Step]:
        pass

    def run(self, stock: str, strategy: Strategy, period: str, start_date: str = '1997-01-01', end_date: str = datetime.now().strftime("%Y-%m-%d"), timeout: int = 30) -> IstState:
        state: IstState = IstState(
            stock=stock,
            start_date=start_date,
            end_date=end_date,
            timeout=timeout,
            strategy=strategy,
            period=period
        )
        r = self.__pipeline.run(state)
        return state


class DayDataPipeline(PeriodDataPipeline):
    def get_steps(self) -> List[Step]:
        return [fetchdata, addmacddata, addkddata, verifystrategy, telegramnotify]


class WeekDataPipeline(PeriodDataPipeline):
    def get_steps(self) -> List[Step]:
        return [fetchdata, weeklystock, addmacddata, addkddata, verifystrategy, telegramnotify]


class MonthDataPipeline(PeriodDataPipeline):
    def get_steps(self) -> List[Step]:
        return [fetchdata, monthlystock, addmacddata, addkddata, verifystrategy, telegramnotify]

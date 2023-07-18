from backtesting.lib import cross, crossover

from ist import (DayDataPipeline, MonthDataPipeline, Strategy,
                 WeekDataPipeline, logs)
from tests.sleep import sleep


class KDStrategy(Strategy):
    def condition_for_buying_stock(self) -> bool:
        return (self.dataframe.k < 27)[-1] & crossover(self.dataframe.k, self.dataframe.d)

    def condition_for_selling_stock(self) -> bool:
        return (self.dataframe.k > 75)[-1] & cross(self.dataframe.d, self.dataframe.k)


class TestDayDataPipeline:
    stock = '2330'
    pipeline = DayDataPipeline('day data pipeline')
    strategy = KDStrategy()

    def test_buy(self):
        state = self.pipeline.run(self.stock, self.strategy, start_date='2023-1-1', end_date='2023-4-28')
        logs.info(f'last: {state.dataframe.tail(1).to_dict()}')
        logs.info(f'buy: {state.buy}')
        logs.info(f'sell: {state.sell}')
        assert state.buy == True
        assert state.sell == False

        # last day
        n = len(state.dataframe) - 1
        df = state.dataframe[:n]
        strategy = KDStrategy()
        strategy.dataframe = df
        assert strategy.condition_for_buying_stock() == False
        assert strategy.condition_for_selling_stock() == False

        sleep()

    def test_sell(self):
        state = self.pipeline.run(self.stock, self.strategy, start_date='2023-1-1', end_date='2023-5-31')
        logs.info(f'last: {state.dataframe.tail(1).to_dict()}')
        logs.info(f'buy: {state.buy}')
        logs.info(f'sell: {state.sell}')
        assert state.buy == False
        assert state.sell == True

        # last day
        n = len(state.dataframe) - 1
        df = state.dataframe[:n]
        strategy = KDStrategy()
        strategy.dataframe = df
        assert strategy.condition_for_buying_stock() == False
        assert strategy.condition_for_selling_stock() == False

        sleep()


class TestWeekDataPipeline:
    stock = '2330'
    pipeline = WeekDataPipeline('week data pipeline')
    strategy = KDStrategy()

    def test_buy(self):
        state = self.pipeline.run(self.stock, self.strategy, end_date='2022-7-15')
        logs.info(f'last: {state.dataframe.tail(1).to_dict()}')
        logs.info(f'buy: {state.buy}')
        logs.info(f'sell: {state.sell}')
        assert state.buy == True
        assert state.sell == False

        # last day
        n = len(state.dataframe) - 1
        df = state.dataframe[:n]
        strategy = KDStrategy()
        strategy.dataframe = df
        assert strategy.condition_for_buying_stock() == False
        assert strategy.condition_for_selling_stock() == False

        sleep()

    def test_sell(self):
        state = self.pipeline.run(self.stock, self.strategy, end_date='2023-2-24')
        logs.info(f'last: {state.dataframe.tail(1).to_dict()}')
        logs.info(f'buy: {state.buy}')
        logs.info(f'sell: {state.sell}')
        assert state.buy == False
        assert state.sell == True

        # last day
        n = len(state.dataframe) - 1
        df = state.dataframe[:n]
        strategy = KDStrategy()
        strategy.dataframe = df
        assert strategy.condition_for_buying_stock() == False
        assert strategy.condition_for_selling_stock() == False

        sleep()


class TestMonthDataPipeline:
    stock = '2330'
    pipeline = MonthDataPipeline('month data pipeline')
    strategy = KDStrategy()

    def test_buy(self):
        state = self.pipeline.run(self.stock, self.strategy, end_date='2022-11-30')
        logs.info(f'last: {state.dataframe.tail(1).to_dict()}')
        logs.info(f'buy: {state.buy}')
        logs.info(f'sell: {state.sell}')
        assert state.buy == True
        assert state.sell == False

        # last day
        n = len(state.dataframe) - 1
        df = state.dataframe[:n]
        strategy = KDStrategy()
        strategy.dataframe = df
        assert strategy.condition_for_buying_stock() == False
        assert strategy.condition_for_selling_stock() == False

        sleep()

    def test_sell(self):
        state = self.pipeline.run(self.stock, self.strategy, end_date='2021-3-30')
        logs.info(f'last: {state.dataframe.tail(1).to_dict()}')
        logs.info(f'buy: {state.buy}')
        logs.info(f'sell: {state.sell}')
        assert state.buy == False
        assert state.sell == True

        # last day
        n = len(state.dataframe) - 1
        df = state.dataframe[:n]
        strategy = KDStrategy()
        strategy.dataframe = df
        assert strategy.condition_for_buying_stock() == False
        assert strategy.condition_for_selling_stock() == False

        sleep()

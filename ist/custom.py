# Please write your strategy below
from backtesting.lib import cross, crossover

from ist.strategy import Strategy


class Custom(Strategy):
    def condition_for_buying_stock(self) -> bool:
        df = self.dataframe
        df.k
        df.d
        df.macd
        df.dif
        df.osc
        return False

    def condition_for_selling_stock(self) -> bool:
        df = self.dataframe
        df.k
        df.d
        df.macd
        df.dif
        df.osc
        return False

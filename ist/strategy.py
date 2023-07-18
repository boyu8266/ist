from abc import ABC, abstractmethod

import pandas as pd


class Strategy(ABC):
    dataframe: pd.DataFrame

    @abstractmethod
    def condition_for_buying_stock(self) -> bool:
        return False

    @abstractmethod
    def condition_for_selling_stock(self) -> bool:
        return False

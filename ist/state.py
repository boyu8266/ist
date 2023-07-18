from datetime import datetime

import pandas as pd
from tpdp import State

from ist.strategy import Strategy


class IstState(State):
    stock: str = ''
    start_date: str = '1997-01-01'
    end_date: str = datetime.now().strftime("%Y-%m-%d")
    timeout: int = 30

    dataframe: pd.DataFrame = pd.DataFrame()

    strategy: Strategy = None
    buy: bool = False
    sell: bool = False

    period: str = 'Day'

    class Config:
        arbitrary_types_allowed = True

from datetime import datetime

import pandas as pd
from tpdp import State


class IstState(State):
    stock: str = ''
    start_date: str = '1997-01-01'
    end_date: str = datetime.now().strftime("%Y-%m-%d")
    timeout: int = 30

    dataframe: pd.DataFrame = pd.DataFrame()

    class Config:
        arbitrary_types_allowed = True

import pandas as pd
from stockstats import StockDataFrame


class KD:
    @staticmethod
    def add_columns(df_raw: pd.DataFrame) -> pd.DataFrame:
        ser = StockDataFrame.retype(df_raw)
        df_raw['k'] = ser['kdjk']
        df_raw['d'] = ser['kdjd']
        return df_raw

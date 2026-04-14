import pandas as pd
from stockstats import StockDataFrame


class MACD:
    @staticmethod
    def add_columns(df_raw: pd.DataFrame) -> pd.DataFrame:
        ser = StockDataFrame.retype(df_raw)
        df_raw['osc'] = ser['macdh'].values
        df_raw['dif'] = ser['macd'].values
        df_raw['macd'] = ser['macds'].values
        return df_raw

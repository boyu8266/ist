import pandas as pd


class Weekly():
    df: pd.DataFrame = None

    def __init__(self, df_raw: pd.DataFrame):
        df_raw['timestamp'] = pd.to_datetime(df_raw['date']).apply(lambda x: x.timestamp())
        df_raw['year'] = pd.to_datetime(df_raw['date']).dt.year
        df_raw['month'] = pd.to_datetime(df_raw['date']).dt.month
        df_raw['day'] = pd.to_datetime(df_raw['date']).dt.day

        df = self.add_week_column(df_raw)
        group_week = df.groupby(['year', 'week'])
        self.df = self.create_week_df(group_week)

    def add_week_column(self, df: pd.DataFrame) -> pd.DataFrame:
        df['week'] = df['timestamp'].map(lambda x: pd.Timestamp(ts_input=x, unit='s', tz='Asia/Taipei').week)
        return df

    def create_week_df(self, group_week) -> pd.DataFrame:
        df = pd.DataFrame()

        df['open'] = group_week['open'].first()
        df['close'] = group_week['close'].last()
        df['high'] = group_week['high'].max()
        df['low'] = group_week['low'].min()
        df.index = pd.DatetimeIndex(pd.to_datetime(group_week['timestamp'].max() * 1000 * 1000 * 1000))

        return df

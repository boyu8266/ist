import pandas as pd


class Weekly():
    df: pd.DataFrame = None

    def __init__(self, df_raw: pd.DataFrame):
        df_raw['timestamp'] = pd.to_datetime(df_raw['date']).apply(lambda x: x.timestamp())
        df_raw['year'] = pd.to_datetime(df_raw['date']).dt.year
        df_raw['month'] = pd.to_datetime(df_raw['date']).dt.month
        df_raw['day'] = pd.to_datetime(df_raw['date']).dt.day

        df = self.__add_week_column(df_raw)
        group_week = df.groupby(['year', 'week'])
        self.df = self.__create_week_df(group_week)

    def __add_week_column(self, df: pd.DataFrame) -> pd.DataFrame:
        df['week'] = df['timestamp'].map(lambda x: pd.Timestamp(ts_input=x, unit='s', tz='Asia/Taipei').week)
        return df

    def __create_week_df(self, group_week) -> pd.DataFrame:
        df = pd.DataFrame()

        df['Open'] = group_week['Open'].first()
        df['Close'] = group_week['Close'].last()
        df['High'] = group_week['High'].max()
        df['Low'] = group_week['Low'].min()
        df.index = pd.DatetimeIndex(pd.to_datetime(group_week['timestamp'].max() * 1000 * 1000 * 1000))

        return df


class Monthly():
    df: pd.DataFrame = None

    def __init__(self, df_raw: pd.DataFrame):
        df_raw['timestamp'] = pd.to_datetime(df_raw['date']).apply(lambda x: x.timestamp())
        df_raw['year'] = pd.to_datetime(df_raw['date']).dt.year
        df_raw['month'] = pd.to_datetime(df_raw['date']).dt.month
        df_raw['day'] = pd.to_datetime(df_raw['date']).dt.day

        group_monthly = df_raw.groupby(['year', 'month'])
        self.df = self.__create_week_df(group_monthly)

    def __create_week_df(self, group_monthly) -> pd.DataFrame:
        df = pd.DataFrame()

        df['Open'] = group_monthly['Open'].first()
        df['Close'] = group_monthly['Close'].last()
        df['High'] = group_monthly['High'].max()
        df['Low'] = group_monthly['Low'].min()
        df.index = pd.DatetimeIndex(pd.to_datetime(group_monthly['timestamp'].max() * 1000 * 1000 * 1000))

        return df

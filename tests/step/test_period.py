from ist.state import IstState
from ist.step import FetchData, MonthlyStock, WeeklyStock
from tests.sleep import sleep


class TestWeeklyStock:
    step = WeeklyStock('weekly stock')

    def test_columns(self):
        state = IstState()
        state.stock = '2330'
        state.start_date = '2023-7-10'
        state.end_date = '2023-7-14'
        FetchData('fetch data').run(state)
        self.step.run(state)

        assert abs(state.dataframe['Open'][0] - 567) < 0.01
        assert abs(state.dataframe['Low'][0] - 565) < 0.01
        assert abs(state.dataframe['High'][0] - 591) < 0.01
        assert abs(state.dataframe['Close'][0] - 591) < 0.01

        sleep()


class TestMonthlyStock:
    step = MonthlyStock('monthly stock')

    def test_columns(self):
        state = IstState()
        state.stock = '2330'
        state.start_date = '2023-6-1'
        state.end_date = '2023-6-30'
        FetchData('fetch data').run(state)
        self.step.run(state)

        assert abs(state.dataframe['Open'][0] - 550) < 0.01
        assert abs(state.dataframe['Low'][0] - 550) < 0.01
        assert abs(state.dataframe['High'][0] - 594) < 0.01
        assert abs(state.dataframe['Close'][0] - 576) < 0.01

        sleep()

import pandas as pd
import pytest

from ist.state import IstState
from ist.step.fetch import FetchData
from ist.step.indicator import AddKDData, AddMACDData
from tests.sleep import sleep


class TestAddMACDData:
    step = AddMACDData('add macd data')

    def test_dataframe_is_none(self):
        state = IstState()
        with pytest.raises(ValueError):
            self.step.run(state)

    def test_dataframe_is_empty(self):
        state = IstState(dataframe=pd.DataFrame())
        with pytest.raises(ValueError):
            self.step.run(state)

    def test_columns(self):
        state = IstState(stock='2330')
        s1 = FetchData('fetch data')
        s1.run(state)
        self.step.run(state)
        assert all(col in state.dataframe.columns for col in ['osc', 'dif', 'macd'])

        sleep()


class TestAddKDData:
    step = AddKDData('add kd data')

    def test_dataframe_is_none(self):
        state = IstState()
        with pytest.raises(ValueError):
            self.step.run(state)

    def test_dataframe_is_empty(self):
        state = IstState(dataframe=pd.DataFrame())
        with pytest.raises(ValueError):
            self.step.run(state)

    def test_columns(self):
        state = IstState(stock='2330')
        s1 = FetchData('fetch data')
        s1.run(state)
        self.step.run(state)
        assert all(col in state.dataframe.columns for col in ['k', 'd'])

        sleep()

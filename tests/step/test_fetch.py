import pytest

from ist.state import IstState
from ist.step import FetchData
from tests.sleep import sleep


class TestFetchDate:
    step = FetchData('fetch_data')

    def test_stock_is_none(self):
        state = IstState()
        with pytest.raises(ValueError):
            self.step.run(state)
            sleep()

    def test_date_is_none(self):
        state = IstState(stock='2330')
        self.step.run(state)
        sleep()

from typing import Any, Callable

from FinMind.data import DataLoader
from tpdp import Step

from ist.state import IstState


class FetchData(Step):
    def run(self, state: IstState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> IstState:
        if state == None or state.stock == None or state.stock == '':
            raise ValueError(f"state == None or state.stock == None or state.stock == ''")

        dataloader: DataLoader = DataLoader()
        df = dataloader.taiwan_stock_daily(state.stock, state.start_date, state.end_date, state.timeout)
        state.dataframe = \
            df.rename(columns={"open": "Open", "max": "High", "min": "Low",
                      "close": "Close", "Trading_Volume": "Volume"})
        return state

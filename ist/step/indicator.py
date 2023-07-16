from typing import Any, Callable

from tpdp import Step

from ist.indicator import KD, MACD
from ist.state import IstState


class AddMACDData(Step):
    def run(self, state: IstState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> IstState:
        if state == None or state.dataframe.empty:
            raise ValueError(f'state == None or state.dataframe.empty')

        state.dataframe = MACD.add_columns(state.dataframe)
        return state


class AddKDData(Step):
    def run(self, state: IstState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> IstState:
        if state == None or state.dataframe.empty:
            raise ValueError(f'state == None or state.dataframe.empty')

        state.dataframe = KD.add_columns(state.dataframe)
        return state

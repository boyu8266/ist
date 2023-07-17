from typing import Any, Callable

from tpdp import Step

from ist.data import Weekly
from ist.state import IstState


class WeeklyStock(Step):
    def run(self, state: IstState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> IstState:
        state.dataframe = Weekly(state.dataframe).df
        return state

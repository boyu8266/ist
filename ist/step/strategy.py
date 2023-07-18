from typing import Any, Callable

from tpdp import Step

from ist.state import IstState
from ist.strategy import Strategy


class VerifyStrategy(Step):
    def run(self, state: IstState, pipeline_abort: Callable[[], None] | None = None, **kwargs: Any) -> IstState:
        if state == None or not isinstance(state.strategy, Strategy):
            raise ValueError(f'state == None or not isinstance(state.strategy, Strategy)')

        state.strategy.dataframe = state.dataframe

        if state.strategy.condition_for_buying_stock():
            state.buy = True

        if state.strategy.condition_for_selling_stock():
            state.sell = True

        return state

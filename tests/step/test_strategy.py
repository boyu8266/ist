import pytest

from ist.state import IstState
from ist.step.strategy import VerifyStrategy
from ist.strategy import Strategy


class TestVerifyStrategy:
    step = VerifyStrategy('verify strategy')

    def test_strategy_is_none(self):
        state = IstState()
        with pytest.raises(ValueError):
            self.step.run(state)

    def test_buying_is_true(self):
        class Buy(Strategy):
            def condition_for_buying_stock(self, **kwargs) -> bool:
                return True

            def condition_for_selling_stock(self, **kwargs) -> bool:
                return super().condition_for_selling_stock(**kwargs)

        buy = Buy()
        state = IstState(strategy=buy)
        self.step.run(state)
        assert state.buy == True
        assert state.sell == False

    def test_selling_is_true(self):
        class Sell(Strategy):
            def condition_for_buying_stock(self, **kwargs) -> bool:
                return super().condition_for_buying_stock(**kwargs)

            def condition_for_selling_stock(self, **kwargs) -> bool:
                return True

        sell = Sell()
        state = IstState(strategy=sell)
        self.step.run(state)
        assert state.buy == False
        assert state.sell == True

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def condition_for_buying_stock(self, **kwargs) -> bool:
        return False

    @abstractmethod
    def condition_for_selling_stock(self, **kwargs) -> bool:
        return False

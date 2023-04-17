from abc import ABC, abstractmethod


class Engine(ABC):
    def __int__(self, current_mileage, last_serviced_mileage, warning_indicator_is_on):
        self.current_mileage = current_mileage
        self.last_serviced_mileage = last_serviced_mileage
        self.warning_indicator_is_on = warning_indicator_is_on

    @abstractmethod
    def engine_should_be_serviced(self):
        pass

from abc import ABC, abstractmethod


class Battery(ABC):
    def __int__(self, last_serviced_date):
        self.last_serviced_date = last_serviced_date

    @abstractmethod
    def battery_should_be_serviced(self):
        pass

from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, tire_status):
        self.tire_status = tire_status


    @abstractmethod
    def tire_should_be_serviced(self):
        pass

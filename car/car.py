from abc import ABC


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    def need_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced()

        # second way
        #if self.engine.engine_should_be_serviced():
        #   return True
        #elif self.battery.battery_should_be_serviced():
        #   return True
        #else:
        #   return False
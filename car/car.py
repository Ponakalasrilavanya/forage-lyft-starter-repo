from abc import ABC


class Car(ABC):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire
    def need_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced() or self.tire.tire_should_be_serviced()

        # second way
        #if self.engine.engine_should_be_serviced():
        #   return True
        #elif self.battery.battery_should_be_serviced():
        #   return True
        #else:
        #   return False
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from car.car import Car


class Calliope(Car):

    def __init__(self, current_mileage, last_serviced_mileage, last_serviced_date):
        self.engine = CapuletEngine(current_mileage, last_serviced_mileage)
        self.battery = SpindlerBattery(last_serviced_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super().need_service()

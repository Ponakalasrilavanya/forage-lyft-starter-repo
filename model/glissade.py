from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from tire.octoprime_tire import Octoprime
from car.car import Car


class Glissade(Car):

    def __init__(self, current_mileage, last_serviced_mileage, last_serviced_date,tire_status = [0]):
        self.engine = WilloughbyEngine(current_mileage, last_serviced_mileage)
        self.battery = SpindlerBattery(last_serviced_date)
        self.tire = Octoprime(tire_status)
        super().__init__(self.engine, self.battery, self.tire)
    def needs_service(self):
        return super().need_service()

from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from car.car import Car


class Palindrome(Car):
    def __init__(self, warning_indicator_is_on, last_serviced_date, tire_status = [0]):
        self.engine = SternmanEngine(warning_indicator_is_on)
        self.battery = SpindlerBattery(last_serviced_date)
        self.tire = CarriganTire(tire_status)
        super().__init__(self.engine, self.battery, self.tire)

    def needs_service(self):
        return super().need_service()

from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from car.car import Car


class Palindrome(Car):
    def __init__(self, warning_indicator_is_on, last_serviced_date):
        self.engine = SternmanEngine(warning_indicator_is_on)
        self.battery = SpindlerBattery(last_serviced_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super().need_service()

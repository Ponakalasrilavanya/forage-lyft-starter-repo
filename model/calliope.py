from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import  CarriganTire
from car.car import Car


class Calliope(Car):

    def __init__(self, current_mileage, last_serviced_mileage, last_serviced_date, tire_status=[0]):
        self.engine = CapuletEngine(current_mileage, last_serviced_mileage)
        self.battery = SpindlerBattery(last_serviced_date)
        self.tire = CarriganTire(tire_status)
        super().__init__(self.engine, self.battery, self.tire)

    def needs_service(self):
        return super().need_service()

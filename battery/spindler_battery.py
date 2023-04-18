from battery.battery import Battery
from datetime import datetime


class SpindlerBattery(Battery):

    def __init__(self, last_serviced_date):
        super().__init__(last_serviced_date)
        self.last_serviced_date = last_serviced_date

    def battery_should_be_serviced(self):
        serviced_date = self.last_serviced_date.replace(year=self.last_serviced_date.year + 3)
        return serviced_date < datetime.today().date()

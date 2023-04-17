from battery.battery import Battery
from datetime import datetime


class NubbinBattery(Battery):
    def __int__(self, last_serviced_date):
        super().__init__(last_serviced_date)
        self.last_serviced_date = last_serviced_date
    def battery_should_be_serviced(self):
        serviced_date = self.last_serviced_date.replace(year=datetime.today().year + 4)
        return serviced_date < datetime.today().date()
        
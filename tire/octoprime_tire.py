from tire.tire import Tire


class Octoprime(Tire):
    def __init__(self, tire_status):
        super().__init__(tire_status)
        self.tire_status = tire_status

    def tire_should_be_serviced(self):
        return sum(self.tire_status) >= 3

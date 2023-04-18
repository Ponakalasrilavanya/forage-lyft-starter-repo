from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_status):
        super().__init__(tire_status)
        self.tire_status = tire_status

    def tire_should_be_serviced(self):
        return max(self.tire_status) >= 0.9
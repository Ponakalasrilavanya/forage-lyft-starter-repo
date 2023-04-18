from tire.carrigan_tire import CarriganTire

import unittest


from battery.nubbin_battery import NubbinBattery


class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_status = [0.4, 0.9, 0.2, 0]

        tire = CarriganTire(tire_status)
        self.assertTrue(tire.tire_should_be_serviced())


    def test_tire_should_not_be_serviced(self):
        tire_status = [0, 0.1, 0.5, 0.6]

        tire = CarriganTire(tire_status)
        self.assertFalse(tire.tire_should_be_serviced())
import unittest


from tire.octoprime_tire import Octoprime


class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_status = [0.8, 0.9, 0.8, 0.7]

        tire = Octoprime(tire_status)
        self.assertTrue(tire.tire_should_be_serviced())


    def test_tire_should_not_be_serviced(self):
        tire_status = [0, 0.1, 0.5, 0.6]

        tire = Octoprime(tire_status)
        self.assertFalse(tire.tire_should_be_serviced())
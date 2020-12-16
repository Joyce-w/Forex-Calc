from unittest import TestCase
from forex import Forex

class ForexTestCase(TestCase):

    def test_valid_curr(self):
        forex_sim = Forex('USD', 'JPN', 304.00)

        self.assertTrue(forex_sim.check_valid_curr('USD'), True)
        self.assertFalse(forex_sim.check_valid_curr('USD92893'), False)
        self.assertNotEqual(forex_sim.check_valid_curr('US'), 3)


# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.speed.kilometres_per_hour

class TestKilometresPerHourMethods(unittest.TestCase):

	def test_convert_known_kilometres_per_hour_to_miles_per_hour(self):
		self.assertAlmostEqual(41.6319, units.speed.kilometres_per_hour.to_miles_per_hour(67.0), places=1)
		self.assertAlmostEqual(7.45645, units.speed.kilometres_per_hour.to_miles_per_hour(12.0), places=1)
		self.assertAlmostEqual(3.91464, units.speed.kilometres_per_hour.to_miles_per_hour(6.3), places=1)

	def test_convert_known_kilometres_per_hour_to_feet_per_second(self):
		self.assertAlmostEqual(4.55672, units.speed.kilometres_per_hour.to_feet_per_second(5.0), places=1)
		self.assertAlmostEqual(1.36702, units.speed.kilometres_per_hour.to_feet_per_second(1.5), places=1)
		self.assertAlmostEqual(81.83873, units.speed.kilometres_per_hour.to_feet_per_second(89.8), places=1)

	def test_convert_known_kilometres_per_hour_to_metres_per_second(self):
		self.assertAlmostEqual(18.6111, units.speed.kilometres_per_hour.to_metres_per_second(67.0), places=1)
		self.assertAlmostEqual(1.63889, units.speed.kilometres_per_hour.to_metres_per_second(5.9), places=1)
		self.assertAlmostEqual(250.0, units.speed.kilometres_per_hour.to_metres_per_second(900.0), places=1)

	def test_convert_known_kilometres_per_hour_to_knots(self):
		self.assertAlmostEqual(485.961, units.speed.kilometres_per_hour.to_knots(900.0), places=1)
		self.assertAlmostEqual(2.10583, units.speed.kilometres_per_hour.to_knots(3.9), places=1)
		self.assertAlmostEqual(6.47948, units.speed.kilometres_per_hour.to_knots(12.0), places=1)

if __name__ == '__main__':
    unittest.main()
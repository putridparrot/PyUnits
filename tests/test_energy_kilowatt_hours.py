# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.energy.kilowatt_hours

class TestKilowattHoursMethods(unittest.TestCase):

	def test_convert_known_kilowatt_hours_to_kilojoules(self):
		self.assertAlmostEqual(2160.0, units.energy.kilowatt_hours.to_kilojoules(0.6), places=1)
		self.assertAlmostEqual(482400.0, units.energy.kilowatt_hours.to_kilojoules(134.0), places=1)
		self.assertAlmostEqual(164160.0, units.energy.kilowatt_hours.to_kilojoules(45.6), places=1)

	def test_convert_known_kilowatt_hours_to_kilocalories(self):
		self.assertAlmostEqual(39235.1976, units.energy.kilowatt_hours.to_kilocalories(45.6), places=1)
		self.assertAlmostEqual(10325.052, units.energy.kilowatt_hours.to_kilocalories(12.0), places=1)
		self.assertAlmostEqual(344.168, units.energy.kilowatt_hours.to_kilocalories(0.4), places=1)

	def test_convert_known_kilowatt_hours_to_joules(self):
		self.assertAlmostEqual(36000.0, units.energy.kilowatt_hours.to_joules(0.01), places=1)
		self.assertAlmostEqual(32400.0, units.energy.kilowatt_hours.to_joules(0.009), places=1)
		self.assertAlmostEqual(7.2e+6, units.energy.kilowatt_hours.to_joules(2.0), places=1)

	def test_convert_known_kilowatt_hours_to_btu(self):
		self.assertAlmostEqual(6824.28, units.energy.kilowatt_hours.to_btu(2.0), places=1)
		self.assertAlmostEqual(2388.4979, units.energy.kilowatt_hours.to_btu(0.7), places=1)
		self.assertAlmostEqual(68.24283, units.energy.kilowatt_hours.to_btu(0.02), places=1)

	def test_convert_known_kilowatt_hours_to_calories(self):
		self.assertAlmostEqual(86042.1, units.energy.kilowatt_hours.to_calories(0.1), places=1)
		self.assertAlmostEqual(60229.47, units.energy.kilowatt_hours.to_calories(0.07), places=1)
		self.assertAlmostEqual(10583.174, units.energy.kilowatt_hours.to_calories(0.0123), places=1)

	def test_convert_known_kilowatt_hours_to_u_s_therms(self):
		self.assertAlmostEqual(0.170648, units.energy.kilowatt_hours.to_u_s_therms(5.0), places=1)
		self.assertAlmostEqual(7.98632, units.energy.kilowatt_hours.to_u_s_therms(234.0), places=1)
		self.assertAlmostEqual(34.16369, units.energy.kilowatt_hours.to_u_s_therms(1001.0), places=1)

	def test_convert_known_kilowatt_hours_to_watt_hours(self):
		self.assertAlmostEqual(123000.0, units.energy.kilowatt_hours.to_watt_hours(123.0), places=1)
		self.assertAlmostEqual(98400.0, units.energy.kilowatt_hours.to_watt_hours(98.4), places=1)
		self.assertAlmostEqual(1600.0, units.energy.kilowatt_hours.to_watt_hours(1.6), places=1)

	def test_convert_known_kilowatt_hours_to_foot_pounds(self):
		self.assertAlmostEqual(2655.196219, units.energy.kilowatt_hours.to_foot_pounds(0.001), places=1)
		self.assertAlmostEqual(238967.6597, units.energy.kilowatt_hours.to_foot_pounds(0.09), places=1)
		self.assertAlmostEqual(1593.1177314, units.energy.kilowatt_hours.to_foot_pounds(0.0006), places=1)

if __name__ == '__main__':
    unittest.main()
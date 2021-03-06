# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.time.years

class TestYearsMethods(unittest.TestCase):

	def test_convert_known_years_to_milliseconds(self):
		self.assertAlmostEqual(31556952.0, units.time.years.to_milliseconds(0.001), places=1)
		self.assertAlmostEqual(28401256.8, units.time.years.to_milliseconds(0.0009), places=1)
		self.assertAlmostEqual(10729363.680000002, units.time.years.to_milliseconds(0.00034), places=1)

	def test_convert_known_years_to_seconds(self):
		self.assertAlmostEqual(1892160.0, units.time.years.to_seconds(0.06), places=1)
		self.assertAlmostEqual(283824.0, units.time.years.to_seconds(0.009), places=1)
		self.assertAlmostEqual(630720.0, units.time.years.to_seconds(0.02), places=1)

	def test_convert_known_years_to_minutes(self):
		self.assertAlmostEqual(10512.0, units.time.years.to_minutes(0.02), places=1)
		self.assertAlmostEqual(157680.0, units.time.years.to_minutes(0.3), places=1)
		self.assertAlmostEqual(525.6, units.time.years.to_minutes(0.001), places=1)

	def test_convert_known_years_to_hours(self):
		self.assertAlmostEqual(8.76, units.time.years.to_hours(0.001), places=1)
		self.assertAlmostEqual(2628.0, units.time.years.to_hours(0.3), places=1)
		self.assertAlmostEqual(17520.0, units.time.years.to_hours(2.0), places=1)

	def test_convert_known_years_to_days(self):
		self.assertAlmostEqual(730.0, units.time.years.to_days(2.0), places=1)
		self.assertAlmostEqual(368285.0, units.time.years.to_days(1009.0), places=1)
		self.assertAlmostEqual(2555.0, units.time.years.to_days(7.0), places=1)

	def test_convert_known_years_to_weeks(self):
		self.assertAlmostEqual(365.0, units.time.years.to_weeks(7.0), places=1)
		self.assertAlmostEqual(67.7857, units.time.years.to_weeks(1.3), places=1)
		self.assertAlmostEqual(4588.5839, units.time.years.to_weeks(88.0), places=1)

	def test_convert_known_years_to_months(self):
		self.assertAlmostEqual(71.9999, units.time.years.to_months(6.0), places=1)
		self.assertAlmostEqual(144.0, units.time.years.to_months(12.0), places=1)
		self.assertAlmostEqual(3.6, units.time.years.to_months(0.3), places=1)

if __name__ == '__main__':
    unittest.main()

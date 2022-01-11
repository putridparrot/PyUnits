# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.time.months

class TestMonthsMethods(unittest.TestCase):

	def test_convert_known_months_to_seconds(self):
		self.assertAlmostEqual(78840.00, units.time.months.to_seconds(0.03), places=1)
		self.assertAlmostEqual(262800.0, units.time.months.to_seconds(0.1), places=1)
		self.assertAlmostEqual(21024.0, units.time.months.to_seconds(0.008), places=1)

	def test_convert_known_months_to_minutes(self):
		self.assertAlmostEqual(30660.0, units.time.months.to_minutes(0.7), places=1)
		self.assertAlmostEqual(61319.99, units.time.months.to_minutes(1.4), places=1)
		self.assertAlmostEqual(219000.0, units.time.months.to_minutes(5.0), places=1)

	def test_convert_known_months_to_hours(self):
		self.assertAlmostEqual(2920.0, units.time.months.to_hours(4.0), places=1)
		self.assertAlmostEqual(219.0, units.time.months.to_hours(0.3), places=1)
		self.assertAlmostEqual(3285.0, units.time.months.to_hours(4.5), places=1)

	def test_convert_known_months_to_days(self):
		self.assertAlmostEqual(136.875, units.time.months.to_days(4.5), places=1)
		self.assertAlmostEqual(2737.53, units.time.months.to_days(90.0), places=1)
		self.assertAlmostEqual(12.1667, units.time.months.to_days(0.4), places=1)

	def test_convert_known_months_to_weeks(self):
		self.assertAlmostEqual(2.17262, units.time.months.to_weeks(0.5), places=1)
		self.assertAlmostEqual(382.359, units.time.months.to_weeks(88.0), places=1)
		self.assertAlmostEqual(54.75006, units.time.months.to_weeks(12.6), places=1)

	def test_convert_known_months_to_years(self):
		self.assertAlmostEqual(1.050001, units.time.months.to_years(12.6), places=1)
		self.assertAlmostEqual(9.08334, units.time.months.to_years(109.0), places=1)
		self.assertAlmostEqual(1.91667, units.time.months.to_years(23.0), places=1)

if __name__ == '__main__':
    unittest.main()
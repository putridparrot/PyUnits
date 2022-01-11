# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.temperature.rankine

class TestRankineMethods(unittest.TestCase):

	def test_convert_known_rankine_to_celsius(self):
		self.assertAlmostEqual(-167.59444444, units.temperature.rankine.to_celsius(190.0), places=1)
		self.assertAlmostEqual(-272.76111111, units.temperature.rankine.to_celsius(0.7), places=1)
		self.assertAlmostEqual(226.85, units.temperature.rankine.to_celsius(900.0), places=1)

	def test_convert_known_rankine_to_fahrenheit(self):
		self.assertAlmostEqual(-350.67, units.temperature.rankine.to_fahrenheit(109.0), places=1)
		self.assertAlmostEqual(3107.33, units.temperature.rankine.to_fahrenheit(3567.0), places=1)
		self.assertAlmostEqual(-450.67, units.temperature.rankine.to_fahrenheit(9.0), places=1)

	def test_convert_known_rankine_to_kelvin(self):
		self.assertAlmostEqual(68.333333333, units.temperature.rankine.to_kelvin(123.0), places=1)
		self.assertAlmostEqual(0.5, units.temperature.rankine.to_kelvin(0.9), places=1)
		self.assertAlmostEqual(12.777777778, units.temperature.rankine.to_kelvin(23.0), places=1)

if __name__ == '__main__':
    unittest.main()

# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.temperature.celsius

class TestCelsiusMethods(unittest.TestCase):

	def test_convert_known_celsius_to_fahrenheit(self):
		self.assertAlmostEqual(89.6, units.temperature.celsius.to_fahrenheit(32.0), places=1)
		self.assertAlmostEqual(33.62, units.temperature.celsius.to_fahrenheit(0.9), places=1)
		self.assertAlmostEqual(32.0, units.temperature.celsius.to_fahrenheit(0.0), places=1)

	def test_convert_known_celsius_to_kelvin(self):
		self.assertAlmostEqual(274.15, units.temperature.celsius.to_kelvin(1.0), places=1)
		self.assertAlmostEqual(283.05, units.temperature.celsius.to_kelvin(9.9), places=1)
		self.assertAlmostEqual(373.15, units.temperature.celsius.to_kelvin(100.0), places=1)

	def test_convert_known_celsius_to_rankine(self):
		self.assertAlmostEqual(2111.67, units.temperature.celsius.to_rankine(900.0), places=1)
		self.assertAlmostEqual(513.27, units.temperature.celsius.to_rankine(12.0), places=1)
		self.assertAlmostEqual(486.27, units.temperature.celsius.to_rankine(-3.0), places=1)

if __name__ == '__main__':
    unittest.main()
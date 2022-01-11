# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.temperature.fahrenheit

class TestFahrenheitMethods(unittest.TestCase):

	def test_convert_known_fahrenheit_to_celsius(self):
		self.assertAlmostEqual(42.7778, units.temperature.fahrenheit.to_celsius(109.0), places=1)
		self.assertAlmostEqual(13.83333, units.temperature.fahrenheit.to_celsius(56.9), places=1)
		self.assertAlmostEqual(38.8889, units.temperature.fahrenheit.to_celsius(102.0), places=1)

	def test_convert_known_fahrenheit_to_kelvin(self):
		self.assertAlmostEqual(274.5389, units.temperature.fahrenheit.to_kelvin(34.5), places=1)
		self.assertAlmostEqual(755.928, units.temperature.fahrenheit.to_kelvin(901.0), places=1)
		self.assertAlmostEqual(268.65, units.temperature.fahrenheit.to_kelvin(23.9), places=1)

	def test_convert_known_fahrenheit_to_rankine(self):
		self.assertAlmostEqual(582.67, units.temperature.fahrenheit.to_rankine(123.0), places=1)
		self.assertAlmostEqual(468.87, units.temperature.fahrenheit.to_rankine(9.2), places=1)
		self.assertAlmostEqual(459.87, units.temperature.fahrenheit.to_rankine(0.2), places=1)

if __name__ == '__main__':
    unittest.main()
# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.temperature.kelvin

class TestKelvinMethods(unittest.TestCase):

	def test_convert_known_kelvin_to_celsius(self):
		self.assertAlmostEqual(-193.15, units.temperature.kelvin.to_celsius(80.0), places=1)
		self.assertAlmostEqual(-272.25, units.temperature.kelvin.to_celsius(0.9), places=1)
		self.assertAlmostEqual(32.0, units.temperature.kelvin.to_celsius(305.15), places=1)

	def test_convert_known_kelvin_to_fahrenheit(self):
		self.assertAlmostEqual(-237.55, units.temperature.kelvin.to_fahrenheit(123.4), places=1)
		self.assertAlmostEqual(980.33, units.temperature.kelvin.to_fahrenheit(800.0), places=1)
		self.assertAlmostEqual(-279.6718, units.temperature.kelvin.to_fahrenheit(99.999), places=1)

	def test_convert_known_kelvin_to_rankine(self):
		self.assertAlmostEqual(280.8, units.temperature.kelvin.to_rankine(156.0), places=1)
		self.assertAlmostEqual(14.76, units.temperature.kelvin.to_rankine(8.2), places=1)
		self.assertAlmostEqual(1.44, units.temperature.kelvin.to_rankine(0.8), places=1)

	def test_convert_known_kelvin_to_reaumur(self):
		self.assertAlmostEqual(501.48, units.temperature.kelvin.to_reaumur(900.0), places=1)
		self.assertAlmostEqual(-217.48, units.temperature.kelvin.to_reaumur(1.3), places=1)
		self.assertAlmostEqual(-170.52, units.temperature.kelvin.to_reaumur(60.0), places=1)

if __name__ == '__main__':
    unittest.main()

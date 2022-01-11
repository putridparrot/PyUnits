# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.mass.pounds

class TestPoundsMethods(unittest.TestCase):

	def test_convert_known_pounds_to_milligrams(self):
		self.assertAlmostEqual(997903.214, units.mass.pounds.to_milligrams(2.2), places=1)
		self.assertAlmostEqual(317514.6589, units.mass.pounds.to_milligrams(0.7), places=1)
		self.assertAlmostEqual(145149.5584, units.mass.pounds.to_milligrams(0.32), places=1)

	def test_convert_known_pounds_to_grams(self):
		self.assertAlmostEqual(136.078, units.mass.pounds.to_grams(0.3), places=1)
		self.assertAlmostEqual(544.311, units.mass.pounds.to_grams(1.2), places=1)
		self.assertAlmostEqual(4082.33, units.mass.pounds.to_grams(9.0), places=1)

	def test_convert_known_pounds_to_kilograms(self):
		self.assertAlmostEqual(2.26796, units.mass.pounds.to_kilograms(5.0), places=1)
		self.assertAlmostEqual(0.498952, units.mass.pounds.to_kilograms(1.1), places=1)
		self.assertAlmostEqual(0.317515, units.mass.pounds.to_kilograms(0.7), places=1)

	def test_convert_known_pounds_to_tonnes(self):
		self.assertAlmostEqual(0.5592794, units.mass.pounds.to_tonnes(1233.0), places=1)
		self.assertAlmostEqual(297.812874, units.mass.pounds.to_tonnes(656565.0), places=1)
		self.assertAlmostEqual(0.408233, units.mass.pounds.to_tonnes(900.0), places=1)

	def test_convert_known_pounds_to_ounces(self):
		self.assertAlmostEqual(720.0, units.mass.pounds.to_ounces(45.0), places=1)
		self.assertAlmostEqual(107.2, units.mass.pounds.to_ounces(6.7), places=1)
		self.assertAlmostEqual(1425.6, units.mass.pounds.to_ounces(89.1), places=1)

	def test_convert_known_pounds_to_stones(self):
		self.assertAlmostEqual(6.364286, units.mass.pounds.to_stones(89.1), places=1)
		self.assertAlmostEqual(0.0857143, units.mass.pounds.to_stones(1.2), places=1)
		self.assertAlmostEqual(56.3571, units.mass.pounds.to_stones(789.0), places=1)

	def test_convert_known_pounds_to_carats(self):
		self.assertAlmostEqual(181436.7522, units.mass.pounds.to_carats(80.0), places=1)
		self.assertAlmostEqual(5307.031, units.mass.pounds.to_carats(2.34), places=1)
		self.assertAlmostEqual(2041.17, units.mass.pounds.to_carats(0.9), places=1)

if __name__ == '__main__':
    unittest.main()
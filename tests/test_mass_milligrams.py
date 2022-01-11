# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.mass.milligrams

class TestMilligramsMethods(unittest.TestCase):

	def test_convert_known_milligrams_to_grams(self):
		self.assertAlmostEqual(0.19, units.mass.milligrams.to_grams(190.0), places=1)
		self.assertAlmostEqual(2.3, units.mass.milligrams.to_grams(2300.0), places=1)
		self.assertAlmostEqual(19.0, units.mass.milligrams.to_grams(19000.0), places=1)

	def test_convert_known_milligrams_to_kilograms(self):
		self.assertAlmostEqual(1.234567, units.mass.milligrams.to_kilograms(1234567.0), places=1)
		self.assertAlmostEqual(0.9008, units.mass.milligrams.to_kilograms(900800.0), places=1)
		self.assertAlmostEqual(7.8, units.mass.milligrams.to_kilograms(7800000.0), places=1)

	def test_convert_known_milligrams_to_tonnes(self):
		self.assertAlmostEqual(0.9, units.mass.milligrams.to_tonnes(900000000.0), places=1)
		self.assertAlmostEqual(0.06, units.mass.milligrams.to_tonnes(60000000.0), places=1)
		self.assertAlmostEqual(0.123456789, units.mass.milligrams.to_tonnes(123456789.0), places=1)

	def test_convert_known_milligrams_to_ounces(self):
		self.assertAlmostEqual(0.2116438, units.mass.milligrams.to_ounces(6000.0), places=1)
		self.assertAlmostEqual(4.35478225, units.mass.milligrams.to_ounces(123456.0), places=1)
		self.assertAlmostEqual(0.282227, units.mass.milligrams.to_ounces(8001.0), places=1)

	def test_convert_known_milligrams_to_pounds(self):
		self.assertAlmostEqual(0.27217389, units.mass.milligrams.to_pounds(123456.0), places=1)
		self.assertAlmostEqual(1.76568226, units.mass.milligrams.to_pounds(800900.0), places=1)
		self.assertAlmostEqual(1.46974694, units.mass.milligrams.to_pounds(666666.0), places=1)

	def test_convert_known_milligrams_to_stones(self):
		self.assertAlmostEqual(0.14172574, units.mass.milligrams.to_stones(900000.0), places=1)
		self.assertAlmostEqual(1.9441115001, units.mass.milligrams.to_stones(12345678.0), places=1)
		self.assertAlmostEqual(0.125994183, units.mass.milligrams.to_stones(800100.0), places=1)

	def test_convert_known_milligrams_to_carats(self):
		self.assertAlmostEqual(3.0, units.mass.milligrams.to_carats(600.0), places=1)
		self.assertAlmostEqual(6.17, units.mass.milligrams.to_carats(1234.0), places=1)
		self.assertAlmostEqual(45.45, units.mass.milligrams.to_carats(9090.0), places=1)

if __name__ == '__main__':
    unittest.main()
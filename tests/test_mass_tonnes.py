# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.mass.tonnes

class TestTonnesMethods(unittest.TestCase):

	def test_convert_known_tonnes_to_milligrams(self):
		self.assertAlmostEqual(9000000.0, units.mass.tonnes.to_milligrams(0.009), places=1)
		self.assertAlmostEqual(810000.0, units.mass.tonnes.to_milligrams(0.00081), places=1)
		self.assertAlmostEqual(1230000.0, units.mass.tonnes.to_milligrams(0.00123), places=1)

	def test_convert_known_tonnes_to_grams(self):
		self.assertAlmostEqual(1230.0, units.mass.tonnes.to_grams(0.00123), places=1)
		self.assertAlmostEqual(800000.0, units.mass.tonnes.to_grams(0.8), places=1)
		self.assertAlmostEqual(30000.0, units.mass.tonnes.to_grams(0.03), places=1)

	def test_convert_known_tonnes_to_kilograms(self):
		self.assertAlmostEqual(30.0, units.mass.tonnes.to_kilograms(0.03), places=1)
		self.assertAlmostEqual(4000.0, units.mass.tonnes.to_kilograms(4.0), places=1)
		self.assertAlmostEqual(1200.0, units.mass.tonnes.to_kilograms(1.2), places=1)

	def test_convert_known_tonnes_to_ounces(self):
		self.assertAlmostEqual(42328.754376824065, units.mass.tonnes.to_ounces(1.2), places=1)
		self.assertAlmostEqual(28219.169584549378, units.mass.tonnes.to_ounces(0.8), places=1)
		self.assertAlmostEqual(35.273962, units.mass.tonnes.to_ounces(0.001), places=1)

	def test_convert_known_tonnes_to_pounds(self):
		self.assertAlmostEqual(2645.55, units.mass.tonnes.to_pounds(1.2), places=1)
		self.assertAlmostEqual(1984.16, units.mass.tonnes.to_pounds(0.9), places=1)
		self.assertAlmostEqual(74957.08, units.mass.tonnes.to_pounds(34.0), places=1)

	def test_convert_known_tonnes_to_stones(self):
		self.assertAlmostEqual(1889.68, units.mass.tonnes.to_stones(12.0), places=1)
		self.assertAlmostEqual(1322.77, units.mass.tonnes.to_stones(8.4), places=1)
		self.assertAlmostEqual(47.2419, units.mass.tonnes.to_stones(0.3), places=1)

	def test_convert_known_tonnes_to_carats(self):
		self.assertAlmostEqual(15000.0, units.mass.tonnes.to_carats(0.003), places=1)
		self.assertAlmostEqual(450000.0, units.mass.tonnes.to_carats(0.09), places=1)
		self.assertAlmostEqual(6000.0, units.mass.tonnes.to_carats(0.0012), places=1)

if __name__ == '__main__':
    unittest.main()

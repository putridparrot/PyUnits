# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.length.yards

class TestYardsMethods(unittest.TestCase):

	def test_convert_known_yards_to_millimetres(self):
		self.assertAlmostEqual(31089.6, units.length.yards.to_millimetres(34.0), places=1)
		self.assertAlmostEqual(822.96, units.length.yards.to_millimetres(0.9), places=1)
		self.assertAlmostEqual(1828.8, units.length.yards.to_millimetres(2.0), places=1)

	def test_convert_known_yards_to_centimetres(self):
		self.assertAlmostEqual(896.112, units.length.yards.to_centimetres(9.8), places=1)
		self.assertAlmostEqual(73.152, units.length.yards.to_centimetres(0.8), places=1)
		self.assertAlmostEqual(1097.28, units.length.yards.to_centimetres(12.0), places=1)

	def test_convert_known_yards_to_metres(self):
		self.assertAlmostEqual(10.9728, units.length.yards.to_metres(12.0), places=1)
		self.assertAlmostEqual(0.64008, units.length.yards.to_metres(0.7), places=1)
		self.assertAlmostEqual(2.7432, units.length.yards.to_metres(3.0), places=1)

	def test_convert_known_yards_to_kilometres(self):
		self.assertAlmostEqual(0.36576, units.length.yards.to_kilometres(400.0), places=1)
		self.assertAlmostEqual(1.73736, units.length.yards.to_kilometres(1900.0), places=1)
		self.assertAlmostEqual(11.288268, units.length.yards.to_kilometres(12345.0), places=1)

	def test_convert_known_yards_to_inches(self):
		self.assertAlmostEqual(828.0, units.length.yards.to_inches(23.0), places=1)
		self.assertAlmostEqual(32.4, units.length.yards.to_inches(0.9), places=1)
		self.assertAlmostEqual(432.0, units.length.yards.to_inches(12.0), places=1)

	def test_convert_known_yards_to_feet(self):
		self.assertAlmostEqual(36.0, units.length.yards.to_feet(12.0), places=1)
		self.assertAlmostEqual(5.4, units.length.yards.to_feet(1.8), places=1)
		self.assertAlmostEqual(201.0, units.length.yards.to_feet(67.0), places=1)

	def test_convert_known_yards_to_miles(self):
		self.assertAlmostEqual(5.056818, units.length.yards.to_miles(8900.0), places=1)
		self.assertAlmostEqual(2.840909, units.length.yards.to_miles(5000.0), places=1)
		self.assertAlmostEqual(70.1454545, units.length.yards.to_miles(123456.0), places=1)

	def test_convert_known_yards_to_nautical_miles(self):
		self.assertAlmostEqual(0.493737, units.length.yards.to_nautical_miles(1000.0), places=1)
		self.assertAlmostEqual(99.7446479, units.length.yards.to_nautical_miles(202020.0), places=1)
		self.assertAlmostEqual(35.513479, units.length.yards.to_nautical_miles(71928.0), places=1)

if __name__ == '__main__':
    unittest.main()

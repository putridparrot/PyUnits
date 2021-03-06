# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.length.feet

class TestFeetMethods(unittest.TestCase):

	def test_convert_known_feet_to_millimetres(self):
		self.assertAlmostEqual(91.44, units.length.feet.to_millimetres(0.3), places=1)
		self.assertAlmostEqual(609.6, units.length.feet.to_millimetres(2.0), places=1)
		self.assertAlmostEqual(18.288, units.length.feet.to_millimetres(0.06), places=1)

	def test_convert_known_feet_to_centimetres(self):
		self.assertAlmostEqual(2.1336, units.length.feet.to_centimetres(0.07), places=1)
		self.assertAlmostEqual(106.68, units.length.feet.to_centimetres(3.5), places=1)
		self.assertAlmostEqual(2712.72, units.length.feet.to_centimetres(89.0), places=1)

	def test_convert_known_feet_to_metres(self):
		self.assertAlmostEqual(274.32, units.length.feet.to_metres(900.0), places=1)
		self.assertAlmostEqual(0.36576, units.length.feet.to_metres(1.2), places=1)
		self.assertAlmostEqual(0.24384, units.length.feet.to_metres(0.8), places=1)

	def test_convert_known_feet_to_kilometres(self):
		self.assertAlmostEqual(0.6092952, units.length.feet.to_kilometres(1999.0), places=1)
		self.assertAlmostEqual(37.6293888, units.length.feet.to_kilometres(123456.0), places=1)
		self.assertAlmostEqual(0.24384, units.length.feet.to_kilometres(800.0), places=1)

	def test_convert_known_feet_to_inches(self):
		self.assertAlmostEqual(96.0, units.length.feet.to_inches(8.0), places=1)
		self.assertAlmostEqual(14.4, units.length.feet.to_inches(1.2), places=1)
		self.assertAlmostEqual(4.8, units.length.feet.to_inches(0.4), places=1)

	def test_convert_known_feet_to_yards(self):
		self.assertAlmostEqual(26.0, units.length.feet.to_yards(78.0), places=1)
		self.assertAlmostEqual(0.0333333, units.length.feet.to_yards(0.1), places=1)
		self.assertAlmostEqual(2387.333, units.length.feet.to_yards(7162.0), places=1)

	def test_convert_known_feet_to_miles(self):
		self.assertAlmostEqual(1.704545, units.length.feet.to_miles(9000.0), places=1)
		self.assertAlmostEqual(0.3785985, units.length.feet.to_miles(1999.0), places=1)
		self.assertAlmostEqual(0.9507576, units.length.feet.to_miles(5020.0), places=1)

	def test_convert_known_feet_to_nautical_miles(self):
		self.assertAlmostEqual(1.442533, units.length.feet.to_nautical_miles(8765.0), places=1)
		self.assertAlmostEqual(3.1269978, units.length.feet.to_nautical_miles(19000.0), places=1)
		self.assertAlmostEqual(0.164579, units.length.feet.to_nautical_miles(1000.0), places=1)

if __name__ == '__main__':
    unittest.main()

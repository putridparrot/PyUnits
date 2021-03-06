# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.angle.milliradians

class TestMilliradiansMethods(unittest.TestCase):

	def test_convert_known_milliradians_to_degrees(self):
		self.assertAlmostEqual(0.338045, units.angle.milliradians.to_degrees(5.9), places=1)
		self.assertAlmostEqual(6.24524, units.angle.milliradians.to_degrees(109.0), places=1)
		self.assertAlmostEqual(401.5861, units.angle.milliradians.to_degrees(7009.0), places=1)
		self.assertAlmostEqual(23333.11, units.angle.milliradians.to_degrees(407239.5873), places=1)

	def test_convert_known_milliradians_to_radians(self):
		self.assertAlmostEqual(8.011, units.angle.milliradians.to_radians(8011.0), places=1)
		self.assertAlmostEqual(7.689, units.angle.milliradians.to_radians(7689.0), places=1)
		self.assertAlmostEqual(0.129, units.angle.milliradians.to_radians(129.0), places=1)

	def test_convert_known_milliradians_to_gradians(self):
		self.assertAlmostEqual(8.2124, units.angle.milliradians.to_gradians(129.0), places=1)
		self.assertAlmostEqual(50.9296, units.angle.milliradians.to_gradians(800.0), places=1)
		self.assertAlmostEqual(0.8206029, units.angle.milliradians.to_gradians(12.89), places=1)

	def test_convert_known_milliradians_to_minute_of_arc(self):
		self.assertAlmostEqual(41.253, units.angle.milliradians.to_minute_of_arc(12.0), places=1)
		self.assertAlmostEqual(3.09397, units.angle.milliradians.to_minute_of_arc(0.9), places=1)
		self.assertAlmostEqual(2750.2, units.angle.milliradians.to_minute_of_arc(800.0), places=1)

	def test_convert_known_milliradians_to_seconds_of_arc(self):
		self.assertAlmostEqual(13819.742, units.angle.milliradians.to_seconds_of_arc(67.0), places=1)
		self.assertAlmostEqual(185638.32562238674, units.angle.milliradians.to_seconds_of_arc(900.0), places=1)
		self.assertAlmostEqual(167590.16, units.angle.milliradians.to_seconds_of_arc(812.5), places=1)

if __name__ == '__main__':
    unittest.main()

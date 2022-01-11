# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.area.square_kilometres

class TestSquareKilometresMethods(unittest.TestCase):

	def test_convert_known_square_kilometres_to_square_metres(self):
		self.assertAlmostEqual(120000.0, units.area.square_kilometres.to_square_metres(0.12), places=1)
		self.assertAlmostEqual(900000.0, units.area.square_kilometres.to_square_metres(0.9), places=1)
		self.assertAlmostEqual(8123456.0, units.area.square_kilometres.to_square_metres(8.123456), places=1)

	def test_convert_known_square_kilometres_to_square_miles(self):
		self.assertAlmostEqual(190.0, units.area.square_kilometres.to_square_miles(492.098), places=1)
		self.assertAlmostEqual(9.0, units.area.square_kilometres.to_square_miles(23.3099), places=1)
		self.assertAlmostEqual(1800.0, units.area.square_kilometres.to_square_miles(4661.979), places=1)

	def test_convert_known_square_kilometres_to_square_yards(self):
		self.assertAlmostEqual(189000.0005, units.area.square_kilometres.to_square_yards(0.158028071), places=1)
		self.assertAlmostEqual(9999999.0310, units.area.square_kilometres.to_square_yards(8.361272764), places=1)
		self.assertAlmostEqual(717594.030, units.area.square_kilometres.to_square_yards(0.6), places=1)

	def test_convert_known_square_kilometres_to_square_feet(self):
		self.assertAlmostEqual(96875.194, units.area.square_kilometres.to_square_feet(0.009), places=1)
		self.assertAlmostEqual(861112.833, units.area.square_kilometres.to_square_feet(0.08), places=1)
		self.assertAlmostEqual(1323960.9812553, units.area.square_kilometres.to_square_feet(0.123), places=1)

	def test_convert_known_square_kilometres_to_square_inches(self):
		self.assertAlmostEqual(1240002.48, units.area.square_kilometres.to_square_inches(0.0008), places=1)
		self.assertAlmostEqual(1906503.813, units.area.square_kilometres.to_square_inches(0.00123), places=1)
		self.assertAlmostEqual(69750.1395, units.area.square_kilometres.to_square_inches(0.000045), places=1)

	def test_convert_known_square_kilometres_to_hectares(self):
		self.assertAlmostEqual(19000.0, units.area.square_kilometres.to_hectares(190.0), places=1)
		self.assertAlmostEqual(5567.0, units.area.square_kilometres.to_hectares(55.67), places=1)
		self.assertAlmostEqual(90.0, units.area.square_kilometres.to_hectares(0.9), places=1)

	def test_convert_known_square_kilometres_to_acres(self):
		self.assertAlmostEqual(7510.4999900100, units.area.square_kilometres.to_acres(30.393962), places=1)
		self.assertAlmostEqual(13368.3805, units.area.square_kilometres.to_acres(54.1), places=1)
		self.assertAlmostEqual(22405.0103, units.area.square_kilometres.to_acres(90.67), places=1)

if __name__ == '__main__':
    unittest.main()
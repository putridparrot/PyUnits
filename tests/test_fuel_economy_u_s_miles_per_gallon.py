# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.fuel_economy.u_s_miles_per_gallon

class TestUSMilesPerGallonMethods(unittest.TestCase):

	def test_convert_known_u_s_miles_per_gallon_to_kilometre_per_litre(self):
		self.assertAlmostEqual(9.77831, units.fuel_economy.u_s_miles_per_gallon.to_kilometre_per_litre(23.0), places=1)
		self.assertAlmostEqual(2.97601, units.fuel_economy.u_s_miles_per_gallon.to_kilometre_per_litre(7.0), places=1)
		self.assertAlmostEqual(0.382629, units.fuel_economy.u_s_miles_per_gallon.to_kilometre_per_litre(0.9), places=1)

	def test_convert_known_u_s_miles_per_gallon_to_miles_per_gallon(self):
		self.assertAlmostEqual(130.9036, units.fuel_economy.u_s_miles_per_gallon.to_miles_per_gallon(109.0), places=1)
		self.assertAlmostEqual(93.91432, units.fuel_economy.u_s_miles_per_gallon.to_miles_per_gallon(78.2), places=1)
		self.assertAlmostEqual(1.08086, units.fuel_economy.u_s_miles_per_gallon.to_miles_per_gallon(0.9), places=1)

if __name__ == '__main__':
    unittest.main()

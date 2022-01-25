# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.fuel_economy.kilometre_per_litre

class TestKilometrePerLitreMethods(unittest.TestCase):

	def test_convert_known_kilometre_per_litre_to_u_s_miles_per_gallon(self):
		self.assertAlmostEqual(256.384, units.fuel_economy.kilometre_per_litre.to_u_s_miles_per_gallon(109.0), places=1)
		self.assertAlmostEqual(22.1102, units.fuel_economy.kilometre_per_litre.to_u_s_miles_per_gallon(9.4), places=1)
		self.assertAlmostEqual(3.05779, units.fuel_economy.kilometre_per_litre.to_u_s_miles_per_gallon(1.3), places=1)

	def test_convert_known_kilometre_per_litre_to_miles_per_gallon(self):
		self.assertAlmostEqual(14.124, units.fuel_economy.kilometre_per_litre.to_miles_per_gallon(5.0), places=1)
		self.assertAlmostEqual(508.466, units.fuel_economy.kilometre_per_litre.to_miles_per_gallon(180.0), places=1)
		self.assertAlmostEqual(15.254, units.fuel_economy.kilometre_per_litre.to_miles_per_gallon(5.4), places=1)

	def test_convert_known_kilometre_per_litre_to_litres_per100_kilometres(self):
		self.assertAlmostEqual(0.917431, units.fuel_economy.kilometre_per_litre.to_litres_per100_kilometres(109.0), places=1)
		self.assertAlmostEqual(125.0, units.fuel_economy.kilometre_per_litre.to_litres_per100_kilometres(0.8), places=1)
		self.assertAlmostEqual(43.4783, units.fuel_economy.kilometre_per_litre.to_litres_per100_kilometres(2.3), places=1)

if __name__ == '__main__':
    unittest.main()

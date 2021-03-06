# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.fuel_economy.miles_per_gallon

class TestMilesPerGallonMethods(unittest.TestCase):

	def test_convert_known_miles_per_gallon_to_kilometre_per_litre(self):
		self.assertAlmostEqual(4.24807, units.fuel_economy.miles_per_gallon.to_kilometre_per_litre(12.0), places=1)
		self.assertAlmostEqual(2.90285, units.fuel_economy.miles_per_gallon.to_kilometre_per_litre(8.2), places=1)
		self.assertAlmostEqual(0.177003, units.fuel_economy.miles_per_gallon.to_kilometre_per_litre(0.5), places=1)

	def test_convert_known_miles_per_gallon_to_u_s_miles_per_gallon(self):
		self.assertAlmostEqual(1.16574, units.fuel_economy.miles_per_gallon.to_u_s_miles_per_gallon(1.4), places=1)
		self.assertAlmostEqual(839.3356, units.fuel_economy.miles_per_gallon.to_u_s_miles_per_gallon(1008.0), places=1)
		self.assertAlmostEqual(0.666139, units.fuel_economy.miles_per_gallon.to_u_s_miles_per_gallon(0.8), places=1)

	def test_convert_known_miles_per_gallon_to_litres_per100_kilometres(self):
		self.assertAlmostEqual(12.66731, units.fuel_economy.miles_per_gallon.to_litres_per100_kilometres(22.3), places=1)
		self.assertAlmostEqual(706.202, units.fuel_economy.miles_per_gallon.to_litres_per100_kilometres(0.4), places=1)
		self.assertAlmostEqual(54.3233, units.fuel_economy.miles_per_gallon.to_litres_per100_kilometres(5.2), places=1)

if __name__ == '__main__':
    unittest.main()

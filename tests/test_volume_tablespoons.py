# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.volume.tablespoons

class TestTablespoonsMethods(unittest.TestCase):

	def test_convert_known_tablespoons_to_millilitres(self):
		self.assertAlmostEqual(47.9471, units.volume.tablespoons.to_millilitres(2.7), places=1)
		self.assertAlmostEqual(11.54281, units.volume.tablespoons.to_millilitres(0.65), places=1)
		self.assertAlmostEqual(1422.43, units.volume.tablespoons.to_millilitres(80.1), places=1)

	def test_convert_known_tablespoons_to_litres(self):
		self.assertAlmostEqual(0.976699, units.volume.tablespoons.to_litres(55.0), places=1)
		self.assertAlmostEqual(3.37405, units.volume.tablespoons.to_litres(190.0), places=1)
		self.assertAlmostEqual(71.0397889, units.volume.tablespoons.to_litres(4000.0), places=1)

	def test_convert_known_tablespoons_to_kilolitres(self):
		self.assertAlmostEqual(0.1775817, units.volume.tablespoons.to_kilolitres(10000.0), places=1)
		self.assertAlmostEqual(1.7538858, units.volume.tablespoons.to_kilolitres(98765.0), places=1)
		self.assertAlmostEqual(11.8446826, units.volume.tablespoons.to_kilolitres(666999.0), places=1)

	def test_convert_known_tablespoons_to_teaspoons(self):
		self.assertAlmostEqual(36.0, units.volume.tablespoons.to_teaspoons(12.0), places=1)
		self.assertAlmostEqual(0.72, units.volume.tablespoons.to_teaspoons(0.24), places=1)
		self.assertAlmostEqual(59.7, units.volume.tablespoons.to_teaspoons(19.9), places=1)

	def test_convert_known_tablespoons_to_quarts(self):
		self.assertAlmostEqual(2.96875, units.volume.tablespoons.to_quarts(190.0), places=1)
		self.assertAlmostEqual(0.140625, units.volume.tablespoons.to_quarts(9.0), places=1)
		self.assertAlmostEqual(0.0578125, units.volume.tablespoons.to_quarts(3.7), places=1)

	def test_convert_known_tablespoons_to_pints(self):
		self.assertAlmostEqual(0.146875, units.volume.tablespoons.to_pints(4.7), places=1)
		self.assertAlmostEqual(5.9375, units.volume.tablespoons.to_pints(190.0), places=1)
		self.assertAlmostEqual(34.0906391, units.volume.tablespoons.to_pints(1090.9), places=1)

	def test_convert_known_tablespoons_to_gallons(self):
		self.assertAlmostEqual(31.25001, units.volume.tablespoons.to_gallons(8000.0), places=1)
		self.assertAlmostEqual(0.210938, units.volume.tablespoons.to_gallons(54.0), places=1)
		self.assertAlmostEqual(0.3878908, units.volume.tablespoons.to_gallons(99.3), places=1)

	def test_convert_known_tablespoons_to_fluid_ounces(self):
		self.assertAlmostEqual(50.50002, units.volume.tablespoons.to_fluid_ounces(80.8), places=1)
		self.assertAlmostEqual(5630.627, units.volume.tablespoons.to_fluid_ounces(9009.0), places=1)
		self.assertAlmostEqual(7.875003, units.volume.tablespoons.to_fluid_ounces(12.6), places=1)

	def test_convert_known_tablespoons_to_u_s_teaspoons(self):
		self.assertAlmostEqual(43.2342, units.volume.tablespoons.to_u_s_teaspoons(12.0), places=1)
		self.assertAlmostEqual(2.16171, units.volume.tablespoons.to_u_s_teaspoons(0.6), places=1)
		self.assertAlmostEqual(190.5909, units.volume.tablespoons.to_u_s_teaspoons(52.9), places=1)

	def test_convert_known_tablespoons_to_u_s_tablespoons(self):
		self.assertAlmostEqual(80.4637, units.volume.tablespoons.to_u_s_tablespoons(67.0), places=1)
		self.assertAlmostEqual(6.96551, units.volume.tablespoons.to_u_s_tablespoons(5.8), places=1)
		self.assertAlmostEqual(0.2762186, units.volume.tablespoons.to_u_s_tablespoons(0.23), places=1)

	def test_convert_known_tablespoons_to_u_s_quarts(self):
		self.assertAlmostEqual(1.0133, units.volume.tablespoons.to_u_s_quarts(54.0), places=1)
		self.assertAlmostEqual(18.875563, units.volume.tablespoons.to_u_s_quarts(1005.9), places=1)
		self.assertAlmostEqual(0.0168884, units.volume.tablespoons.to_u_s_quarts(0.9), places=1)

	def test_convert_known_tablespoons_to_u_s_pints(self):
		self.assertAlmostEqual(1.27601, units.volume.tablespoons.to_u_s_pints(34.0), places=1)
		self.assertAlmostEqual(4.1019963, units.volume.tablespoons.to_u_s_pints(109.3), places=1)
		self.assertAlmostEqual(7.13064, units.volume.tablespoons.to_u_s_pints(190.0), places=1)

	def test_convert_known_tablespoons_to_u_s_gallons(self):
		self.assertAlmostEqual(4.22209, units.volume.tablespoons.to_u_s_gallons(900.0), places=1)
		self.assertAlmostEqual(0.0131354, units.volume.tablespoons.to_u_s_gallons(2.8), places=1)
		self.assertAlmostEqual(6.891391, units.volume.tablespoons.to_u_s_gallons(1469.0), places=1)

	def test_convert_known_tablespoons_to_u_s_fluid_ounces(self):
		self.assertAlmostEqual(605.8795, units.volume.tablespoons.to_u_s_fluid_ounces(1009.0), places=1)
		self.assertAlmostEqual(4.9239, units.volume.tablespoons.to_u_s_fluid_ounces(8.2), places=1)
		self.assertAlmostEqual(114.39053, units.volume.tablespoons.to_u_s_fluid_ounces(190.5), places=1)

	def test_convert_known_tablespoons_to_u_s_cups(self):
		self.assertAlmostEqual(8.18147, units.volume.tablespoons.to_u_s_cups(109.0), places=1)
		self.assertAlmostEqual(0.255202, units.volume.tablespoons.to_u_s_cups(3.4), places=1)
		self.assertAlmostEqual(75.0594, units.volume.tablespoons.to_u_s_cups(1000.0), places=1)

	def test_convert_known_tablespoons_to_cubic_metres(self):
		self.assertAlmostEqual(0.1775817, units.volume.tablespoons.to_cubic_metres(10000.0), places=1)
		self.assertAlmostEqual(0.059999995422, units.volume.tablespoons.to_cubic_metres(3378.726), places=1)
		self.assertAlmostEqual(14.2066969, units.volume.tablespoons.to_cubic_metres(800009.0), places=1)

	def test_convert_known_tablespoons_to_cubic_feet(self):
		self.assertAlmostEqual(0.489157, units.volume.tablespoons.to_cubic_feet(780.0), places=1)
		self.assertAlmostEqual(4.0, units.volume.tablespoons.to_cubic_feet(6378.32), places=1)
		self.assertAlmostEqual(5.3, units.volume.tablespoons.to_cubic_feet(8451.28), places=1)

	def test_convert_known_tablespoons_to_cubic_inches(self):
		self.assertAlmostEqual(71.5222, units.volume.tablespoons.to_cubic_inches(66.0), places=1)
		self.assertAlmostEqual(133.291, units.volume.tablespoons.to_cubic_inches(123.0), places=1)
		self.assertAlmostEqual(60.6855, units.volume.tablespoons.to_cubic_inches(56.0), places=1)

	def test_convert_known_tablespoons_to_oil_barrels(self):
		self.assertAlmostEqual(5.0, units.volume.tablespoons.to_oil_barrels(44764.5), places=1)
		self.assertAlmostEqual(1.3651429, units.volume.tablespoons.to_oil_barrels(12222.0), places=1)
		self.assertAlmostEqual(0.0893564, units.volume.tablespoons.to_oil_barrels(800.0), places=1)

if __name__ == '__main__':
    unittest.main()

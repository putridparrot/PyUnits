# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.volume.litres

class TestLitresMethods(unittest.TestCase):

	def test_convert_known_litres_to_millilitres(self):
		self.assertAlmostEqual(34000.0, units.volume.litres.to_millilitres(34.0), places=1)
		self.assertAlmostEqual(670.0, units.volume.litres.to_millilitres(0.67), places=1)
		self.assertAlmostEqual(1090.0, units.volume.litres.to_millilitres(1.09), places=1)

	def test_convert_known_litres_to_kilolitres(self):
		self.assertAlmostEqual(0.2, units.volume.litres.to_kilolitres(200.0), places=1)
		self.assertAlmostEqual(12.345, units.volume.litres.to_kilolitres(12345.0), places=1)
		self.assertAlmostEqual(0.08, units.volume.litres.to_kilolitres(80.0), places=1)

	def test_convert_known_litres_to_teaspoons(self):
		self.assertAlmostEqual(506.809, units.volume.litres.to_teaspoons(3.0), places=1)
		self.assertAlmostEqual(33.7873, units.volume.litres.to_teaspoons(0.2), places=1)
		self.assertAlmostEqual(709.533, units.volume.litres.to_teaspoons(4.2), places=1)

	def test_convert_known_litres_to_tablespoons(self):
		self.assertAlmostEqual(168.936, units.volume.litres.to_tablespoons(3.0), places=1)
		self.assertAlmostEqual(22.5248, units.volume.litres.to_tablespoons(0.4), places=1)
		self.assertAlmostEqual(3772.91, units.volume.litres.to_tablespoons(67.0), places=1)

	def test_convert_known_litres_to_quarts(self):
		self.assertAlmostEqual(47.5134, units.volume.litres.to_quarts(54.0), places=1)
		self.assertAlmostEqual(1.75975, units.volume.litres.to_quarts(2.0), places=1)
		self.assertAlmostEqual(0.615914, units.volume.litres.to_quarts(0.7), places=1)

	def test_convert_known_litres_to_pints(self):
		self.assertAlmostEqual(0.879877, units.volume.litres.to_pints(0.5), places=1)
		self.assertAlmostEqual(255.164, units.volume.litres.to_pints(145.0), places=1)
		self.assertAlmostEqual(16.0138, units.volume.litres.to_pints(9.1), places=1)

	def test_convert_known_litres_to_gallons(self):
		self.assertAlmostEqual(2.837603, units.volume.litres.to_gallons(12.9), places=1)
		self.assertAlmostEqual(23.9766, units.volume.litres.to_gallons(109.0), places=1)
		self.assertAlmostEqual(14.7379, units.volume.litres.to_gallons(67.0), places=1)

	def test_convert_known_litres_to_fluid_ounces(self):
		self.assertAlmostEqual(175.975, units.volume.litres.to_fluid_ounces(5.0), places=1)
		self.assertAlmostEqual(10.5585, units.volume.litres.to_fluid_ounces(0.3), places=1)
		self.assertAlmostEqual(38.7146, units.volume.litres.to_fluid_ounces(1.1), places=1)

	def test_convert_known_litres_to_u_s_teaspoons(self):
		self.assertAlmostEqual(2434.61, units.volume.litres.to_u_s_teaspoons(12.0), places=1)
		self.assertAlmostEqual(142.019, units.volume.litres.to_u_s_teaspoons(0.7), places=1)
		self.assertAlmostEqual(18239.29, units.volume.litres.to_u_s_teaspoons(89.9), places=1)

	def test_convert_known_litres_to_u_s_tablespoons(self):
		self.assertAlmostEqual(811.537, units.volume.litres.to_u_s_tablespoons(12.0), places=1)
		self.assertAlmostEqual(378.717, units.volume.litres.to_u_s_tablespoons(5.6), places=1)
		self.assertAlmostEqual(33.814, units.volume.litres.to_u_s_tablespoons(0.5), places=1)

	def test_convert_known_litres_to_u_s_quarts(self):
		self.assertAlmostEqual(12.6803, units.volume.litres.to_u_s_quarts(12.0), places=1)
		self.assertAlmostEqual(1.15179, units.volume.litres.to_u_s_quarts(1.09), places=1)
		self.assertAlmostEqual(5.81179, units.volume.litres.to_u_s_quarts(5.5), places=1)

	def test_convert_known_litres_to_u_s_pints(self):
		self.assertAlmostEqual(7.18548, units.volume.litres.to_u_s_pints(3.4), places=1)
		self.assertAlmostEqual(1.6907, units.volume.litres.to_u_s_pints(0.8), places=1)
		self.assertAlmostEqual(6340.129, units.volume.litres.to_u_s_pints(3000.0), places=1)

	def test_convert_known_litres_to_u_s_gallons(self):
		self.assertAlmostEqual(28.821171, units.volume.litres.to_u_s_gallons(109.1), places=1)
		self.assertAlmostEqual(10.96314, units.volume.litres.to_u_s_gallons(41.5), places=1)
		self.assertAlmostEqual(0.211338, units.volume.litres.to_u_s_gallons(0.8), places=1)

	def test_convert_known_litres_to_u_s_fluid_ounces(self):
		self.assertAlmostEqual(2738.94, units.volume.litres.to_u_s_fluid_ounces(81.0), places=1)
		self.assertAlmostEqual(246.842, units.volume.litres.to_u_s_fluid_ounces(7.3), places=1)
		self.assertAlmostEqual(21.97911, units.volume.litres.to_u_s_fluid_ounces(0.65), places=1)

	def test_convert_known_litres_to_u_s_cups(self):
		self.assertAlmostEqual(3.80408, units.volume.litres.to_u_s_cups(0.9), places=1)
		self.assertAlmostEqual(439.15962, units.volume.litres.to_u_s_cups(103.9), places=1)
		self.assertAlmostEqual(302.6355, units.volume.litres.to_u_s_cups(71.6), places=1)

	def test_convert_known_litres_to_cubic_metres(self):
		self.assertAlmostEqual(0.4005, units.volume.litres.to_cubic_metres(400.5), places=1)
		self.assertAlmostEqual(0.9, units.volume.litres.to_cubic_metres(900.0), places=1)
		self.assertAlmostEqual(6.09, units.volume.litres.to_cubic_metres(6090.0), places=1)

	def test_convert_known_litres_to_cubic_feet(self):
		self.assertAlmostEqual(0.176573, units.volume.litres.to_cubic_feet(5.0), places=1)
		self.assertAlmostEqual(3.0, units.volume.litres.to_cubic_feet(84.9505), places=1)
		self.assertAlmostEqual(0.211888, units.volume.litres.to_cubic_feet(6.0), places=1)

	def test_convert_known_litres_to_cubic_inches(self):
		self.assertAlmostEqual(40641.7842, units.volume.litres.to_cubic_inches(666.0), places=1)
		self.assertAlmostEqual(48086.675599, units.volume.litres.to_cubic_inches(788.0), places=1)
		self.assertAlmostEqual(244.095, units.volume.litres.to_cubic_inches(4.0), places=1)

	def test_convert_known_litres_to_oil_barrels(self):
		self.assertAlmostEqual(55.0, units.volume.litres.to_oil_barrels(8744.3), places=1)
		self.assertAlmostEqual(7.761626, units.volume.litres.to_oil_barrels(1234.0), places=1)
		self.assertAlmostEqual(6.0, units.volume.litres.to_oil_barrels(953.924), places=1)

if __name__ == '__main__':
    unittest.main()

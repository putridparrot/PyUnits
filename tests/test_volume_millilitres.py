# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.volume.millilitres

class TestMillilitresMethods(unittest.TestCase):

	def test_convert_known_millilitres_to_litres(self):
		self.assertAlmostEqual(1.9, units.volume.millilitres.to_litres(1900.0), places=1)
		self.assertAlmostEqual(56.789, units.volume.millilitres.to_litres(56789.0), places=1)
		self.assertAlmostEqual(0.567, units.volume.millilitres.to_litres(567.0), places=1)

	def test_convert_known_millilitres_to_kilolitres(self):
		self.assertAlmostEqual(10.06, units.volume.millilitres.to_kilolitres(10060000.0), places=1)
		self.assertAlmostEqual(0.987654, units.volume.millilitres.to_kilolitres(987654.0), places=1)
		self.assertAlmostEqual(0.405, units.volume.millilitres.to_kilolitres(405000.0), places=1)

	def test_convert_known_millilitres_to_teaspoons(self):
		self.assertAlmostEqual(0.168936, units.volume.millilitres.to_teaspoons(1.0), places=1)
		self.assertAlmostEqual(9.46043, units.volume.millilitres.to_teaspoons(56.0), places=1)
		self.assertAlmostEqual(2.077917, units.volume.millilitres.to_teaspoons(12.3), places=1)

	def test_convert_known_millilitres_to_tablespoons(self):
		self.assertAlmostEqual(6.13802, units.volume.millilitres.to_tablespoons(109.0), places=1)
		self.assertAlmostEqual(4.95547, units.volume.millilitres.to_tablespoons(88.0), places=1)
		self.assertAlmostEqual(0.675745, units.volume.millilitres.to_tablespoons(12.0), places=1)

	def test_convert_known_millilitres_to_quarts(self):
		self.assertAlmostEqual(0.783091, units.volume.millilitres.to_quarts(890.0), places=1)
		self.assertAlmostEqual(10.862081, units.volume.millilitres.to_quarts(12345.0), places=1)
		self.assertAlmostEqual(0.113504, units.volume.millilitres.to_quarts(129.0), places=1)

	def test_convert_known_millilitres_to_pints(self):
		self.assertAlmostEqual(0.218209, units.volume.millilitres.to_pints(124.0), places=1)
		self.assertAlmostEqual(0.174216, units.volume.millilitres.to_pints(99.0), places=1)
		self.assertAlmostEqual(1.0686986, units.volume.millilitres.to_pints(607.3), places=1)

	def test_convert_known_millilitres_to_gallons(self):
		self.assertAlmostEqual(0.2714421, units.volume.millilitres.to_gallons(1234.0), places=1)
		self.assertAlmostEqual(1.979723, units.volume.millilitres.to_gallons(9000.0), places=1)
		self.assertAlmostEqual(2.2458816257, units.volume.millilitres.to_gallons(10209.98), places=1)

	def test_convert_known_millilitres_to_fluid_ounces(self):
		self.assertAlmostEqual(2.74522, units.volume.millilitres.to_fluid_ounces(78.0), places=1)
		self.assertAlmostEqual(0.4540165, units.volume.millilitres.to_fluid_ounces(12.9), places=1)
		self.assertAlmostEqual(35.51184, units.volume.millilitres.to_fluid_ounces(1009.0), places=1)

	def test_convert_known_millilitres_to_u_s_teaspoons(self):
		self.assertAlmostEqual(20.2884, units.volume.millilitres.to_u_s_teaspoons(100.0), places=1)
		self.assertAlmostEqual(2.495476, units.volume.millilitres.to_u_s_teaspoons(12.3), places=1)
		self.assertAlmostEqual(13.999, units.volume.millilitres.to_u_s_teaspoons(69.0), places=1)

	def test_convert_known_millilitres_to_u_s_tablespoons(self):
		self.assertAlmostEqual(2.56987, units.volume.millilitres.to_u_s_tablespoons(38.0), places=1)
		self.assertAlmostEqual(69.18349, units.volume.millilitres.to_u_s_tablespoons(1023.0), places=1)
		self.assertAlmostEqual(6.00537, units.volume.millilitres.to_u_s_tablespoons(88.8), places=1)

	def test_convert_known_millilitres_to_u_s_quarts(self):
		self.assertAlmostEqual(1.066198, units.volume.millilitres.to_u_s_quarts(1009.0), places=1)
		self.assertAlmostEqual(4.825895, units.volume.millilitres.to_u_s_quarts(4567.0), places=1)
		self.assertAlmostEqual(8.463016, units.volume.millilitres.to_u_s_quarts(8009.0), places=1)

	def test_convert_known_millilitres_to_u_s_pints(self):
		self.assertAlmostEqual(0.232471, units.volume.millilitres.to_u_s_pints(110.0), places=1)
		self.assertAlmostEqual(4.294381, units.volume.millilitres.to_u_s_pints(2032.0), places=1)
		self.assertAlmostEqual(2.11527846, units.volume.millilitres.to_u_s_pints(1000.9), places=1)

	def test_convert_known_millilitres_to_u_s_gallons(self):
		self.assertAlmostEqual(1.32086, units.volume.millilitres.to_u_s_gallons(5000.0), places=1)
		self.assertAlmostEqual(32.6136249, units.volume.millilitres.to_u_s_gallons(123456.0), places=1)
		self.assertAlmostEqual(0.237755, units.volume.millilitres.to_u_s_gallons(900.0), places=1)

	def test_convert_known_millilitres_to_u_s_fluid_ounces(self):
		self.assertAlmostEqual(2.26554, units.volume.millilitres.to_u_s_fluid_ounces(67.0), places=1)
		self.assertAlmostEqual(0.4260567, units.volume.millilitres.to_u_s_fluid_ounces(12.6), places=1)
		self.assertAlmostEqual(372.25858, units.volume.millilitres.to_u_s_fluid_ounces(11009.0), places=1)

	def test_convert_known_millilitres_to_u_s_cups(self):
		self.assertAlmostEqual(1.47091, units.volume.millilitres.to_u_s_cups(348.0), places=1)
		self.assertAlmostEqual(0.05452511, units.volume.millilitres.to_u_s_cups(12.9), places=1)
		self.assertAlmostEqual(2.95873, units.volume.millilitres.to_u_s_cups(700.0), places=1)

	def test_convert_known_millilitres_to_cubic_metres(self):
		self.assertAlmostEqual(9.999999, units.volume.millilitres.to_cubic_metres(9999999.0), places=1)
		self.assertAlmostEqual(0.123456, units.volume.millilitres.to_cubic_metres(123456.0), places=1)
		self.assertAlmostEqual(0.4005, units.volume.millilitres.to_cubic_metres(400500.0), places=1)

	def test_convert_known_millilitres_to_cubic_feet(self):
		self.assertAlmostEqual(9.0, units.volume.millilitres.to_cubic_feet(254852.0), places=1)
		self.assertAlmostEqual(0.211888, units.volume.millilitres.to_cubic_feet(6000.0), places=1)
		self.assertAlmostEqual(2.5, units.volume.millilitres.to_cubic_feet(70792.1), places=1)

	def test_convert_known_millilitres_to_cubic_inches(self):
		self.assertAlmostEqual(47.4154, units.volume.millilitres.to_cubic_inches(777.0), places=1)
		self.assertAlmostEqual(5.999987, units.volume.millilitres.to_cubic_inches(98.3224), places=1)
		self.assertAlmostEqual(0.732285, units.volume.millilitres.to_cubic_inches(12.0), places=1)

	def test_convert_known_millilitres_to_oil_barrels(self):
		self.assertAlmostEqual(0.3, units.volume.millilitres.to_oil_barrels(47696.2), places=1)
		self.assertAlmostEqual(0.9, units.volume.millilitres.to_oil_barrels(143089.0), places=1)
		self.assertAlmostEqual(0.002, units.volume.millilitres.to_oil_barrels(317.97459), places=1)

if __name__ == '__main__':
    unittest.main()

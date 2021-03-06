# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.pressure.psi

class TestPsiMethods(unittest.TestCase):

	def test_convert_known_psi_to_bars(self):
		self.assertAlmostEqual(62.0528, units.pressure.psi.to_bars(900.0), places=1)
		self.assertAlmostEqual(9.23897, units.pressure.psi.to_bars(134.0), places=1)
		self.assertAlmostEqual(7.6669701, units.pressure.psi.to_bars(111.2), places=1)

	def test_convert_known_psi_to_pascals(self):
		self.assertAlmostEqual(6205.28, units.pressure.psi.to_pascals(0.9), places=1)
		self.assertAlmostEqual(206.8427, units.pressure.psi.to_pascals(0.03), places=1)
		self.assertAlmostEqual(13789.5, units.pressure.psi.to_pascals(2.0), places=1)

	def test_convert_known_psi_to_atmospheres(self):
		self.assertAlmostEqual(0.136092, units.pressure.psi.to_atmospheres(2.0), places=1)
		self.assertAlmostEqual(7.41701, units.pressure.psi.to_atmospheres(109.0), places=1)
		self.assertAlmostEqual(0.544368, units.pressure.psi.to_atmospheres(8.0), places=1)

	def test_convert_known_psi_to_torrs(self):
		self.assertAlmostEqual(310.29, units.pressure.psi.to_torrs(6.0), places=1)
		self.assertAlmostEqual(175.831, units.pressure.psi.to_torrs(3.4), places=1)
		self.assertAlmostEqual(25.8575, units.pressure.psi.to_torrs(0.5), places=1)

if __name__ == '__main__':
    unittest.main()

# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.pressure.bars

class TestBarsMethods(unittest.TestCase):

	def test_convert_known_bars_to_atmospheres(self):
		self.assertAlmostEqual(789.539, units.pressure.bars.to_atmospheres(800.0), places=1)
		self.assertAlmostEqual(121.392, units.pressure.bars.to_atmospheres(123.0), places=1)
		self.assertAlmostEqual(87.8362, units.pressure.bars.to_atmospheres(89.0), places=1)

	def test_convert_known_bars_to_pascals(self):
		self.assertAlmostEqual(89000.0, units.pressure.bars.to_pascals(0.89), places=1)
		self.assertAlmostEqual(1000.0, units.pressure.bars.to_pascals(0.01), places=1)
		self.assertAlmostEqual(12300.0, units.pressure.bars.to_pascals(0.123), places=1)

	def test_convert_known_bars_to_torrs(self):
		self.assertAlmostEqual(92.257587, units.pressure.bars.to_torrs(0.123), places=1)
		self.assertAlmostEqual(1500.12, units.pressure.bars.to_torrs(2.0), places=1)
		self.assertAlmostEqual(6675.55, units.pressure.bars.to_torrs(8.9), places=1)

	def test_convert_known_bars_to_psi(self):
		self.assertAlmostEqual(117.481, units.pressure.bars.to_psi(8.1), places=1)
		self.assertAlmostEqual(14518.29290, units.pressure.bars.to_psi(1001.0), places=1)
		self.assertAlmostEqual(87.0226, units.pressure.bars.to_psi(6.0), places=1)

if __name__ == '__main__':
    unittest.main()

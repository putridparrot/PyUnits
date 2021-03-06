# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.pressure.atmospheres

class TestAtmospheresMethods(unittest.TestCase):

	def test_convert_known_atmospheres_to_bars(self):
		self.assertAlmostEqual(6.0795, units.pressure.atmospheres.to_bars(6.0), places=1)
		self.assertAlmostEqual(1.2159, units.pressure.atmospheres.to_bars(1.2), places=1)
		self.assertAlmostEqual(0.8106, units.pressure.atmospheres.to_bars(0.8), places=1)

	def test_convert_known_atmospheres_to_pascals(self):
		self.assertAlmostEqual(81060.0, units.pressure.atmospheres.to_pascals(0.8), places=1)
		self.assertAlmostEqual(121590.0, units.pressure.atmospheres.to_pascals(1.2), places=1)
		self.assertAlmostEqual(45596.25, units.pressure.atmospheres.to_pascals(0.45), places=1)

	def test_convert_known_atmospheres_to_torrs(self):
		self.assertAlmostEqual(342.0, units.pressure.atmospheres.to_torrs(0.45), places=1)
		self.assertAlmostEqual(912.0, units.pressure.atmospheres.to_torrs(1.2), places=1)
		self.assertAlmostEqual(4560.0, units.pressure.atmospheres.to_torrs(6.0), places=1)

	def test_convert_known_atmospheres_to_psi(self):
		self.assertAlmostEqual(88.1757, units.pressure.atmospheres.to_psi(6.0), places=1)
		self.assertAlmostEqual(5.87838, units.pressure.atmospheres.to_psi(0.4), places=1)
		self.assertAlmostEqual(17.6351, units.pressure.atmospheres.to_psi(1.2), places=1)

if __name__ == '__main__':
    unittest.main()

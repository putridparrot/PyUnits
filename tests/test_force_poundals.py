# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.force.poundals

class TestPoundalsMethods(unittest.TestCase):

	def test_convert_known_poundals_to_newtons(self):
		self.assertAlmostEqual(110.604, units.force.poundals.to_newtons(800.0), places=1)
		self.assertAlmostEqual(1.13369, units.force.poundals.to_newtons(8.2), places=1)
		self.assertAlmostEqual(26.2684, units.force.poundals.to_newtons(190.0), places=1)

	def test_convert_known_poundals_to_dynes(self):
		self.assertAlmostEqual(138.255, units.force.poundals.to_dynes(0.01), places=1)
		self.assertAlmostEqual(27651.0, units.force.poundals.to_dynes(2.0), places=1)
		self.assertAlmostEqual(12442.94589384, units.force.poundals.to_dynes(0.9), places=1)

	def test_convert_known_poundals_to_kilogramforce(self):
		self.assertAlmostEqual(0.479335, units.force.poundals.to_kilogramforce(34.0), places=1)
		self.assertAlmostEqual(1.4253161, units.force.poundals.to_kilogramforce(101.1), places=1)
		self.assertAlmostEqual(0.133932, units.force.poundals.to_kilogramforce(9.5), places=1)

if __name__ == '__main__':
    unittest.main()

# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.force.kilogramforce

class TestKilogramforceMethods(unittest.TestCase):

	def test_convert_known_kilogramforce_to_newtons(self):
		self.assertAlmostEqual(156.906, units.force.kilogramforce.to_newtons(16.0), places=1)
		self.assertAlmostEqual(91.2018, units.force.kilogramforce.to_newtons(9.3), places=1)
		self.assertAlmostEqual(49.0332, units.force.kilogramforce.to_newtons(5.0), places=1)

	def test_convert_known_kilogramforce_to_dynes(self):
		self.assertAlmostEqual(98066.5, units.force.kilogramforce.to_dynes(0.1), places=1)
		self.assertAlmostEqual(8825.985, units.force.kilogramforce.to_dynes(0.009), places=1)
		self.assertAlmostEqual(1961330.0, units.force.kilogramforce.to_dynes(2.0), places=1)

	def test_convert_known_kilogramforce_to_poundals(self):
		self.assertAlmostEqual(141.863, units.force.kilogramforce.to_poundals(2.0), places=1)
		self.assertAlmostEqual(595.826, units.force.kilogramforce.to_poundals(8.4), places=1)
		self.assertAlmostEqual(63.8385, units.force.kilogramforce.to_poundals(0.9), places=1)

if __name__ == '__main__':
    unittest.main()

# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.magnetomotive_force.ampereturns

class TestAmpereturnsMethods(unittest.TestCase):

	def test_convert_known_ampereturns_to_gilberts(self):
		self.assertAlmostEqual(502.6548248, units.magnetomotive_force.ampereturns.to_gilberts(400.0), places=1)
		self.assertAlmostEqual(8.4194683154, units.magnetomotive_force.ampereturns.to_gilberts(6.7), places=1)
		self.assertAlmostEqual(1.0053096496, units.magnetomotive_force.ampereturns.to_gilberts(0.8), places=1)

if __name__ == '__main__':
    unittest.main()

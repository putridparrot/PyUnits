# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.frequency.kilohertz

class TestKilohertzMethods(unittest.TestCase):

	def test_convert_known_kilohertz_to_hertz(self):
		self.assertAlmostEqual(90909.09, units.frequency.kilohertz.to_hertz(90.90909), places=1)
		self.assertAlmostEqual(123.45, units.frequency.kilohertz.to_hertz(0.12345), places=1)
		self.assertAlmostEqual(500000.0, units.frequency.kilohertz.to_hertz(500.0), places=1)

	def test_convert_known_kilohertz_to_megahertz(self):
		self.assertAlmostEqual(0.909, units.frequency.kilohertz.to_megahertz(909.0), places=1)
		self.assertAlmostEqual(123.456, units.frequency.kilohertz.to_megahertz(123456.0), places=1)
		self.assertAlmostEqual(0.9, units.frequency.kilohertz.to_megahertz(900.0), places=1)

	def test_convert_known_kilohertz_to_gigahertz(self):
		self.assertAlmostEqual(0.987654, units.frequency.kilohertz.to_gigahertz(987654.0), places=1)
		self.assertAlmostEqual(0.01, units.frequency.kilohertz.to_gigahertz(10000.0), places=1)
		self.assertAlmostEqual(0.09009, units.frequency.kilohertz.to_gigahertz(90090.0), places=1)

if __name__ == '__main__':
    unittest.main()

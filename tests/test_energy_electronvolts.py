# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.energy.electronvolts

class TestElectronvoltsMethods(unittest.TestCase):

	def test_convert_known_electronvolts_to_kilojoules(self):
		self.assertAlmostEqual(1.9779957413e-14, units.energy.electronvolts.to_kilojoules(123456789.0), places=1)
		self.assertAlmostEqual(1.4434023094e-13, units.energy.electronvolts.to_kilojoules(900900900.0), places=1)
		self.assertAlmostEqual(1.977995743237493669e-5, units.energy.electronvolts.to_kilojoules(123456789123456789.0), places=1)

	def test_convert_known_electronvolts_to_kilocalories(self):
		self.assertAlmostEqual(1.6053857310684e-11, units.energy.electronvolts.to_kilocalories(100200300400.0), places=1)
		self.assertAlmostEqual(1.9779957413e-14, units.energy.electronvolts.to_kilocalories(123456789.0), places=1)
		self.assertAlmostEqual(1.4432417722369e-10, units.energy.electronvolts.to_kilocalories(900800700600.0), places=1)

	def test_convert_known_electronvolts_to_joules(self):
		self.assertAlmostEqual(1.9779957432302e-8, units.energy.electronvolts.to_joules(123456789123.0), places=1)
		self.assertAlmostEqual(1.4432417722369e-7, units.energy.electronvolts.to_joules(900800700600.0), places=1)
		self.assertAlmostEqual(1.601998367183e-7, units.energy.electronvolts.to_joules(999888777666.0), places=1)

	def test_convert_known_electronvolts_to_btu(self):
		self.assertAlmostEqual(15.188741377060267723, units.energy.electronvolts.to_btu(100020003000100020003000.0), places=1)
		self.assertAlmostEqual(151.84014791315084381, units.energy.electronvolts.to_btu(999888777666999888777666.0), places=1)
		self.assertAlmostEqual(1874.7782293466862029, units.energy.electronvolts.to_btu(12345678912341234567891234.0), places=1)

	def test_convert_known_electronvolts_to_calories(self):
		self.assertAlmostEqual(2.5515853167503e-8, units.energy.electronvolts.to_calories(666333111999.0), places=1)
		self.assertAlmostEqual(3.8288679904011702e-5, units.energy.electronvolts.to_calories(999888777666555.0), places=1)
		self.assertAlmostEqual(4.727523282641506e-7, units.energy.electronvolts.to_calories(12345678901234.0), places=1)

	def test_convert_known_electronvolts_to_u_s_therms(self):
		self.assertAlmostEqual(1.0118737258101e-10, units.energy.electronvolts.to_u_s_therms(666333111999.0), places=1)
		self.assertAlmostEqual(1.5184014791308327e-7, units.energy.electronvolts.to_u_s_therms(999888777666555.0), places=1)
		self.assertAlmostEqual(1.874778227659974e-9, units.energy.electronvolts.to_u_s_therms(12345678901234.0), places=1)

	def test_convert_known_electronvolts_to_watt_hours(self):
		self.assertAlmostEqual(4.490576030342e-12, units.energy.electronvolts.to_watt_hours(100900700100.0), places=1)
		self.assertAlmostEqual(4.00579748289276988e-7, units.energy.electronvolts.to_watt_hours(9000800070006000.0), places=1)
		self.assertAlmostEqual(5.494432653620188248e-7, units.energy.electronvolts.to_watt_hours(12345678987654321.0), places=1)

	def test_convert_known_electronvolts_to_kilowatt_hours(self):
		self.assertAlmostEqual(4.490576030342e-15, units.energy.electronvolts.to_kilowatt_hours(100900700100.0), places=1)
		self.assertAlmostEqual(4.4504410034909e-14, units.energy.electronvolts.to_kilowatt_hours(999988887777.0), places=1)
		self.assertAlmostEqual(5.494432653620187834e-10, units.energy.electronvolts.to_kilowatt_hours(12345678987654321.0), places=1)

	def test_convert_known_electronvolts_to_foot_pounds(self):
		self.assertAlmostEqual(1.1923484070355e-8, units.energy.electronvolts.to_foot_pounds(100900700100.0), places=1)
		self.assertAlmostEqual(1.1816916594359e-7, units.energy.electronvolts.to_foot_pounds(999988887777.0), places=1)
		self.assertAlmostEqual(0.0014588948005427860004, units.energy.electronvolts.to_foot_pounds(12345678987654321.0), places=1)

if __name__ == '__main__':
    unittest.main()

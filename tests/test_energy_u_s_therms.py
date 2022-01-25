# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.energy.u_s_therms

class TestUSThermsMethods(unittest.TestCase):

	def test_convert_known_u_s_therms_to_kilojoules(self):
		self.assertAlmostEqual(949.3236, units.energy.u_s_therms.to_kilojoules(0.009), places=1)
		self.assertAlmostEqual(316440.12, units.energy.u_s_therms.to_kilojoules(3.0), places=1)
		self.assertAlmostEqual(200412.075, units.energy.u_s_therms.to_kilojoules(1.9), places=1)

	def test_convert_known_u_s_therms_to_kilocalories(self):
		self.assertAlmostEqual(27731.484079398004, units.energy.u_s_therms.to_kilocalories(1.1), places=1)
		self.assertAlmostEqual(1008.417, units.energy.u_s_therms.to_kilocalories(0.04), places=1)
		self.assertAlmostEqual(310.088174, units.energy.u_s_therms.to_kilocalories(0.0123), places=1)

	def test_convert_known_u_s_therms_to_joules(self):
		self.assertAlmostEqual(843843.2, units.energy.u_s_therms.to_joules(0.008), places=1)
		self.assertAlmostEqual(358.633, units.energy.u_s_therms.to_joules(3.4e-6), places=1)
		self.assertAlmostEqual(715157.112, units.energy.u_s_therms.to_joules(0.00678), places=1)

	def test_convert_known_u_s_therms_to_btu(self):
		self.assertAlmostEqual(665.8409891, units.energy.u_s_therms.to_btu(0.00666), places=1)
		self.assertAlmostEqual(199952.249, units.energy.u_s_therms.to_btu(2.0), places=1)
		self.assertAlmostEqual(89978.51204, units.energy.u_s_therms.to_btu(0.9), places=1)

	def test_convert_known_u_s_therms_to_calories(self):
		self.assertAlmostEqual(75631.262, units.energy.u_s_therms.to_calories(0.003), places=1)
		self.assertAlmostEqual(171430.856, units.energy.u_s_therms.to_calories(6.8e-3), places=1)
		self.assertAlmostEqual(20168.3365, units.energy.u_s_therms.to_calories(0.0008), places=1)

	def test_convert_known_u_s_therms_to_watt_hours(self):
		self.assertAlmostEqual(175800.59, units.energy.u_s_therms.to_watt_hours(6.0), places=1)
		self.assertAlmostEqual(55670.189, units.energy.u_s_therms.to_watt_hours(1.9), places=1)
		self.assertAlmostEqual(2051.008, units.energy.u_s_therms.to_watt_hours(0.07), places=1)

	def test_convert_known_u_s_therms_to_kilowatt_hours(self):
		self.assertAlmostEqual(26.3701, units.energy.u_s_therms.to_kilowatt_hours(0.9), places=1)
		self.assertAlmostEqual(231.471, units.energy.u_s_therms.to_kilowatt_hours(7.9), places=1)
		self.assertAlmostEqual(41.0202, units.energy.u_s_therms.to_kilowatt_hours(1.4), places=1)

	def test_convert_known_u_s_therms_to_foot_pounds(self):
		self.assertAlmostEqual(700352.43389267, units.energy.u_s_therms.to_foot_pounds(0.009), places=1)
		self.assertAlmostEqual(1556338.74198, units.energy.u_s_therms.to_foot_pounds(0.02), places=1)
		self.assertAlmostEqual(23345.081129, units.energy.u_s_therms.to_foot_pounds(0.0003), places=1)

	def test_convert_known_u_s_therms_to_electronvolts(self):
		self.assertAlmostEqual(592520940098199000000.0, units.energy.u_s_therms.to_electronvolts(0.0000009), places=1)
		self.assertAlmostEqual(8.815394875460983E+17, units.energy.u_s_therms.to_electronvolts(0.000000001339), places=1)
		self.assertAlmostEqual(43846549567266728.0, units.energy.u_s_therms.to_electronvolts(0.0000000000666), places=1)

if __name__ == '__main__':
    unittest.main()

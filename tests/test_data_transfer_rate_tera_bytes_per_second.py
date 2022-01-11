# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.data_transfer_rate.tera_bytes_per_second

class TestTeraBytesPerSecondMethods(unittest.TestCase):

	def test_convert_known_tera_bytes_per_second_to_bits_per_second(self):
		self.assertAlmostEqual(640000000.0, units.data_transfer_rate.tera_bytes_per_second.to_bits_per_second(0.00008), places=1)
		self.assertAlmostEqual(9.6, units.data_transfer_rate.tera_bytes_per_second.to_bits_per_second(1.2e-12), places=1)
		self.assertAlmostEqual(7.2e+13, units.data_transfer_rate.tera_bytes_per_second.to_bits_per_second(9.0), places=1)

	def test_convert_known_tera_bytes_per_second_to_kilo_bits_per_second(self):
		self.assertAlmostEqual(72000000.0, units.data_transfer_rate.tera_bytes_per_second.to_kilo_bits_per_second(0.009), places=1)
		self.assertAlmostEqual(11200.0, units.data_transfer_rate.tera_bytes_per_second.to_kilo_bits_per_second(1.4e-6), places=1)
		self.assertAlmostEqual(488000.0, units.data_transfer_rate.tera_bytes_per_second.to_kilo_bits_per_second(6.1e-5), places=1)

	def test_convert_known_tera_bytes_per_second_to_mega_bits_per_second(self):
		self.assertAlmostEqual(40000.0, units.data_transfer_rate.tera_bytes_per_second.to_mega_bits_per_second(0.005), places=1)
		self.assertAlmostEqual(984.0, units.data_transfer_rate.tera_bytes_per_second.to_mega_bits_per_second(0.000123), places=1)
		self.assertAlmostEqual(480.0, units.data_transfer_rate.tera_bytes_per_second.to_mega_bits_per_second(0.00006), places=1)

	def test_convert_known_tera_bytes_per_second_to_giga_bits_per_second(self):
		self.assertAlmostEqual(64.0, units.data_transfer_rate.tera_bytes_per_second.to_giga_bits_per_second(0.008), places=1)
		self.assertAlmostEqual(0.0024, units.data_transfer_rate.tera_bytes_per_second.to_giga_bits_per_second(3e-7), places=1)
		self.assertAlmostEqual(1.84, units.data_transfer_rate.tera_bytes_per_second.to_giga_bits_per_second(0.00023), places=1)

	def test_convert_known_tera_bytes_per_second_to_tera_bits_per_second(self):
		self.assertAlmostEqual(40.0, units.data_transfer_rate.tera_bytes_per_second.to_tera_bits_per_second(5.0), places=1)
		self.assertAlmostEqual(9.84, units.data_transfer_rate.tera_bytes_per_second.to_tera_bits_per_second(1.23), places=1)
		self.assertAlmostEqual(6400.0, units.data_transfer_rate.tera_bytes_per_second.to_tera_bits_per_second(800.0), places=1)

	def test_convert_known_tera_bytes_per_second_to_kilo_bytes_per_second(self):
		self.assertAlmostEqual(900000.0, units.data_transfer_rate.tera_bytes_per_second.to_kilo_bytes_per_second(0.0009), places=1)
		self.assertAlmostEqual(314.0, units.data_transfer_rate.tera_bytes_per_second.to_kilo_bytes_per_second(3.14e-7), places=1)
		self.assertAlmostEqual(630000.0, units.data_transfer_rate.tera_bytes_per_second.to_kilo_bytes_per_second(0.00063), places=1)

	def test_convert_known_tera_bytes_per_second_to_mega_bytes_per_second(self):
		self.assertAlmostEqual(9000.0, units.data_transfer_rate.tera_bytes_per_second.to_mega_bytes_per_second(0.009), places=1)
		self.assertAlmostEqual(234000.0, units.data_transfer_rate.tera_bytes_per_second.to_mega_bytes_per_second(0.234), places=1)
		self.assertAlmostEqual(2e+6, units.data_transfer_rate.tera_bytes_per_second.to_mega_bytes_per_second(2.0), places=1)

	def test_convert_known_tera_bytes_per_second_to_giga_bytes_per_second(self):
		self.assertAlmostEqual(2700.0, units.data_transfer_rate.tera_bytes_per_second.to_giga_bytes_per_second(2.7), places=1)
		self.assertAlmostEqual(900.0, units.data_transfer_rate.tera_bytes_per_second.to_giga_bytes_per_second(0.9), places=1)
		self.assertAlmostEqual(12.3, units.data_transfer_rate.tera_bytes_per_second.to_giga_bytes_per_second(0.0123), places=1)

	def test_convert_known_tera_bytes_per_second_to_kibibits_per_second(self):
		self.assertAlmostEqual(7031250.0, units.data_transfer_rate.tera_bytes_per_second.to_kibibits_per_second(0.0009), places=1)
		self.assertAlmostEqual(96093.75, units.data_transfer_rate.tera_bytes_per_second.to_kibibits_per_second(1.23e-5), places=1)
		self.assertAlmostEqual(781250.0, units.data_transfer_rate.tera_bytes_per_second.to_kibibits_per_second(0.0001), places=1)

	def test_convert_known_tera_bytes_per_second_to_mebibits_per_second(self):
		self.assertAlmostEqual(76293.95, units.data_transfer_rate.tera_bytes_per_second.to_mebibits_per_second(0.01), places=1)
		self.assertAlmostEqual(61035.156, units.data_transfer_rate.tera_bytes_per_second.to_mebibits_per_second(0.008), places=1)
		self.assertAlmostEqual(15258789.0625, units.data_transfer_rate.tera_bytes_per_second.to_mebibits_per_second(2.0), places=1)

if __name__ == '__main__':
    unittest.main()
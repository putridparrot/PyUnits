# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.data_storage.gigabytes

class TestGigabytesMethods(unittest.TestCase):

	def test_convert_known_gigabytes_to_bits(self):
		self.assertAlmostEqual(32000000.0, units.data_storage.gigabytes.to_bits(0.004), places=1)
		self.assertAlmostEqual(96000000.0, units.data_storage.gigabytes.to_bits(0.012), places=1)
		self.assertAlmostEqual(24.0, units.data_storage.gigabytes.to_bits(3e-9), places=1)

	def test_convert_known_gigabytes_to_kilobits(self):
		self.assertAlmostEqual(72000.0, units.data_storage.gigabytes.to_kilobits(0.009), places=1)
		self.assertAlmostEqual(960.0, units.data_storage.gigabytes.to_kilobits(1.2e-4), places=1)
		self.assertAlmostEqual(62400.0, units.data_storage.gigabytes.to_kilobits(0.0078), places=1)

	def test_convert_known_gigabytes_to_megabits(self):
		self.assertAlmostEqual(62.4, units.data_storage.gigabytes.to_megabits(0.0078), places=1)
		self.assertAlmostEqual(80.0, units.data_storage.gigabytes.to_megabits(0.01), places=1)
		self.assertAlmostEqual(9.872, units.data_storage.gigabytes.to_megabits(0.001234), places=1)

	def test_convert_known_gigabytes_to_gigabits(self):
		self.assertAlmostEqual(40.0, units.data_storage.gigabytes.to_gigabits(5.0), places=1)
		self.assertAlmostEqual(9.6, units.data_storage.gigabytes.to_gigabits(1.2), places=1)
		self.assertAlmostEqual(0.08, units.data_storage.gigabytes.to_gigabits(0.01), places=1)

	def test_convert_known_gigabytes_to_terabits(self):
		self.assertAlmostEqual(0.56, units.data_storage.gigabytes.to_terabits(70.0), places=1)
		self.assertAlmostEqual(72.008, units.data_storage.gigabytes.to_terabits(9001.0), places=1)
		self.assertAlmostEqual(6144.9912, units.data_storage.gigabytes.to_terabits(768123.9), places=1)

	def test_convert_known_gigabytes_to_kilobytes(self):
		self.assertAlmostEqual(200000.0, units.data_storage.gigabytes.to_kilobytes(0.2), places=1)
		self.assertAlmostEqual(9000.0, units.data_storage.gigabytes.to_kilobytes(0.009), places=1)
		self.assertAlmostEqual(1230.0, units.data_storage.gigabytes.to_kilobytes(0.00123), places=1)

	def test_convert_known_gigabytes_to_megabytes(self):
		self.assertAlmostEqual(900.0, units.data_storage.gigabytes.to_megabytes(0.9), places=1)
		self.assertAlmostEqual(12000.0, units.data_storage.gigabytes.to_megabytes(12.0), places=1)
		self.assertAlmostEqual(35600.0, units.data_storage.gigabytes.to_megabytes(35.6), places=1)

	def test_convert_known_gigabytes_to_terabytes(self):
		self.assertAlmostEqual(0.0356, units.data_storage.gigabytes.to_terabytes(35.6), places=1)
		self.assertAlmostEqual(0.10023, units.data_storage.gigabytes.to_terabytes(100.23), places=1)
		self.assertAlmostEqual(900.1, units.data_storage.gigabytes.to_terabytes(900100.0), places=1)

	def test_convert_known_gigabytes_to_kibibits(self):
		self.assertAlmostEqual(390625.0, units.data_storage.gigabytes.to_kibibits(0.05), places=1)
		self.assertAlmostEqual(62500.0, units.data_storage.gigabytes.to_kibibits(0.008), places=1)
		self.assertAlmostEqual(9609.375, units.data_storage.gigabytes.to_kibibits(0.00123), places=1)

	def test_convert_known_gigabytes_to_mebibits(self):
		self.assertAlmostEqual(68.66451, units.data_storage.gigabytes.to_mebibits(0.009), places=1)
		self.assertAlmostEqual(9155.268, units.data_storage.gigabytes.to_mebibits(1.2), places=1)
		self.assertAlmostEqual(146484.288, units.data_storage.gigabytes.to_mebibits(19.2), places=1)

if __name__ == '__main__':
    unittest.main()
# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.data_storage.gigabits

class TestGigabitsMethods(unittest.TestCase):

	def test_convert_known_gigabits_to_bits(self):
		self.assertAlmostEqual(900000.0, units.data_storage.gigabits.to_bits(0.0009), places=1)
		self.assertAlmostEqual(70000.0, units.data_storage.gigabits.to_bits(0.00007), places=1)
		self.assertAlmostEqual(12000.0, units.data_storage.gigabits.to_bits(1.2e-5), places=1)

	def test_convert_known_gigabits_to_kilobits(self):
		self.assertAlmostEqual(10000.0, units.data_storage.gigabits.to_kilobits(0.01), places=1)
		self.assertAlmostEqual(910000.0, units.data_storage.gigabits.to_kilobits(0.91), places=1)
		self.assertAlmostEqual(6.1e+6, units.data_storage.gigabits.to_kilobits(6.1), places=1)

	def test_convert_known_gigabits_to_megabits(self):
		self.assertAlmostEqual(6100.0, units.data_storage.gigabits.to_megabits(6.1), places=1)
		self.assertAlmostEqual(961.0, units.data_storage.gigabits.to_megabits(0.961), places=1)
		self.assertAlmostEqual(1.2, units.data_storage.gigabits.to_megabits(1.2e-3), places=1)

	def test_convert_known_gigabits_to_terabits(self):
		self.assertAlmostEqual(1.2, units.data_storage.gigabits.to_terabits(1200.0), places=1)
		self.assertAlmostEqual(90.012, units.data_storage.gigabits.to_terabits(90012.0), places=1)
		self.assertAlmostEqual(8.0, units.data_storage.gigabits.to_terabits(8000.0), places=1)

	def test_convert_known_gigabits_to_kilobytes(self):
		self.assertAlmostEqual(150000.0, units.data_storage.gigabits.to_kilobytes(1.2), places=1)
		self.assertAlmostEqual(112500.0, units.data_storage.gigabits.to_kilobytes(0.9), places=1)
		self.assertAlmostEqual(125.0, units.data_storage.gigabits.to_kilobytes(0.001), places=1)

	def test_convert_known_gigabits_to_megabytes(self):
		self.assertAlmostEqual(112.5, units.data_storage.gigabits.to_megabytes(0.9), places=1)
		self.assertAlmostEqual(150.0, units.data_storage.gigabits.to_megabytes(1.2), places=1)
		self.assertAlmostEqual(10012.5, units.data_storage.gigabits.to_megabytes(80.1), places=1)

	def test_convert_known_gigabits_to_gigabytes(self):
		self.assertAlmostEqual(12.375, units.data_storage.gigabits.to_gigabytes(99.0), places=1)
		self.assertAlmostEqual(15.390375, units.data_storage.gigabits.to_gigabytes(123.123), places=1)
		self.assertAlmostEqual(1000.1125, units.data_storage.gigabits.to_gigabytes(8000.9), places=1)

	def test_convert_known_gigabits_to_terabytes(self):
		self.assertAlmostEqual(1.125, units.data_storage.gigabits.to_terabytes(9000.0), places=1)
		self.assertAlmostEqual(154.320875, units.data_storage.gigabits.to_terabytes(1234567.0), places=1)
		self.assertAlmostEqual(0.076625, units.data_storage.gigabits.to_terabytes(613.0), places=1)

	def test_convert_known_gigabits_to_kibibits(self):
		self.assertAlmostEqual(781250.0, units.data_storage.gigabits.to_kibibits(0.8), places=1)
		self.assertAlmostEqual(11718.75, units.data_storage.gigabits.to_kibibits(0.012), places=1)
		self.assertAlmostEqual(1953.125, units.data_storage.gigabits.to_kibibits(0.002), places=1)

	def test_convert_known_gigabits_to_mebibits(self):
		self.assertAlmostEqual(1.9073486, units.data_storage.gigabits.to_mebibits(0.002), places=1)
		self.assertAlmostEqual(858.30688476562, units.data_storage.gigabits.to_mebibits(0.9), places=1)
		self.assertAlmostEqual(5817.413330078125, units.data_storage.gigabits.to_mebibits(6.1), places=1)

if __name__ == '__main__':
    unittest.main()

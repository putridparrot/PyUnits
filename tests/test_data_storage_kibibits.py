# <auto-generated>
# This code was generated by the UnitCodeGenerator tool
#
# Changes to this file will be lost if the code is regenerated
# </auto-generated>

import unittest
import units.data_storage.kibibits

class TestKibibitsMethods(unittest.TestCase):

	def test_convert_known_kibibits_to_bits(self):
		self.assertAlmostEqual(2048.0, units.data_storage.kibibits.to_bits(2.0), places=1)
		self.assertAlmostEqual(9216.0, units.data_storage.kibibits.to_bits(9.0), places=1)
		self.assertAlmostEqual(18227.2, units.data_storage.kibibits.to_bits(17.8), places=1)

	def test_convert_known_kibibits_to_kilobits(self):
		self.assertAlmostEqual(6.3488, units.data_storage.kibibits.to_kilobits(6.2), places=1)
		self.assertAlmostEqual(0.9216, units.data_storage.kibibits.to_kilobits(0.9), places=1)
		self.assertAlmostEqual(89.088, units.data_storage.kibibits.to_kilobits(87.0), places=1)

	def test_convert_known_kibibits_to_megabits(self):
		self.assertAlmostEqual(0.089088, units.data_storage.kibibits.to_megabits(87.0), places=1)
		self.assertAlmostEqual(0.01263616, units.data_storage.kibibits.to_megabits(12.34), places=1)
		self.assertAlmostEqual(126.418879, units.data_storage.kibibits.to_megabits(123456.0), places=1)

	def test_convert_known_kibibits_to_gigabits(self):
		self.assertAlmostEqual(0.126418944, units.data_storage.kibibits.to_gigabits(123456.0), places=1)
		self.assertAlmostEqual(8.192, units.data_storage.kibibits.to_gigabits(8000000.0), places=1)
		self.assertAlmostEqual(1.307521024, units.data_storage.kibibits.to_gigabits(1276876.0), places=1)

	def test_convert_known_kibibits_to_terabits(self):
		self.assertAlmostEqual(0.8192, units.data_storage.kibibits.to_terabits(800000000.0), places=1)
		self.assertAlmostEqual(1536.0, units.data_storage.kibibits.to_terabits(1.5e12), places=1)
		self.assertAlmostEqual(0.01023999898, units.data_storage.kibibits.to_terabits(9999999.0), places=1)

	def test_convert_known_kibibits_to_kilobytes(self):
		self.assertAlmostEqual(117.632, units.data_storage.kibibits.to_kilobytes(919.0), places=1)
		self.assertAlmostEqual(9.9072, units.data_storage.kibibits.to_kilobytes(77.4), places=1)
		self.assertAlmostEqual(13.965952, units.data_storage.kibibits.to_kilobytes(109.109), places=1)

	def test_convert_known_kibibits_to_megabytes(self):
		self.assertAlmostEqual(0.128, units.data_storage.kibibits.to_megabytes(1000.0), places=1)
		self.assertAlmostEqual(0.102415744, units.data_storage.kibibits.to_megabytes(800.123), places=1)
		self.assertAlmostEqual(15.802368, units.data_storage.kibibits.to_megabytes(123456.0), places=1)

	def test_convert_known_kibibits_to_gigabytes(self):
		self.assertAlmostEqual(1.580347926, units.data_storage.kibibits.to_gigabytes(12345678.0), places=1)
		self.assertAlmostEqual(1024000.00, units.data_storage.kibibits.to_gigabytes(8e12), places=1)
		self.assertAlmostEqual(0.01536, units.data_storage.kibibits.to_gigabytes(1.2e5), places=1)

	def test_convert_known_kibibits_to_terabytes(self):
		self.assertAlmostEqual(0.01536, units.data_storage.kibibits.to_terabytes(120000000.0), places=1)
		self.assertAlmostEqual(11264.0, units.data_storage.kibibits.to_terabytes(88e12), places=1)
		self.assertAlmostEqual(0.009216, units.data_storage.kibibits.to_terabytes(9000000.0), places=1)

	def test_convert_known_kibibits_to_mebibits(self):
		self.assertAlmostEqual(0.5859375, units.data_storage.kibibits.to_mebibits(600.0), places=1)
		self.assertAlmostEqual(12.055664, units.data_storage.kibibits.to_mebibits(12345.0), places=1)
		self.assertAlmostEqual(0.0986328, units.data_storage.kibibits.to_mebibits(101.0), places=1)

if __name__ == '__main__':
    unittest.main()
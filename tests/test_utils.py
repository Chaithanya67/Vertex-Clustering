import unittest
from core.utils import shingle_cover

class UtilsTest(unittest.TestCase):

	def test_empty_shingle(self):
		self.assertTrue(shingle_cover([], []))

	def test_generic_shingles(self):
		self.assertTrue(
			shingle_cover(
				[20, 50, 88, 244], 
				[20, 50, 88, 244]
			)
		)

	def test_different_shingles(self):
		self.assertFalse(
			shingle_cover(
				[1, 50, 88, 244], 
				[20, 50, 88, 244]
			)
		)

	def test_masked_shingles(self):
		self.assertTrue(
			shingle_cover(
				[77, None, 5, 10],
				[None, 2, 5, 10]
			)
		)

	def test_wrong_masked_shingle(self):
		self.assertFalse(
			shingle_cover(
				[15, 99, 255, 0],
				[None, 222, 255, 0]
			)
		)
import unittest
from core.ShingleVectorFactory import create_shingle_vector
from core.ShingleVectorFactory import create_masked_shingles

class ShingleVectorFactoryTest(unittest.TestCase):

	def setUp(self):
		self.shingle_vector = create_shingle_vector([
							["html", "head"], 
							["head", "head"],
							["head", "body"],
							["body", "body"],
							["body", "html"]
		])

	def test_create_generic_shingle(self):
		self.assertEqual(len(self.shingle_vector), 8)

	def test_shingle_all_positives(self):
		lowest_hash = min(self.shingle_vector)
		self.assertTrue(lowest_hash >= 0)

	def test_fits_one_byte(self):
		highest_hash = max(self.shingle_vector)
		self.assertTrue(highest_hash <= 255)

class ShingleMaskedVectorFactoryTest(unittest.TestCase):

	def setUp(self):
		self.shingle_source = [1,2,3,4,5,6,7,8]

	# mask 8/8
	def test_mask_full_8_8(self):
		masked = create_masked_shingles(self.shingle_source, mask=0)
		self.assertEqual(len(masked), 1)

	# mask 7/8
	def test_mask_partial_7_8(self):
		masked = create_masked_shingles(self.shingle_source, mask=1)
		self.assertEqual(len(masked), 8)

	# mask 6/8
	def test_mask_partial_6_8(self):
		masked = create_masked_shingles(self.shingle_source, mask=2)
		self.assertEqual(len(masked), 28)
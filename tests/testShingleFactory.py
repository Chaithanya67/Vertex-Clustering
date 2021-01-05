import unittest
from core.ShingleVectorFactory import create_shingle_vector

class ShingleExtractorTest(unittest.TestCase):

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
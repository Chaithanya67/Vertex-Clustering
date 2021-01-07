import unittest
from core.ShingleVectorFactory import create_shingle_vector
from core.webpage import Webpage
from core.ShingleExtractor import extract_shingle_set

class ShingleExtractorTest(unittest.TestCase):

    def setUp(self):
        
        self.basic_page = Webpage("boh","<html><head></head><body>hello world</body></html>")
        self.shingle_set = extract_shingle_set(self.basic_page, 2)
        self.shingle_vector = create_shingle_vector(self.shingle_set)

    def test_create_generic_shingle(self):
        self.assertEqual(len(self.shingle_vector.getContent()), 8)

    def test_shingle_all_positives(self):
        lowest_hash = min(self.shingle_vector.getContent())
        self.assertTrue(lowest_hash >= 0)

    def test_fits_one_byte(self):
        highest_hash = max(self.shingle_vector.getContent())
        self.assertTrue(highest_hash <= 255)

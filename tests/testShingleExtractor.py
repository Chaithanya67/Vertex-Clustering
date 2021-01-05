import unittest
from core.ShingleExtractor import extract_shingle_set

class ShingleExtractorTest(unittest.TestCase):
	
	def test_basic_webpage(self):
		basic_page = "<html><head></head><body>hello world</body></html>"
		expected_shingle = [
			["html", "head"], 
			["head", "head"],
			["head", "body"],
			["body", "body"],
			["body", "html"]
		]
		shingle = extract_shingle_set(basic_page, 2)
		self.assertEqual(shingle, expected_shingle)

	def test_void_webpage(self):
		void_page = ""
		shingle = extract_shingle_set(void_page, 5)
		self.assertEqual(len(shingle), 0)


	def test_window_bigger_than_page(self):
		page = "<html><body></body></html>"
		shingle = extract_shingle_set(page, 5)
		self.assertEqual(len(shingle), 0)

	def test_window_equal_than_page(self):
		page = "<html><body></body></html>"
		shingle = extract_shingle_set(page, 4)
		self.assertEqual(len(shingle), 1)


if __name__ == "__main__":
	unittest.main()
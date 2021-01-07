import unittest
from core.ShingleExtractor import extract_shingle_set
from core.webpage import Webpage
from core.shingle import Shingle

class ShingleExtractorTest(unittest.TestCase):

    def test_basic_webpage(self):
        basic_page = Webpage("boh","<html><head></head><body>hello world</body></html>")
        expected_shingle = Shingle("boh",[
            ["html", "head"], 
            ["head", "head"],
            ["head", "body"],
            ["body", "body"],
            ["body", "html"]
        ])
        shingle = extract_shingle_set(basic_page, 2)
        self.assertEqual(shingle[0].getContent(), ["html", "head"])
        self.assertEqual(shingle[1].getContent(), ["head", "head"])
        self.assertEqual(shingle[2].getContent(), ["head", "body"])
        self.assertEqual(shingle[3].getContent(), ["body", "body"])
        self.assertEqual(shingle[4].getContent(), ["body", "html"])

    def test_void_webpage(self):
        void_page = Webpage("","")
        shingle = extract_shingle_set(void_page, 5)
        self.assertEqual(len(shingle), 0)


    def test_window_bigger_than_page(self):
        page = Webpage("boh","<html><body></body></html>")
        shingle = extract_shingle_set(page, 5)
        self.assertEqual(len(shingle), 0)

    def test_window_equal_than_page(self):
        page = Webpage("boh","<html><body></body></html>")
        shingle = extract_shingle_set(page, 4)
        self.assertEqual(len(shingle), 1)

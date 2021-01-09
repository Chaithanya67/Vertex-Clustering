import unittest
from core.utils import shingle_cover
from core.shingleVector import ShingleVector
from core.utils import k_shingle_cover
from core.utils import find_8_masked_shingle_vectors_sorted
from core.utils import maximum_count_covering


class UtilsTest(unittest.TestCase):

    def setUp(self):
        self.shingle_vector = ShingleVector("boh", [1, 2, 3])
        self.shingle_vector_content = self.shingle_vector.getContent()

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


    def test_find_8_masked_shingle_vectors(self):
        hashtable = {}
        hashtable[(None,1,2)] = 1
        hashtable[(1,2,3)] = 1
        hashtable[(2,None,None)] = 1
        self.assertTrue(1 == len(find_8_masked_shingle_vectors_sorted(hashtable)))
        self.assertTrue((1,2,3) == find_8_masked_shingle_vectors_sorted(hashtable)[0])
        hashtable[(2,2,2)] = 1
        self.assertTrue(2 == len(find_8_masked_shingle_vectors_sorted(hashtable)))
        
    def test_find_8_masked_shingle_vectors_sorted(self):
        hashtable = {}
        hashtable[(1,1,1)] = 3 ##Terzo
        hashtable[(2,2,2)] = 1 ##Primo
        hashtable[(3,3,3)] = 2 ##Secondo
        self.assertTrue((2,2,2) == find_8_masked_shingle_vectors_sorted(hashtable)[0])
        self.assertTrue((1,1,1) == find_8_masked_shingle_vectors_sorted(hashtable)[2])
        
    def test_maximum_count_covering(self):
        hashtable = {}
        hashtable[(1,1,2)] = 2
        hashtable[(1,1,3)] = 1 ##Unico coperto da (1,None,3)
        hashtable[(1,1,1)] = 3 ##Massimo coperto da (1,1,None)
        self.assertEqual((1,1,1), maximum_count_covering(hashtable, (1,1,None)))
        self.assertEqual((1,1,3), maximum_count_covering(hashtable, (1,None,3)))
        hashtable[(2,1,3)] = 2 ##Massimo coperto da (None,1,3)
        hashtable[(3,1,3)] = 1                
        self.assertEqual((2,1,3), maximum_count_covering(hashtable, (None,1,3))) 
        hashtable[(3,3,3)] = 2 ##A parità di conteggio devi prendere il primo che incontri
        hashtable[(2,3,3)] = 2
        hashtable[(1,3,3)] = 2
        self.assertEqual((3,3,3), maximum_count_covering(hashtable, (None,3,3)))
        
    def test_6_shingle_cover(self):
        self.assertEqual([ShingleVector('boh', (None, None, 3)),
                          ShingleVector('boh', (None, 2, None)),
                          ShingleVector('boh', (1, None, None)),
                          ShingleVector('boh', (None, 2, 3)),
                          ShingleVector('boh', (1, None, 3)),
                          ShingleVector('boh', (1, 2, None)),
                          ShingleVector('boh', (1, 2, 3))],
                         k_shingle_cover(self.shingle_vector, 6))

    def test_7_shingle_cover(self):
        self.assertEqual([ShingleVector('boh', (None, 2, 3)),
                          ShingleVector('boh', (1, None, 3)),
                          ShingleVector('boh', (1, 2, None)),
                          ShingleVector('boh', (1, 2, 3))],
                         k_shingle_cover(self.shingle_vector, 7))

    def test_8_shingle_cover(self):
        self.assertEqual([ShingleVector('boh', (1, 2, 3))], k_shingle_cover(self.shingle_vector, 8))

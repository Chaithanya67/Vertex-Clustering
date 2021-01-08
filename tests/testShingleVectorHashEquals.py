import unittest
from core.shingleVector import ShingleVector
from core.webpage import Webpage


class MyTestCase(unittest.TestCase):
    def test_not_equal_shingle_vectors(self):
        # shingle vectors presi dal paper Vertex
        v1 = ShingleVector(None, [0, 0, 0, 0, 0, 1, 2, 4])
        v2 = ShingleVector(None, [0, 0, 0, 0, 0, 6, 2, 3])
        v3 = ShingleVector(None, [0, 0, 0, 0, 0, 1, 5, 3])
        self.assertNotEqual(v1, v2)
        self.assertNotEqual(v1, v3)
        self.assertNotEqual(v2, v3)

    def test_not_equal_masked_vectors(self):
        # masked vectors presi da esempio in Vertex
        mv1 = ShingleVector(None, [0, 0, 0, 0, 0, 1, None, None])
        mv2 = ShingleVector(None, [0, 0, 0, 0, 0, None, 2, None])
        mv3 = ShingleVector(None, [0, 0, 0, 0, 0, None, None, 3])
        self.assertNotEqual(mv1, mv2)
        self.assertNotEqual(mv1, mv3)
        self.assertNotEqual(mv2, mv3)

    def test_equal_shingle_vectors(self):
        webpage1 = Webpage('cluster1', '<html></html>')
        webpage2 = Webpage('cluster2', '<html><head></head></html>')
        v4 = ShingleVector(webpage1, [0, 0, 0, 0, 0, 1, 2, 4])
        v5 = ShingleVector(webpage2, [0, 0, 0, 0, 0, 1, 2, 4])
        # TODO decidere se va bene che siano uguali (in teoria si)
        self.assertEqual(v4, v5)

    def test_equal_masked_shingle_vectors(self):
        mv4 = ShingleVector(None, [0, 0, 0, 0, 0, 1, None, 4])
        mv5 = ShingleVector(None, [0, 0, 0, 0, 0, 1, None, 4])
        self.assertEqual(mv4, mv5)

    def test_equal_hash_vectors(self):
        v6 = ShingleVector(None, [0, 0, 5, 0, 0, 1, 2, 3])
        v7 = ShingleVector(None, [0, 0, 5, 0, 0, 1, 2, 3])
        self.assertEqual(hash(v6), hash(v7))

    def test_equal_hash_masked_vectors(self):
        mv4 = ShingleVector(None, [0, 0, 0, 0, 0, 1, None, 4])
        mv5 = ShingleVector(None, [0, 0, 0, 0, 0, 1, None, 4])
        self.assertEqual(hash(mv4), hash(mv5))

    def test_not_equal_hash_vectors(self):
        v1 = ShingleVector(None, [0, 0, 0, 0, 0, 1, 2, 4])
        v2 = ShingleVector(None, [0, 0, 0, 0, 0, 6, 2, 3])
        self.assertNotEqual(hash(v1), hash(v2))

    def test_not_equal_hash_masked_vectors(self):
        mv1 = ShingleVector(None, [0, 0, 0, 0, 0, 1, None, None])
        mv2 = ShingleVector(None, [0, 0, 0, 0, 0, None, 2, None])
        self.assertNotEqual(hash(mv1), hash(mv2))

    def test_dictionary_operations(self):
        v1 = ShingleVector(None, [0, 0, 0, 0, 0, 1, 2, 4])
        v2 = ShingleVector(None, [0, 0, 0, 0, 0, 6, 2, 3])
        # v3 = v1
        v3 = ShingleVector(None, [0, 0, 0, 0, 0, 1, 2, 4])
        mv1 = ShingleVector(None, [0, 0, 0, 0, 0, 1, None, None])
        mv2 = ShingleVector(None, [0, 0, 0, 0, 0, None, 2, None])
        dictionary = {
            v1: (v1, 1),
            v2: (v2, 1),
            mv1: (mv1, 1),
            mv2: (mv2, 1),
            # sovrascrive v1
            v3: (v3, 2)
        }
        self.assertEqual(len(dictionary), 4)
        self.assertEqual(dictionary.get(v2)[0], v2)
        self.assertNotEqual(dictionary.get(mv1)[0], v1)
        # il dizionario è stato aggiornato inserendo v3 che ha sovrascritto v1
        self.assertEqual(dictionary.get(v3)[1], 2)
        # usando la chiave di v1 (uguale a quella di v3) si ottiene il valore inserito con v3
        self.assertEqual(dictionary.get(v1)[0], v3)
        self.assertEqual(dictionary.get(v3)[0], v3)


if __name__ == '__main__':
    unittest.main()

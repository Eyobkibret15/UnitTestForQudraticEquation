import unittest
import main

class TestMain(unittest.TestCase):
    def test_two_root(self):
        result = main.for_two_root(2,9,1)
        self.assertTrue(result)

    def test_one_root(self):
        result = main.for_one_root(4, 4, 1)
        self.assertTrue(result)

    def test_no_real_root(self):
        result = main.for_no_root(2, 1, 6)
        self.assertTrue(result)

unittest.main()
import unittest
import main


class TestMain(unittest.TestCase):
    def test_two_root(self):
        result = main.for_two_root(2, 9, 1)
        self.assertEqual(result,True)

    def test_one_root(self):
        result = main.for_one_root(4, 4, 1)
        self.assertEqual(result,True)

    def test_no_real_root(self):
        result = main.for_no_root(2, 1, 6)
        self.assertEqual(result,True)


if __name__ == '__test_module__':
    unittest.main()

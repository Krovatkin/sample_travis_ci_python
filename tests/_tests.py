import adder.add
import unittest

class AdderTestCase(unittest.TestCase):


    def test_add_one(self):
        self.assertEqual(adder.add.add_one(0), 1)
        self.assertEqual(adder.add.add_one(1), 2)

if __name__ == '__main__':
    unittest.main()
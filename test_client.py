import unittest
from client import getDataPoint, getRatio

class TestClientMethods(unittest.TestCase):

    def test_getDataPoint(self):
        quote = {'stock': 'ABC', 'top_bid': {'price': '100'}, 'top_ask': {'price': '110'}}
        self.assertEqual(getDataPoint(quote), ('ABC', 100.0, 110.0, 105.0))

    def test_getRatio(self):
        self.assertEqual(getRatio(100, 50), 2.0)
        self.assertIsNone(getRatio(100, 0))  # Handling division by zero

if __name__ == '__main__':
    unittest.main()

import unittest
from client import getDataPoint, getRatio

class TestClientMethods(unittest.TestCase):
    
    def test_getDataPoint(self):
        # Test cases for getDataPoint
        quotes = [
            {'stock': 'AAPL', 'top_bid': {'price': '100'}, 'top_ask': {'price': '110'}},
            {'stock': 'GOOG', 'top_bid': {'price': '300'}, 'top_ask': {'price': '310'}}
        ]

        # Expected results are tuples of (stock, bid_price, ask_price, calculated price)
        expected_results = [
            ('AAPL', 100.0, 110.0, 105.0),
            ('GOOG', 300.0, 310.0, 305.0)
        ]

        # Iterate through each quote and check the result against the expected result
        for quote, expected in zip(quotes, expected_results):
            result = getDataPoint(quote)
            self.assertEqual(result, expected)

    def test_getRatio(self):
        # Testing getRatio under different conditions
        self.assertEqual(getRatio(200, 100), 2.0)  # Normal condition
        self.assertEqual(getRatio(100, 200), 0.5)  # Ratio less than 1
        self.assertIsNone(getRatio(100, 0))        # Division by zero

        # Additional test cases can be included here
        # Example: Ratio with price A zero
        self.assertEqual(getRatio(0, 100), 0)

    def test_getRatio_edgeCases(self):
        # Edge cases for getRatio
        self.assertIsNone(getRatio(0, 0))  # Both prices zero
        self.assertIsNone(getRatio(100, 0))  # Price B zero
        self.assertEqual(getRatio(0, 100), 0)  # Price A zero

if __name__ == '__main__':
    unittest.main()

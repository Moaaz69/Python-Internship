import unittest
from api_fetcher import extract_prices

class TestApiFetcher(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "rates": {
                "USD": 1.0,
                "EUR": 0.9,
                "JPY": 110.0
            }
        }

    def test_extract_prices_all(self):
        result = extract_prices(self.sample_data)
        self.assertEqual(result, {"USD": 1.0, "EUR": 0.9, "JPY": 110.0})

    def test_extract_prices_keyword(self):
        result = extract_prices(self.sample_data, keyword="EU")
        self.assertEqual(result, {"EUR": 0.9})

    def test_extract_prices_no_match(self):
        result = extract_prices(self.sample_data, keyword="GBP")
        self.assertEqual(result, {})

if __name__ == "__main__":
    unittest.main()
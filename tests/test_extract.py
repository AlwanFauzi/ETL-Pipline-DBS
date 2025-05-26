import unittest
from utils.extract import extract_data

class TestExtract(unittest.TestCase):

    def test_extract_data_returns_list(self):
        data = extract_data()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_extract_data_fields(self):
        data = extract_data()
        sample = data[0]
        expected_keys = {'title', 'price', 'rating', 'colors', 'size', 'gender'}
        self.assertTrue(expected_keys.issubset(sample.keys()))

if __name__ == '__main__':
    unittest.main()

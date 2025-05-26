import unittest
from utils.transform import transform_data

class TestTransform(unittest.TestCase):

    def setUp(self):
        self.raw_data = [{
            'title': 'Test Item',
            'price': '$10.5',
            'rating': 'Rating: 4.3',
            'colors': '3 colors',
            'size': 'M',
            'gender': 'Male'
        }]

    def test_transform_returns_dataframe(self):
        df = transform_data(self.raw_data)
        self.assertEqual(df.shape[0], 1)
        self.assertIn('price', df.columns)
        self.assertAlmostEqual(df['price'].iloc[0], 168000.0, places=2)

    def test_transformed_rating(self):
        df = transform_data(self.raw_data)
        self.assertAlmostEqual(df['rating'].iloc[0], 4.3, places=1)

    def test_missing_price_dropped(self):
        bad_data = [dict(self.raw_data[0], price=None)]
        df = transform_data(bad_data)
        self.assertEqual(len(df), 0)

if __name__ == '__main__':
    unittest.main()

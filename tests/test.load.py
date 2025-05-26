import unittest
import os
import pandas as pd
from utils.load import save_to_csv

class TestLoad(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame([{
            'title': 'Item 1',
            'price': 10000,
            'rating': 4.5,
            'colors': 2,
            'size': 'L',
            'gender': 'Female'
        }])
        self.test_file = 'test_output.csv'

    def test_csv_saved(self):
        save_to_csv(self.df, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

        df_loaded = pd.read_csv(self.test_file)
        self.assertEqual(df_loaded.shape[0], 1)
        self.assertIn('price', df_loaded.columns)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()

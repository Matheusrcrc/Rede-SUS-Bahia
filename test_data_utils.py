
import unittest
import pandas as pd
from data_utils import load_and_process_data, calculate_metrics

class TestDataUtils(unittest.TestCase):
    def setUp(self):
        self.df = load_and_process_data()
    
    def test_data_loading(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertTrue(len(self.df) > 0)
    
    def test_metrics_calculation(self):
        metrics = calculate_metrics(self.df, year=2023)
        self.assertIsInstance(metrics, dict)
        self.assertTrue(all(key in metrics for key in [
            'total_usb', 'total_usa', 'total_upa', 'total_pa',
            'media_cobertura_samu', 'media_cobertura_ab'
        ]))

if __name__ == '__main__':
    unittest.main()

import unittest
from datetime import datetime
from utils.bazi_calculator import BaziCalculator

class TestBaziCalculator(unittest.TestCase):
    def test_validate_input_date_valid(self):
        self.assertTrue(BaziCalculator.validate_input_date(1990, 1, 1, 12, 0))
        
    def test_validate_input_date_invalid(self):
        self.assertFalse(BaziCalculator.validate_input_date(2023, 2, 30, 12, 0))
        
    def test_create_date_objects(self):
        solar, lunar = BaziCalculator.create_date_objects(1990, 1, 1, 12, 0)
        self.assertEqual(solar.toYmdHms(), "1990-01-01 12:00:00")
        lunar_str = BaziCalculator.get_formatted_lunar_date(lunar)
        self.assertEqual(lunar_str, "己巳年腊月初五")
        
    def test_calculate_age(self):
        self.assertEqual(BaziCalculator.calculate_age(2023, 1990), 34)
        
    def test_get_bazi_and_luck_info(self):
        bazi, yun_list = BaziCalculator.get_bazi_and_luck_info(
            1990, 1, 1, 12, 0, '男'
        )
        self.assertEqual(len(bazi), 4)
        self.assertGreater(len(yun_list), 0)
        self.assertIn('yun', yun_list[0])
        self.assertIn('liunian', yun_list[0])

if __name__ == '__main__':
    unittest.main()

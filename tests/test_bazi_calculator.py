import unittest
from datetime import datetime
from utils.bazi_calculator import BaziCalculator
from lunar_python import Lunar, Solar

class TestBaziCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = BaziCalculator()
        self.test_date = (1990, 5, 15, 12, 30)  # 阳历日期
        self.gender = '男'
    
    def test_validate_input_date(self):
        # 测试有效日期
        self.assertTrue(BaziCalculator.validate_input_date(*self.test_date))
        
        # 测试无效日期
        invalid_dates = [
            (1990, 2, 30, 12, 30),  # 无效的2月日期
            (1990, 13, 15, 12, 30), # 无效的月份
            (1990, 5, 15, 25, 30)   # 无效的小时
        ]
        for date in invalid_dates:
            self.assertFalse(BaziCalculator.validate_input_date(*date))
    
    def test_create_date_objects(self):
        solar, lunar = BaziCalculator.create_date_objects(*self.test_date)
        self.assertIsInstance(solar, Solar)
        self.assertIsInstance(lunar, Lunar)
        
        # 验证转换结果
        self.assertEqual(solar.getYear(), 1990)
        self.assertEqual(solar.getMonth(), 5)
        self.assertEqual(solar.getDay(), 15)
    
    def test_get_formatted_lunar_date(self):
        _, lunar = BaziCalculator.create_date_objects(*self.test_date)
        formatted_date = BaziCalculator.get_formatted_lunar_date(lunar)
        self.assertIsInstance(formatted_date, str)
        self.assertIn('年', formatted_date)
        self.assertIn('月', formatted_date)
    
    def test_calculate_age(self):
        current_year = datetime.now().year
        birth_year = 1990
        expected_age = current_year - birth_year + 1
        self.assertEqual(
            BaziCalculator.calculate_age(current_year, birth_year),
            expected_age
        )
    
    def test_get_bazi_and_luck_info(self):
        bazi, yun_list = BaziCalculator.get_bazi_and_luck_info(
            *self.test_date, self.gender
        )
        
        # 验证八字结构
        self.assertIsInstance(bazi, list)
        self.assertEqual(len(bazi), 4)  # 年柱、月柱、日柱、时柱
        
        # 验证五行和藏干计算
        for item in bazi:
            # 验证天干五行
            self.assertIn(item['tiangan']['wuxing'], ['木', '火', '土', '金', '水'])
            
            # 验证地支五行
            self.assertIn(item['dizhi']['wuxing'], ['木', '火', '土', '金', '水'])
            
            # 验证藏干
            self.assertIsInstance(item['dizhi']['canggan'], list)
            for canggan in item['dizhi']['canggan']:
                self.assertIn(canggan['wuxing'], ['木', '火', '土', '金', '水'])
        
        # 验证大运信息
        self.assertIsInstance(yun_list, list)
        self.assertGreater(len(yun_list), 0)
        
        # 验证每个大运的结构
        for yun in yun_list:
            self.assertIn('yun', yun)
            self.assertIn('liunian', yun)
            self.assertIn('yun_type', yun)
            self.assertIn('start_year', yun)
            self.assertIn('end_year', yun)

if __name__ == '__main__':
    unittest.main()

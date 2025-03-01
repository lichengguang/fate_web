# -*- coding: utf-8 -*-
from datetime import datetime
from lunar_python import Lunar, Solar

class BaziCalculator:
    @staticmethod
    def validate_input_date(year, month, day, hour, minute):
        """验证输入日期时间是否有效"""
        try:
            datetime(year, month, day, hour, minute)
            return True
        except ValueError:
            return False

    @staticmethod
    def create_date_objects(year, month, day, hour, minute):
        """创建阳历和农历日期对象"""
        solar = Solar.fromYmdHms(year, month, day, hour, minute, 0)
        lunar = solar.getLunar()
        return solar, lunar

    @staticmethod
    def get_formatted_lunar_date(lunar):
        """获取格式化后的农历日期字符串"""
        return f"{lunar.getYearInGanZhi()}年{lunar.getMonthInChinese()}月{lunar.getDayInChinese()}"

    @staticmethod
    def calculate_age(year, birth_year):
        """计算虚岁"""
        return year - birth_year + 1

    @classmethod
    def get_bazi_and_luck_info(cls, birth_year, birth_month, birth_day, birth_hour, birth_minute, gender):
        """获取八字和大运信息"""
        solar, lunar = cls.create_date_objects(birth_year, birth_month, birth_day, birth_hour, birth_minute)
        current_year = datetime.now().year
        current_age = cls.calculate_age(current_year, birth_year)
        
        # 获取八字并转换为对象格式
        bazi = []
        for gz in lunar.getBaZi():
            bazi.append({
                "ganzhi": gz,
                "tiangan": {
                    "name": gz[0],
                    "wuxing": "wood"  # TODO: 需要实现五行计算
                },
                "dizhi": {
                    "name": gz[1],
                    "wuxing": "wood",  # TODO: 需要实现五行计算
                    "canggan": [
                        {"name": "甲", "wuxing": "wood"},
                        {"name": "丙", "wuxing": "fire"},
                        {"name": "戊", "wuxing": "earth"}
                    ]  # 示例藏干数据，需要实现实际计算
                },
                "wuxing": "wood"  # TODO: 需要实现五行计算
            })
            
        gender_num = 1 if gender == '男' else 0
        yun = lunar.getEightChar().getYun(gender_num)

        yun_list = []
        dayun_list = yun.getDaYun()
        for dy in dayun_list:
            if dy.getGanZhi():
                d = {
                    "yun": dy.getGanZhi(),
                    "liunian": ["{}({})".format(i.getGanZhi(), i.getYear()) for i in dy.getLiuNian()],
                    "yun_type": "大运",
                    "start_year": dy.getStartYear(),
                    "end_year": dy.getEndYear()
                }
                yun_list.append(d)
        return bazi, yun_list

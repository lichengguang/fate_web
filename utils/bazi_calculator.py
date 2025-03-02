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
    def validate_lunar_date(year, month, day):
        """验证农历日期是否有效"""
        try:
            lunar = Lunar.fromYmd(year, month, day)
            return True
        except:
            return False

    @staticmethod
    def lunar_to_solar(year, month, day):
        """将农历日期转换为阳历日期"""
        lunar = Lunar.fromYmd(year, month, day)
        return lunar.getSolar()

    @staticmethod
    def create_date_objects(year, month, day, hour, minute):
        """创建阳历和农历日期对象"""
        solar = Solar.fromYmdHms(year, month, day, hour, minute, 0)
        lunar = solar.getLunar()
        return solar, lunar

    @staticmethod
    def get_formatted_lunar_date(lunar):
        """获取格式化后的农历日期字符串"""
        return f"{lunar.getYear()}年{lunar.getMonthInChinese()}月{lunar.getDayInChinese()} {lunar.getTimeZhi()}时"

    @staticmethod
    def calculate_age(year, birth_year):
        """计算虚岁"""
        return year - birth_year + 1

    # 天干五行映射
    TIANGAN_WUXING = {
        '甲': '木', '乙': '木',
        '丙': '火', '丁': '火',
        '戊': '土', '己': '土',
        '庚': '金', '辛': '金',
        '壬': '水', '癸': '水'
    }

    # 地支五行映射
    DIZHI_WUXING = {
        '寅': '木', '卯': '木',
        '巳': '火', '午': '火',
        '辰': '土', '戌': '土', '丑': '土', '未': '土',
        '申': '金', '酉': '金',
        '亥': '水', '子': '水'
    }

    # 地支藏干
    DIZHI_CANGGAN = {
        '子': ['癸'],
        '丑': ['己', '癸', '辛'],
        '寅': ['甲', '丙', '戊'],
        '卯': ['乙'],
        '辰': ['戊', '乙', '癸'],
        '巳': ['丙', '戊', '庚'],
        '午': ['丁', '己'],
        '未': ['己', '丁', '乙'],
        '申': ['庚', '壬', '戊'],
        '酉': ['辛'],
        '戌': ['戊', '辛', '丁'],
        '亥': ['壬', '甲']
    }

    # 五行颜色映射
    WUXING_COLORS = {
        '木': 'wood',
        '火': 'fire', 
        '土': 'earth',
        '金': 'metal',
        '水': 'water'
    }

    @staticmethod
    def get_wuxing_from_ganzhi(ganzhi):
        """从干支获取五行"""
        tiangan = ganzhi[0]
        dizhi = ganzhi[1] if len(ganzhi) > 1 else ''
        wuxing = []
        if tiangan in BaziCalculator.TIANGAN_WUXING:
            wuxing.append(BaziCalculator.TIANGAN_WUXING[tiangan])
        if dizhi in BaziCalculator.DIZHI_WUXING:
            wuxing.append(BaziCalculator.DIZHI_WUXING[dizhi])
        return '-'.join(wuxing)

    @staticmethod
    def get_wuxing_color(ganzhi):
        """从干支获取五行颜色"""
        wuxing = BaziCalculator.get_wuxing_from_ganzhi(ganzhi)
        colors = [BaziCalculator.WUXING_COLORS.get(w, '') for w in wuxing.split('-')]
        return '-'.join(colors)

    @classmethod
    def get_xiaoyun_info(cls, lunar, gender_num):
        """获取小运信息"""
        xiaoyun_list = []
        yun = lunar.getEightChar().getYun(gender_num)
        dayun_list = yun.getDaYun()
        
        for dy in dayun_list:
            if not dy.getGanZhi():  # 小运
                xiaoyun_list = dy.getXiaoYun()
                break
        
        result = []
        for xy in xiaoyun_list:
            result.append({
                "year": xy.getYear(),
                "ganzhi": xy.getGanZhi(),
                "age": xy.getAge(),
                "liunian": {
                    "ganzhi": xy.getGanZhi(),
                    "wuxing": cls.get_wuxing_from_ganzhi(xy.getGanZhi()),
                    "color": cls.get_wuxing_color(xy.getGanZhi())
                }
            })
        return result

    @staticmethod
    def get_chinese_zodiac(lunar):
        """获取生肖"""
        return lunar.getYearShengXiao()

    @staticmethod
    def get_formatted_birth_time(solar, lunar):
        """获取格式化后的出生时间"""
        solar_time = f"{solar.getYear()}年{solar.getMonth()}月{solar.getDay()}日 {solar.getHour()}时{solar.getMinute()}分"
        lunar_time = BaziCalculator.get_formatted_lunar_date(lunar)
        return {
            "solar": solar_time,
            "lunar": lunar_time
        }

    @classmethod
    def get_bazi_and_luck_info(cls, birth_year, birth_month, birth_day, birth_hour, birth_minute, gender):
        """获取八字、大运和小运信息"""
        solar, lunar = cls.create_date_objects(birth_year, birth_month, birth_day, birth_hour, birth_minute)
        zodiac = cls.get_chinese_zodiac(lunar)
        birth_time = cls.get_formatted_birth_time(solar, lunar)
        current_year = datetime.now().year
        current_age = cls.calculate_age(current_year, birth_year)
        
        # 获取八字并转换为对象格式
        bazi = []
        for gz in lunar.getBaZi():
            tiangan = gz[0]
            dizhi = gz[1]
            
            # 计算天干五行
            tiangan_wuxing = cls.TIANGAN_WUXING.get(tiangan, '')
            tiangan_color = cls.WUXING_COLORS.get(tiangan_wuxing, '')
            
            # 计算地支五行
            dizhi_wuxing = cls.DIZHI_WUXING.get(dizhi, '')
            dizhi_color = cls.WUXING_COLORS.get(dizhi_wuxing, '')
            
            # 计算地支藏干
            canggan_list = cls.DIZHI_CANGGAN.get(dizhi, [])
            canggan = [{
                "name": gan,
                "wuxing": cls.TIANGAN_WUXING.get(gan, ''),
                "color": cls.WUXING_COLORS.get(cls.TIANGAN_WUXING.get(gan, ''), '')
            } for gan in canggan_list]
            
            bazi.append({
                "ganzhi": gz,
                "tiangan": {
                    "name": tiangan,
                    "wuxing": tiangan_wuxing,
                    "color": tiangan_color
                },
                "dizhi": {
                    "name": dizhi,
                    "wuxing": dizhi_wuxing,
                    "color": dizhi_color,
                    "canggan": canggan
                },
                "wuxing": tiangan_wuxing,  # 以天干五行为主
                "color": tiangan_color
            })
            
        gender_num = 1 if gender == '男' else 0
        yun = lunar.getEightChar().getYun(gender_num)

        # 获取大运信息
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

        # 获取小运信息
        xiaoyun_list = cls.get_xiaoyun_info(lunar, gender_num)

        return bazi, yun_list, xiaoyun_list, zodiac, birth_time, current_age

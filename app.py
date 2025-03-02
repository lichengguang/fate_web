# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from datetime import datetime
import sys
import codecs
from utils.bazi_calculator import BaziCalculator

# 设置系统默认编码为UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # 获取表单数据
    date_type = request.form['date_type']
    birth_date = request.form['birth_date']
    birth_time = request.form['birth_time']
    gender = request.form['gender']
    
    try:
        # 解析日期时间
        birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
        birth_year = birth_datetime.year
        birth_month = birth_datetime.month
        birth_day = birth_datetime.day
        birth_hour = birth_datetime.hour
        birth_minute = birth_datetime.minute
        
        # 处理农历日期
        if date_type == 'lunar':
            if not BaziCalculator.validate_lunar_date(birth_year, birth_month, birth_day):
                raise ValueError("无效的农历日期")
            solar = BaziCalculator.lunar_to_solar(birth_year, birth_month, birth_day)
            birth_datetime = datetime(
                solar.getYear(), solar.getMonth(), solar.getDay(),
                birth_hour, birth_minute
            )
            birth_year = birth_datetime.year
            birth_month = birth_datetime.month
            birth_day = birth_datetime.day
        
        # 验证输入日期
        if not BaziCalculator.validate_input_date(birth_year, birth_month, birth_day, birth_hour, birth_minute):
            raise ValueError("无效的日期时间")
            
        # 计算八字、大运和小运
        bazi, yun_list, xiaoyun_list, zodiac, birth_time, current_age = BaziCalculator.get_bazi_and_luck_info(
            birth_year, birth_month, birth_day, birth_hour, birth_minute, gender
        )
        
        return render_template('result.html', 
                             bazi=bazi,
                             yun_list=yun_list,
                             xiaoyun_list=xiaoyun_list,
                             current_year=datetime.now().year,
                             zodiac=zodiac,
                             birth_time=birth_time,
                             gender=gender,
                             age=current_age)
        
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

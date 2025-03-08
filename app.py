# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify, session
import requests
import os
from dotenv import load_dotenv

load_dotenv()
from datetime import datetime
from utils.bazi_calculator import BaziCalculator

app = Flask(__name__)
app.secret_key = os.urandom(24)

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
        # 存储当前命盘数据用于AI分析
        session['current_bazi'] = bazi
        session['current_gender'] = gender
        session['current_age'] = current_age
        session['current_yun_list'] = yun_list or []
        session['current_xiaoyun_list'] = xiaoyun_list or []
        session['current_zodiac'] = zodiac or ''
        session['current_birth_time'] = birth_time
        return render_template('result.html', 
                             bazi=bazi,
                             yun_list=yun_list or [],
                             xiaoyun_list=xiaoyun_list or [],
                             current_year=datetime.now().year,
                             zodiac=zodiac or '',
                             birth_time=birth_time,
                             gender=gender,
                             age=current_age)
        
    except Exception as e:
        # 记录错误日志
        app.logger.error(f'计算错误: {str(e)}', exc_info=True)
        return render_template('error.html', error='系统繁忙，请检查输入格式')

def get_ai_analysis(bazi_data, gender, age, yun_list, xiaoyun_list, zodiac, birth_time):
    if not isinstance(bazi_data, list) or len(bazi_data) < 4 or any(not isinstance(pillar, dict) for pillar in bazi_data):
        return None
    
    api_key = os.getenv('DEEPSEEK_API_KEY')
    
    prompt = f'''以专业命理师身份分析以下八字：
【基本命盘】
年柱：{bazi_data[0]["ganzhi"]}
月柱：{bazi_data[1]["ganzhi"]}
日柱：{bazi_data[2]["ganzhi"]}
时柱：{bazi_data[3]["ganzhi"]}

精确生辰：{birth_time.get('solar', '')}（阳历）/{birth_time.get('lunar', '')}（农历）
性别：{gender}，当前年龄：{age}岁
生肖属相：{zodiac}
小运及流年信息：{xiaoyun_list}
大运的起运年份：{yun_list[0]['start_year']}
大运及流年信息：{yun_list}

请按以下结构分析：
1. 命盘格局分析
2. 五行强弱分析
3. 大运走势建议
4. 流年注意事项
5. 个性化发展建议
'''


    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'model': 'deepseek-chat',
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.7
    }

    try:
        response = requests.post("https://api.deepseek.com/v1/chat/completions?model=deepseek-chat", json=data, headers=headers)
    
        if response.status_code != 200:
            raise Exception(f"API请求失败: {response.status_code} {response.text}")
            
        result = response.json()

        
        if 'choices' not in result or len(result['choices']) == 0:
            raise Exception("无效的API响应格式")
            
        return result['choices'][0]['message']['content']

    except Exception as e:
        print(f'AI分析错误: {str(e)}')
        return None

@app.route('/get_ai_analysis')
def get_ai_analysis_route():
    bazi_data = session.get('current_bazi', [])
    yun_list = session.get('current_yun_list', [])
    xiaoyun_list = session.get('current_xiaoyun_list', [])
    zodiac = session.get('current_zodiac', '')
    birth_time = session.get('current_birth_time', {})
    gender = session.get('current_gender')
    age = session.get('current_age')

    if not isinstance(bazi_data, list) or len(bazi_data) < 4 or any(not isinstance(item, dict) for item in bazi_data):
        return jsonify({'error': '无效的命盘数据结构'})
    if not all(isinstance(lst, list) for lst in [yun_list, xiaoyun_list]):
        return jsonify({'error': '运势数据格式错误'})
    
    try:
        gender = session.get('current_gender') # 男 or 女
        age = session.get('current_age')
        
        if not gender or not age:
            return jsonify({'error': '用户数据缺失，请重新计算'})
        
        analysis = get_ai_analysis(bazi_data, gender, age, yun_list, xiaoyun_list, zodiac, birth_time)
        return jsonify({'analysis': analysis})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)

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
    
    prompt = f'''你作为中国传统命理学专家，完整掌握《三命通会》《滴天髓》《渊海子平》《穷通宝鉴》理论体系‌，各派融会贯通，能交叉验证盲派、子平派技法差异‌。 请你对以下命盘进行细致分析:
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

### 核心分析模块
列出八字的五行属性，天干、地支、藏干、天干五行、地支五行\纳音、神煞等信息。
分析角度: 职业、学历、财富、婚姻、健康状况、六亲状况、性情描述...
定调：对命局有一个简单的论断，确定大的方向。
过三关：包括父母关、兄弟关、婚姻关。
解析大运流年：详细分析大运流年，预测人生重大事项。
你可以综合《渊海子平》《三命通会》《滴天髓阐微》《子平真诠》等书籍的内容，结合命主的信息给出关键的解析，盲派算命也有许多经典口诀，用于推断命主的命运，你也可以使用恰当的口诀来帮助命主理解命局。
'''


    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'model': 'deepseek-reasoner',
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.7
    }

    try:
        response = requests.post("https://api.deepseek.com/v1/chat/completions?model=deepseek-reasoner", json=data, headers=headers)
    
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

# 八字排盘系统 🎴

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 项目简介
这是一个基于Python Flask的八字排盘系统，可以根据用户输入的出生时间生成八字命盘。

## 🚀 功能状态

| 功能 | 状态 |
|------|------|
| ✅ 八字排盘 | 已完成 |
| ✅ 五行分析 | 已完成 |
| ✅ 大运推算 | 已完成 |
| ✅ 流年运势 | 已完成 |
| ⏳ 即时起盘功能 | 开发中 |
| ⏳ 阳历/阴历选择 | 开发中 |
| ⏳ AI命理分析 | 开发中 |
| ⏳ 命盘分享功能 | 开发中 |

## 🛠️ 安装指南

### 1. 克隆项目
```bash
git clone https://github.com/lichengguang/fate_web.git
cd fate_web
```

### 2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

## 🎯 使用说明

### 启动服务
```bash
python app.py
```

### 访问应用
打开浏览器访问 [http://localhost:5000](http://localhost:5000)

### 输入信息
1. 输入出生日期和时间
2. 查看生成的八字命盘及大运、流年

## 🧑‍💻 开发指南

### 项目结构
```
fate_web/
├── app.py
├── requirements.txt
├── static/
├── templates/
├── tests/
└── utils/
```

### 代码规范
- 遵循PEP 8规范
- 使用类型注解
- 添加必要的文档注释

### 测试说明
```bash
pytest tests/
```

## 🤝 贡献指南
欢迎通过以下方式贡献代码：
1. 提交issue报告问题
2. 创建pull request提交改进
3. 完善文档和测试用例

## 📜 许可证
本项目采用 [MIT 许可证](LICENSE)

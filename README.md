# 八字排盘系统 🎴

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 项目简介
这是一个基于Python Flask的八字排盘系统，可以根据用户输入的出生时间生成八字命盘,并进行AI分析(DeepSeek)。

## 📚 文档导航
- [用户手册](docs/USER_GUIDE.md) - 系统使用说明
- [开发指南](docs/DEVELOPMENT.md) - 项目开发说明
- [贡献指南](docs/CONTRIBUTING.md) - 如何参与贡献
- [CHANGELOG指南](docs/CHANGELOG_GUIDE.md) - 版本更新说明

## 🚀 功能状态

| 功能 | 状态 |
|------|------|
| ✅ 八字排盘 | 已完成 |
| ✅ 大运计算 | 已完成 |
| ✅ 流年计算 | 已完成 |
| ✅ 生肖计算 | 已完成 |
| ✅ 年龄计算 | 已完成 |
| ✅ 阴阳历转换 | 已完成 |
| ⏳ 命理AI分析 | 开发中 |
| ⏳ 纳音计算 | 开发中 |
| ⏳ 命理知识库 | 计划中 |
| ⏳ 用户命盘收藏 | 计划中 |

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

### 4. 环境配置
复制示例环境文件并配置：
```bash
cp .env.example .env
```
按需编辑.env文件中的配置项：
```ini
# DeepSeek API Key
DEEPSEEK_API_KEY=your-secret-key-here
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

## 🛠️ 维护说明

本项目采用语义化版本控制，所有功能更新和修复都会记录在[CHANGELOG.md](CHANGELOG.md)中。建议开发者在提交代码时：
- 遵循[Keep a Changelog](https://keepachangelog.com/)规范
- 使用语义化版本号（SemVer）
- 详细描述变更内容

## 🤝 贡献指南
欢迎通过以下方式贡献代码：
1. 提交issue报告问题
2. 创建pull request提交改进
3. 完善文档和测试用例

## 📜 许可证
本项目采用 [MIT 许可证](LICENSE)

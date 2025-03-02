# 开发指南

## 项目结构
```
fate_web/
├── app.py                # 主应用入口
├── utils/                # 工具模块
│   └── bazi_calculator.py # 八字计算核心逻辑
├── templates/            # 前端模板
├── static/               # 静态资源
├── tests/                # 测试代码
└── docs/                 # 项目文档
```

## 核心模块说明
### 八字计算模块 (bazi_calculator.py)
- 功能：计算八字、大运、流年
- 依赖：lunar_python库
- 主要接口：
  ```python
  def calculate_bazi(birth_datetime: datetime, gender: str) -> BaziResult
  ```

### 前端模板
- index.html：输入页面
- result.html：结果展示页面
- error.html：错误页面

## 测试说明
- 使用pytest框架
- 测试文件位于tests目录
- 运行测试：
  ```bash
  pytest tests/
  ```

## 部署说明
1. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
2. 启动服务
   ```bash
   python app.py
   ```
3. 访问地址
   http://localhost:5000

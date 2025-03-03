# 八字排盘系统 🎴

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 项目简介
这是一个基于Python Flask的八字排盘系统，可以根据用户输入的出生时间生成八字命盘。

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
| ⏳ 纳音计算 | 开发中 |
| ⏳ 神煞计算 | 开发中 |
| ⏳ 命理AI分析 | 开发中 |
| ⏳ 命理知识库 | 计划中 |
| ⏳ 用户命盘收藏 | 计划中 |

## 🛠️ 安装指南

### 1. Python环境安装

#### Windows系统
1. 访问[Python官网](https://www.python.org/downloads/windows/)下载最新安装包
2. 安装时勾选"Add Python to PATH"选项
3. 验证安装：
```bash
python --version
# 应显示Python 3.8或更高版本
```

#### macOS系统
```bash
# 使用Homebrew安装
brew install python@3.8

# 验证安装
python3 --version
```

#### Linux系统 (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.8 python3-pip
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
```

### 2. 克隆项目
```bash
git clone https://github.com/lichengguang/fate_web.git
cd fate_web
```

### 3. 虚拟环境配置

#### 创建环境（支持多Python版本）
```bash
# 指定Python解释器路径
python -m venv venv --prompt fate_web
```

#### 激活环境
```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

#### 退出环境
```bash
deactivate
```

### 4. 安装依赖
```bash
pip install -r requirements.txt

# 国内用户可使用镜像加速
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 5. 环境验证

#### 检查Python版本
```bash
python -c "import sys; print(f'Python版本: {sys.version}')"
```

#### 检查依赖完整性
```bash
pip list --format=columns
```

### 6. 常见问题

| 问题现象 | 解决方案 |
|---------|----------|
| 命令未找到 | 检查Python是否加入PATH环境变量 |
| 虚拟环境激活失败 | 使用`chmod +x venv/bin/activate`添加执行权限 |
| 依赖安装超时 | 使用`--default-timeout=100`参数或更换镜像源 |
| 版本冲突 | 使用`pip check`验证依赖兼容性 |
# 八字排盘系统 🎴

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 项目简介
这是一个基于Python Flask的八字排盘系统，可以根据用户输入的出生时间生成八字命盘。

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
| ⏳ 纳音计算 | 开发中 |
| ⏳ 神煞计算 | 开发中 |
| ⏳ 命理AI分析 | 开发中 |
| ⏳ 命理知识库 | 计划中 |
| ⏳ 用户命盘收藏 | 计划中 |

## 🛠️ 安装指南

### 1. Python环境安装

#### Windows系统
1. 访问[Python官网](https://www.python.org/downloads/windows/)下载最新安装包
2. 安装时勾选"Add Python to PATH"选项
3. 验证安装：
```bash
python --version
# 应显示Python 3.8或更高版本
```

#### macOS系统
```bash
# 使用Homebrew安装
brew install python@3.9

# 验证安装
python3 --version
```

#### Linux系统 (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.9 python3-pip
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
```

### 2. 克隆项目
```bash
git clone https://github.com/lichengguang/fate_web.git
cd fate_web
```

### 3. 虚拟环境配置

#### 创建环境（支持多Python版本）
```bash
# 指定Python解释器路径
python -m venv venv --prompt fate_web
```

#### 激活环境
```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

#### 退出环境
```bash
deactivate
```

### 4. 安装依赖
```bash
pip install -r requirements.txt

# 国内用户可使用镜像加速
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 5. 环境验证

#### 检查Python版本
```bash
python -c "import sys; print(f'Python版本: {sys.version}')"
```

#### 检查依赖完整性
```bash
pip list --format=columns
```

### 6. 常见问题

| 问题现象 | 解决方案 |
|---------|----------|
| 命令未找到 | 检查Python是否加入PATH环境变量 |
| 虚拟环境激活失败 | 使用`chmod +x venv/bin/activate`添加执行权限 |
| 依赖安装超时 | 使用`--default-timeout=100`参数或更换镜像源 |
| 版本冲突 | 使用`pip check`验证依赖兼容性 |
# 八字排盘系统 🎴

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 项目简介
这是一个基于Python Flask的八字排盘系统，可以根据用户输入的出生时间生成八字命盘。

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
| ⏳ 纳音计算 | 开发中 |
| ⏳ 神煞计算 | 开发中 |
| ⏳ 命理AI分析 | 开发中 |
| ⏳ 命理知识库 | 计划中 |
| ⏳ 用户命盘收藏 | 计划中 |

## 🛠️ 安装指南

### 1. Python环境安装

#### Windows系统
1. 访问[Python官网](https://www.python.org/downloads/windows/)下载最新安装包
2. 安装时勾选"Add Python to PATH"选项
3. 验证安装：
```bash
python --version
# 应显示Python 3.8或更高版本
```

#### macOS系统
```bash
# 使用Homebrew安装
brew install python@3.9

# 验证安装
python3 --version
```

#### Linux系统 (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.9 python3-pip
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
```

### 2. 克隆项目
```bash
git clone https://github.com/lichengguang/fate_web.git
cd fate_web
```

### 3. 虚拟环境配置

#### 创建环境（支持多Python版本）
```bash
# 指定Python解释器路径
python -m venv venv --prompt fate_web
```

#### 激活环境
```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

#### 退出环境
```bash
deactivate
```

### 4. 安装依赖
```bash
pip install -r requirements.txt

# 国内用户可使用镜像加速
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 5. 环境验证

#### 检查Python版本
```bash
python -c "import sys; print(f'Python版本: {sys.version}')"
```

#### 检查依赖完整性
```bash
pip list --format=columns
```

### 6. 常见问题

| 问题现象 | 解决方案 |
|---------|----------|
| 命令未找到 | 检查Python是否加入PATH环境变量 |
| 虚拟环境激活失败 | 使用`chmod +x venv/bin/activate`添加执行权限 |
| 依赖安装超时 | 使用`--default-timeout=100`参数或更换镜像源 |
| 版本冲突 | 使用`pip check`验证依赖兼容性 |
# 八字排盘系统 🎴

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 项目简介
这是一个基于Python Flask的八字排盘系统，可以根据用户输入的出生时间生成八字命盘。

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
| ⏳ 纳音计算 | 开发中 |
| ⏳ 神煞计算 | 开发中 |
| ⏳ 命理AI分析 | 开发中 |
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

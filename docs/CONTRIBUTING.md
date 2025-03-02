# 贡献指南

## 🛠️ 开发环境配置
1. 克隆仓库
   ```bash
   git clone https://github.com/your-repo/fate_web.git
   ```
2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
3. 配置环境变量
   ```bash
   cp .env.example .env
   ```

## 📝 代码规范
- 遵循PEP 8 Python代码风格
- 使用类型注解
- 函数注释使用Google风格
- 提交信息遵循Conventional Commits规范

## 🚦 开发流程
1. 从main分支创建新分支
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. 开发完成后提交代码
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```
3. 创建Pull Request
   - 描述功能变更
   - 关联相关issue
   - 通过CI测试

## 🐛 问题报告
- 使用GitHub Issues报告问题
- 提供重现步骤
- 包含相关截图或日志

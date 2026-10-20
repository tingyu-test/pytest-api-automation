# Pytest 接口自动化测试项目

🔗 [点击查看在线 Allure 测试报告](https://tingyu-test.github.io/pytest-api-automation/)

基于 Python + Pytest + Requests 搭建的接口自动化测试框架。

## 📁 项目结构

- `config/`：配置文件（环境地址、数据库等）
- `testcases/`：测试用例
- `utils/`：工具类（请求封装、断言、Excel 处理等）
- `date/`：测试数据
- `report/`：测试报告
- `conftest.py`：Pytest 全局配置
- `pytest.ini`：Pytest 运行配置
- `run.py`：测试执行入口

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt

###2. 运行测试

pytest

python run.py

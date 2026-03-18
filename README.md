# Dedication vs Immunization: 负债驱动投资组合优化

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

## 📌 项目简介

本项目实现了一个完整的**负债驱动投资(LDI)**框架，使用线性规划求解最低成本的债券组合，以匹配未来8年的负债现金流。

**核心模型**：Dedication (现金流匹配)

## 📊 数据说明

- **负债流**：未来8年每年6月和12月的支付需求
- **国债收益率**：用于计算负债现值的无风险利率
- **可选债券**：10种不同期限和票息的国债/机构债

## 🛠️ 技术栈

- Python 3.8+
- NumPy/Pandas: 数据处理
- SciPy: 线性规划求解
- Matplotlib: 可视化
- Jupyter Notebook: 交互式分析

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/你的用户名/Dedication-Immunization-LP.git
cd Dedication-Immunization-LP

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境 (Windows)
venv\Scripts\activate
# 激活虚拟环境 (Mac/Linux)
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 启动Jupyter
jupyter notebook
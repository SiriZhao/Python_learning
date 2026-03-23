# 🐍 Python 学习笔记 (Daily-Python-Learning)

> **"Done is better than perfect."** — 每天进步 1%，一年就是 37 倍的成长。

## 🎯 阶段目标
- [x] **Phase 1: 基础夯实** (数据类型、循环、判断、函数)
- [x] **Phase 2: 进阶提升** (文件操作、异常处理、模块化)
- [ ] **Phase 3: 实战演练** (爬虫、数据分析或自动化办公)

## 🛠️ 运行环境
- Python 版本: 3.13
- IDE: VS Code 

### 📂 笔记说明
* [Notes_basic.py](Notes/Notes_basic.py) - Python 基础
* [Notes_Advanced.py](Notes/Notes_Advanced.py) - 面向对象编程


# Python 编程进阶之路 (Python-Learning-Journey)

这个仓库记录了我从 Python 基础语法到进阶爬虫实战的学习历程。代码涵盖了逻辑控制、算法优化、函数式编程及自动化数据采集等多个模块。

## 📂 模块说明

### 🎮 01. 基础逻辑与算法游戏 (Basic Logic & Games)
探索 Python 的循环、条件分支以及经典的算法实现。
* **猜数字系列**: 包含从基础的用户交互版 `guess_num_human.py` 到基于二分查找算法的 AI 自动猜测版 `guess_num_ai_advanced.py`。
* **二分查找**: `binary_search_logic.py` 展示了如何通过数学逻辑将 $O(n)$ 的搜索复杂度降低至 $O(\log n)$。
* **逻辑练习**: `reverse_9x9_table.py`（嵌套循环应用） 与 `list_custom_ops.py`（手动实现列表清空与深度倒序逻辑）。

### 🛠️ 02. 系统设计与实用工具 (System Tools)
模拟真实业务场景，练习函数封装与异常处理。
* **业务系统**: `member_recharge_system.py` 模拟了包含多级优惠和新老用户福利的会员充值逻辑。
* **健康管理**: `bmi_health_analyzer.py` 使用类型注解（Type Hinting）编写的健壮 BMI 计算器。
* **高阶函数**: `callback_progress_wrapper.py` 演示了如何将函数作为参数传递（回调机制），实现动态任务进度监控。

### 🕷️ 03. 网络爬虫与数据自动化 (Web Spiders)
利用 Python 进行高效的数据采集与分析。
* **Bilibili API 爬虫**: 自动获取视频列表数据并导出为结构化的 Excel 文档。
* **豆瓣电影爬虫**: 实现了一个具备 **Session 会话管理**、**自动重试机制** 以及 **本地 JSON 缓存（断点续爬）** 功能的高阶爬虫脚本。

## 🚀 技术要点
* **鲁棒性**: 广泛使用 `try-except` 处理非标准输入，确保程序不会因异常中断。
* **自动化**: 结合 `pandas` 和 `openpyxl` 实现了从网络数据抓取到本地表格存储的全自动化流程。
* **性能意识**: 在 AI 猜数字项目中引入了二分查找，并对比了理论最优猜测次数。

## 🛠️ 环境依赖
* Python 3.8+
* 第三方库: `requests`, `pandas`, `beautifulsoup4`, `openpyxl`

## ⚖️ 免责声明
本仓库中的爬虫脚本仅用于个人学习和技术研究。请勿用于商业用途或大规模高频抓取，使用时请遵守相关平台的 `robots.txt` 协议。

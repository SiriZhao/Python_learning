# 🐍 Python 学习笔记 (Daily-Python-Learning)

> **"Done is better than perfect."** — 每天进步 1%，一年就是 37 倍的成长。

## 🎯 阶段目标
- [x] **Phase 1: 基础夯实** (数据类型、循环、判断、函数)
- [x] **Phase 2: 进阶提升** (文件操作、异常处理、模块化)
- [x] **Phase 3: 实战演练** (爬虫、数据分析或自动化办公)

## 🛠️ 运行环境
- Python 版本: 3.13
- IDE: VS Code 

### 📂 笔记说明
* [Notes_basic.py](Notes/Notes_basic.py) - Python 基础
* [Notes_Advanced.py](Notes/Notes_Advanced.py) - 面向对象编程


# Python 编程进阶之路 (Python-Learning-Journey)

这个仓库是我系统学习 Python 的实战记录，涵盖了从零基础语法到进阶网络爬虫的完整过程。

## 📂 项目模块说明

### 🎮 01. 算法练习与益智游戏 (Algorithms & Games)
* **二分查找系列**: 
    * `guess_num_ai_advanced.py`: 模拟 AI 使用二分法在千万级数据中精准定位目标。
    * `binary_search_logic.py`: 封装了标准的二分查找函数，支持自定义区间与返回值解包。
* **人机交互**: `guess_num_human.py` 包含异常处理机制的经典猜数字游戏。

### 🛠️ 02. 系统设计与实用工具 (System & Tools)
* **高阶函数实战**: `callback_wrapper_demo.py` 演示了如何将函数作为参数传递，实现任务完成后的自动回调。
* **业务逻辑模拟**: `member_recharge_system.py` 模拟复杂的会员充值算法，包含新老客户判定及多级赠送逻辑。
* **健康分析**: `bmi_health_analyzer.py` 使用类型注解实现的 BMI 计算工具。
* **动态进度条**: `simple_progress_bar.py` 利用 `\r` 实现的控制台动态刷新进度条。

### 🕷️ 03. 网络爬虫与数据处理 (Web Spiders)
* **Bilibili 数据采集**: `bilibili_video_spider.py` 抓取 B 站 API 数据，利用 `pandas` 处理时间戳并导出 Excel。
* **豆瓣电影爬虫**: `douban_movie_spider.py` 具备 **Session 会话管理**、**自动重试**及**断点续爬（JSON 缓存）**功能的高阶爬虫。

### 📚 04. 基础逻辑沉淀 (Syntax Foundation)
* **循环应用**: `reverse_9x9_table.py` 倒序九九乘法表。
* **数列操作**: `list_custom_ops.py` 手动实现列表清空逻辑与子列表嵌套倒序排列。

## 🚀 技术亮点
1. **健壮性**: 广泛应用 `try-except` 捕获无效输入和网络请求异常。
2. **算法意识**: 通过猜数字项目实践了二分查找，理解了 $O(\log n)$ 的效率优势。
3. **工程化思维**: 在爬虫项目中引入了缓存机制和 Session 持久化，有效应对反爬。

## 🛠️ 环境准备
1. 安装 Python 3.8+
2. 安装依赖：`pip install requests pandas beautifulsoup4 openpyxl`

## ⚖️ 免责声明
本仓库中的爬虫脚本仅用于个人学习和技术研究。请勿用于商业用途或大规模高频抓取，使用时请遵守相关平台的 `robots.txt` 协议。

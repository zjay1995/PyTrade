# PyTrade

本代码为一个基于python的交易系统，接受并输出可以让整个系统获得最大收益的交易请求列表（按顺序排列，并包括每个交易中选择执行的转账）以及执行结束后的用户余额和系统收益。

## 需求
本程序使用Python 3编写

## 设置
通过执行以下命令来运行测试：
python test_system.py
通过修改 User, Transaction, Request和 System Class 来定制交易系统。

## 测试
测试位于 test_system.py 文件中。使用unittest模块运行。测试覆盖了交易系统的基本功能。

## 假设
输入的交易格式正确。
交易涉及的用户已经存在于系统中。
用户的余额是非负数字。

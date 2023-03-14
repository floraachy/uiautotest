# -*- coding: utf-8 -*-
# @Version: Python 3.9
# @Time    : 2023/3/13 16:41
# @Author  : chenyinhua
# @File    : login_demo_data.py
# @Software: PyCharm
# @Desc: 登录功能 测试数据

cases_data = [
    {"title": "正确用户名和密码登录成功 （弹窗登录）",  "user": "${login}", "password": "${password}", "run": True},
    {"title": "正确用户名和错误密码登录成功 （弹窗登录）",  "user": "${login}", "password": "xxxxxxxx", "run": False}
             ]


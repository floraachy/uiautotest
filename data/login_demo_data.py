# -*- coding: utf-8 -*-
# @Version: Python 3.9
# @Time    : 2023/3/13 16:41
# @Author  : chenyinhua
# @File    : login_demo_data.py
# @Software: PyCharm
# @Desc: 登录功能 测试数据

login_case_data = {
    "case_common":
        {
            "allure_epic": "Demo用例",
            "allure_feature": "登录模块",
            "allure_story": "弹窗登录"
        },
    "case_login_demo_01":
        {"feature": "登录", "title": "正确用户名和密码登录成功 （弹窗登录）", "user": "${login}", "password": "${password}", "run": True,
         "severity": "critical"},
    "case_login_demo_02":
        {"feature": "登录", "title": "正确用户名和错误密码登录成功 （弹窗登录）", "user": "${login}", "password": "xxxxxxxx", "run": True,
         "severity": "normal"},
}

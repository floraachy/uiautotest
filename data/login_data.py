# -*- coding: utf-8 -*-
# @Version: Python 3.9
# @Time    : 2023/3/13 16:41
# @Author  : chenyinhua
# @File    : login_data.py
# @Software: PyCharm
# @Desc: 登录功能 测试数据

case_common = {
    "allure_epic": "GitLink",
    "allure_feature": "登录模块",
}

# 登录成功
login_pop_success = {
    "allure_story": "弹窗登录",
    "cases":
        [
            {"title": "弹窗登录: 正确用户名和密码登录成功", "user": "${login}", "password": "${password}",
             "run": True,
             "severity": "critical"}
        ]
}

login_page_success = {
    "allure_story": "网页登录",
    "cases":
        [
            {"title": "网页登录: 正确用户名和密码登录成功", "user": "${login}", "password": "${password}",
             "run": True,
             "severity": "critical"
             }

        ]
}

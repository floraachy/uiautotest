# -*- coding: utf-8 -*-
# @Version: Python 3.9
# @Time    : 2023/1/9 17:08
# @Author  : chenyinhua
# @File    : settings.py
# @Software: PyCharm
# @Desc: 项目配置文件

driver_type = "chrome-headless"

# 测试环境配置
test = [
    {
        # 示例测试环境及示例测试账号
        "host": "https://testforgeplus.trustie.net/",
        "login": "chytest10",
        "password": "12345678",
        "nickname": "chy测试10",
        "user_id": "85422"
    }
]
live = [
    {
        "host": "https://www.gitlink.org.cn",
        "login": "******",
        "password": "******",
        "nickname": "******",
        "user_id": "******"
    }
]

# 测试报告的定制化信息展示
REPORT_TITLE = "自动化测试报告"
REPORT_NAME = "uiautotest-report.html"
PROJECT_NAME = "GitLink 确实开源"
TESTER = "测试人员：陈银花"
DEPARTMENT = "所属部门: 开源协同创新中心"


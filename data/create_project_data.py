# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 14:40
# @Author  : chenyinhua
# @File    : create_project_data.py
# @Software: PyCharm
# @Desc:
# 标准库导入
import random

# 第三方库导入
# 本地应用/模块导入


case_common = {
    "allure_epic": "GitLink",
    "allure_feature": "开源项目模块",
}

# 新建项目成功  (注意：project_language可选值范围 不能与 ignore 重复，否则可能出现选择项目语言，实际选择的是ignore)
new_project_success = {
    "allure_story": "新建项目",
    "cases":
        [
            {
                "title": "登录状态下，通过右上角导航栏点击新建>新建项目按钮， 新建个人公有项目",
                "name": "Auto Test ${generate_name()}",
                "desc": "${generate_name()}",
                "identifier": "${generate_identifier()}",
                "project_category": random.choice(["机器学习", "大数据", "深度学习", "人工智能", "量子计算", "智慧医疗", "自动驾驶", "其他"]),
                "project_language": random.choice(["C#", "HTML", "CSS", "Python3.6"]),
                "ignore": random.choice(["Ada", "Actionscript", "Ansible", "Android", "Agda"]),
                "license": random.choice(["0BSD", "AAL", "AFL-1.1", "389-exception"]),
                "private": False,
                "run": True,
                "severity": "critical"
            },
            {
                "title": "登录状态下，通过右上角导航栏点击新建>新建项目按钮， 新建个人私有项目",
                "name": "Auto Test ${generate_name()}",
                "desc": "${generate_name()}",
                "identifier": "${generate_identifier()}",
                "project_category": random.choice(["机器学习", "大数据", "深度学习", "人工智能", "量子计算", "智慧医疗", "自动驾驶", "其他"]),
                "project_language": random.choice(["C#", "HTML", "CSS", "Python3.6"]),
                "ignore": random.choice(["Ada", "Actionscript", "Ansible", "Android", "Agda"]),
                "license": random.choice(["0BSD", "AAL", "AFL-1.1", "389-exception"]),
                "private": True,
                "run": True,
                "severity": "critical"
            }
        ]
}

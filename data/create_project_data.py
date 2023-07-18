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
                "run": True,
                "severity": "critical",
                "name": "Auto Test ${generate_name()}",
                "desc": "${generate_name()}",
                "identifier": "${generate_identifier()}",
                "project_category": random.choice(["机器学习", "大数据", "深度学习", "人工智能", "量子计算", "智慧医疗", "自动驾驶", "其他"]),
                "project_language": random.choice(["C#", "HTML", "CSS", "Python3.6"]),
                "ignore": random.choice(["Ada", "Actionscript", "Ansible", "Android", "Agda"]),
                "license": random.choice(["0BSD", "AAL", "AFL-1.1", "389-exception"]),
                "private": False,
            },
            {
                "title": "登录状态下，通过右上角导航栏点击新建>新建项目按钮， 新建个人私有项目",
                "run": True,
                "severity": "critical",
                "name": "Auto Test ${generate_name()}",
                "desc": "${generate_name()}",
                "identifier": "${generate_identifier()}",
                "project_category": random.choice(["机器学习", "大数据", "深度学习", "人工智能", "量子计算", "智慧医疗", "自动驾驶", "其他"]),
                "project_language": random.choice(["C#", "HTML", "CSS", "Python3.6"]),
                "ignore": random.choice(["Ada", "Actionscript", "Ansible", "Android", "Agda"]),
                "license": random.choice(["0BSD", "AAL", "AFL-1.1", "389-exception"]),
                "private": True
            }
        ]
}

export_project_success = {
    "allure_story": "导入项目",
    "cases":
        [
            {
                "title": "登录状态下，通过右上角导航栏点击新建>导入项目按钮， 导入github项目（公开仓库）作为个人公开仓库",
                "run": False,
                "severity": "critical",
                "mirror_url": "https://github.com/Stability-AI/StableStudio.git",  # 根仓库URL地址
                "mirror_private": False,  # 根仓库 公私有状态
                "name": "Auto Test ${generate_name()}",
                "desc": "${generate_name()}",
                "identifier": "${generate_identifier()}",
                "project_category": random.choice(["机器学习", "大数据", "深度学习", "人工智能", "量子计算", "智慧医疗", "自动驾驶", "其他"]),
                "project_language": random.choice(["C#", "HTML", "CSS", "Python3.6"]),
                "ignore": random.choice(["Ada", "Actionscript", "Ansible", "Android", "Agda"]),
                "license": random.choice(["0BSD", "AAL", "AFL-1.1", "389-exception"]),
                "private": False,  # 导入过来的仓库的公私有状态
                "mirror_type": True,  # 是否设置该仓库为一个同步镜像仓库

            },
            {
                "title": "登录状态下，通过右上角导航栏点击新建>导入项目按钮， 导入gitee项目（公开仓库）作为个人公开仓库",
                "run": False,
                "severity": "Normal",
                "mirror_url": "https://gitee.com/mirrors/pytest.git",
                "mirror_private": False,
                "name": "Auto Test ${generate_name()}",
                "desc": "${generate_name()}",
                "identifier": "${generate_identifier()}",
                "project_category": random.choice(["机器学习", "大数据", "深度学习", "人工智能", "量子计算", "智慧医疗", "自动驾驶", "其他"]),
                "project_language": random.choice(["C#", "HTML", "CSS", "Python3.6"]),
                "ignore": random.choice(["Ada", "Actionscript", "Ansible", "Android", "Agda"]),
                "license": random.choice(["0BSD", "AAL", "AFL-1.1", "389-exception"]),
                "private": False,
                "mirror_type": True,

            },
            {
                "title": "登录状态下，通过右上角导航栏点击新建>导入项目按钮， 导入github项目（私有仓库）作为个人私有仓库",
                "run": False,
                "severity": "critical",
                "mirror_url": "https://github.com/xxx.git",
                "mirror_private": True,
                "auth_token": "",
                "name": "Auto Test ${generate_name()}",
                "desc": "${generate_name()}",
                "identifier": "${generate_identifier()}",
                "project_category": random.choice(["机器学习", "大数据", "深度学习", "人工智能", "量子计算", "智慧医疗", "自动驾驶", "其他"]),
                "project_language": random.choice(["C#", "HTML", "CSS", "Python3.6"]),
                "ignore": random.choice(["Ada", "Actionscript", "Ansible", "Android", "Agda"]),
                "license": random.choice(["0BSD", "AAL", "AFL-1.1", "389-exception"]),
                "private": True,
                "mirror_type": True,

            },
            {
                "title": "登录状态下，通过右上角导航栏点击新建>导入项目按钮， 导入gitee项目（私有仓库）作为个人私有仓库",
                "run": False,
                "severity": "critical",
                "mirror_url": "https://gitee.com/mirrors/xxx.git",
                "mirror_private": True,
                "auth_user": "",
                "auth_password": "",
                "name": "Auto Test ${generate_name()}",
                "desc": "${generate_name()}",
                "identifier": "${generate_identifier()}",
                "project_category": random.choice(["机器学习", "大数据", "深度学习", "人工智能", "量子计算", "智慧医疗", "自动驾驶", "其他"]),
                "project_language": random.choice(["C#", "HTML", "CSS", "Python3.6"]),
                "ignore": random.choice(["Ada", "Actionscript", "Ansible", "Android", "Agda"]),
                "license": random.choice(["0BSD", "AAL", "AFL-1.1", "389-exception"]),
                "private": False,
                "mirror_type": True,

            }
        ]
}

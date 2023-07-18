# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 14:39
# @Author  : chenyinhua
# @File    : test_create_and_delete_project.py
# @Software: PyCharm
# @Desc:
# 标准库导入
# 第三方库导入
import time

import pytest
import allure
from loguru import logger
# 本地应用/模块导入
from config.global_vars import GLOBAL_VARS
from page.common_page import CommonPage
from page.home_page import HomePage
from page.projects.create_project_page import CreateProjectPage
from page.projects.project_detail_page import ProjectDetailPage
from data.create_project_data import *
from case_utils.data_handle import data_handle, eval_data_process
from case_utils.allure_handle import allure_title, allure_step


@allure.epic(case_common["allure_epic"])
@allure.feature(case_common["allure_feature"])
class TestCreateProject:
    """
    新建项目/导入项目的测试用例
    """

    @allure.story(new_project_success["allure_story"])
    @pytest.mark.parametrize("case", new_project_success["cases"],
                             ids=["{}".format(case["title"]) for case in new_project_success["cases"]])
    def test_new_project(self, init_drivers, case, login_api):
        """
        1. 用户新建个人项目
        2. 用户作为拥有者，通过仓库设置删除项目
        """
        logger.debug("\n-----------------------------START-开始执行用例-----------------------------\n")
        # 处理用例数据
        case = eval_data_process(data_handle(obj=case, source=GLOBAL_VARS))
        logger.debug(f"当前执行的用例数据:{case}, {type(case)}")

        # 处理URL
        host = GLOBAL_VARS.get("host", "")

        # 添加用例标题作为allure中显示的用例标题
        allure_title(case.get("title", ""))
        for driver in init_drivers:
            allure_step(step_title=f"当前运行的浏览器驱动是：{driver}")
            logger.debug(f"当前运行的浏览器驱动是：{driver}")

            driver.delete_all_cookies()
            allure_step(step_title="清除浏览器缓存")

            HomePage(driver).load(host)

            # 遍历 cookies 字典并添加到 WebDriver 中
            login_cookies = login_api[0]
            for name, value in login_cookies.items():
                """
                add_cookie() 方法是 WebDriver 的方法，用于向浏览器添加 cookie。正确的方法调用应该只有两个参数：name 和 value
                """
                driver.add_cookie({"name": name, "value": value})

            # 刷新页面
            driver.refresh()
            CommonPage(driver).click_new_icon()
            CommonPage(driver).click_create_project_button()
            CreateProjectPage(driver).new_project(**case)

            # 断言
            project_full_name = f"{login_api[1]['login']}/{case['identifier']}"
            project_url = f"{host}{project_full_name}"
            logger.info(f"断言--> 浏览器地址是否一致----预期：{project_url} 实际：{driver.current_url}")
            allure_step(step_title=f"断言--> 浏览器地址是否一致----预期：{project_url} 实际：{driver.current_url}")
            assert project_url == driver.current_url
            result = ProjectDetailPage(driver).get_project_private_tag()
            allure_step(step_title=f"断言--> 是否存在 私有 标签 预期： {case.get('private')}  实际：{result}")
            assert case.get('private') == result
            logger.debug(f"{case['title']}:测试通过！")

            # 删除测试项目数据
            ProjectDetailPage(driver).delete_project()
            assert ProjectDetailPage(driver).get_delete_project_success_text()
            logger.debug(
                "\n------------------------------------------END-用例执行结束------------------------------------------\n")

    @allure.story(export_project_success["allure_story"])
    @pytest.mark.parametrize("case", export_project_success["cases"],
                             ids=["{}".format(case["title"]) for case in export_project_success["cases"]])
    def test_export_project(self, init_drivers, case, request):
        """
        1. 用户导入仓库
        2. 由于导入仓库，受网络影响比较大，因此不做删除项目操作
        """
        logger.debug("\n-----------------------------START-开始执行用例-----------------------------\n")
        # 处理用例数据
        case = eval_data_process(data_handle(obj=case, source=GLOBAL_VARS))
        logger.debug(f"当前执行的用例数据:{case}, {type(case)}")

        # 处理URL
        host = GLOBAL_VARS.get("host", "")

        # 添加用例标题作为allure中显示的用例标题
        allure_title(case.get("title", ""))
        for driver in init_drivers:
            allure_step(step_title=f"当前运行的浏览器驱动是：{driver}")
            logger.debug(f"当前运行的浏览器驱动是：{driver}")

            driver.delete_all_cookies()
            allure_step(step_title="清除浏览器缓存")

            HomePage(driver).load(host)

            # 遍历 cookies 字典并添加到 WebDriver 中
            login_info = request.getfixturevalue("login_api")
            login_cookies = login_info[0]
            for name, value in login_cookies.items():
                """
                add_cookie() 方法是 WebDriver 的方法，用于向浏览器添加 cookie。正确的方法调用应该只有两个参数：name 和 value
                """
                driver.add_cookie({"name": name, "value": value})

            # 刷新页面
            driver.refresh()
            CommonPage(driver).click_new_icon()
            CommonPage(driver).click_export_project_button()
            CreateProjectPage(driver).export_project(**case)

            # 断言
            project_full_name = f"{login_info[1]['login']}/{case['identifier']}"
            project_url = f"{host}{project_full_name}"
            GLOBAL_VARS["project_url"] = project_url
            logger.info(f"断言--> 浏览器地址是否一致----预期：{project_url} 实际：{driver.current_url}")
            allure_step(step_title=f"断言--> 浏览器地址是否一致----预期：{project_url} 实际：{driver.current_url}")
            assert project_url == driver.current_url
            time.sleep(5)
            result = ProjectDetailPage(driver).get_project_private_tag()
            allure_step(step_title=f"断言--> 是否存在 私有 标签 预期： {case.get('private')}  实际：{result}")
            assert case.get('private') == result
            logger.debug(f"{case['title']}:测试通过！")
            logger.debug(
                "\n------------------------------------------END-用例执行结束------------------------------------------\n")

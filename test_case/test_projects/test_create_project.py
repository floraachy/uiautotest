# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 14:39
# @Author  : chenyinhua
# @File    : test_new_project.py
# @Software: PyCharm
# @Desc:
# 标准库导入
# 第三方库导入
import pytest
import allure
from loguru import logger
# 本地应用/模块导入
from config.global_vars import GLOBAL_VARS
from page.common_page import CommonPage
from page.projects.create_project_page import CreateProjectPage
from data.create_project_data import *
from case_utils.data_handle import data_handle, eval_data_process
from case_utils.allure_handle import allure_title, allure_step


@allure.epic(case_common["allure_epic"])
@allure.feature(case_common["allure_feature"])
class TestNewProject:
    """新建项目的测试用例"""

    @allure.story(new_project_success["allure_story"])
    @pytest.mark.parametrize("case", new_project_success["cases"],
                             ids=["{}".format(case["title"]) for case in new_project_success["cases"]])
    def test_new_project(self, init_drivers, case):
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

            CommonPage(driver).click_new_icon()
            CommonPage(driver).click_create_project_button()
            CreateProjectPage(driver).new_project(**case)

            logger.debug(f"{case['title']}:测试通过！")
            logger.debug(
                "\n------------------------------------------用例执行结束------------------------------------------\n")

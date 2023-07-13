# -*- coding: utf-8 -*-
# @Version: Python 3.9
# @Time    : 2023/1/9 16:41
# @Author  : chenyinhua
# @File    : test_demo.py
# @Software: PyCharm
# @Desc: python脚本编写的测试用例文件

# # 标准库导入
import time
# 第三方库导入
import pytest
import allure
from loguru import logger
# 本地应用/模块导入
from config.global_vars import GLOBAL_VARS
from page.home_page import HomePage
from page.login_page import LoginPop, LoginPage
from page.projects_page import ProjectsPage
from data.login_data import *
from case_utils.data_handle import data_handle, eval_data_process
from case_utils.allure_handle import allure_title, allure_step


@allure.epic(case_common["allure_epic"])
@allure.feature(case_common["allure_feature"])
class TestLogin:
    """
    登录示例
    """

    @allure.story(login_pop_success["allure_story"])
    @pytest.mark.parametrize("case", login_pop_success["cases"],
                             ids=["{}".format(case["title"]) for case in login_pop_success["cases"]])
    def test_login_pop(self, case, init_drivers):
        """
        名称：正确用户名和密码登录成功 （弹窗登录）
        步骤：
        1. 打开浏览器，访问项目首页
        2. 点击登录，进入弹窗登录页面
        3. 输入用户名和密码
        4. 点击登录按钮
        断言：出现用户昵称以及浏览器地址正确
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

            full_url = ProjectsPage(driver).load(host)
            allure_step(step_title=f"访问：{full_url}")
            time.sleep(5)

            HomePage(driver).click_login_button()
            allure_step(step_title=f"游客状态下 点击 右上角 登录 按钮")

            LoginPop(driver).input_login_info(case["user"], case["password"])
            allure_step(step_title=f"输入--> 用户名: {case['user']}  密码：{case['password']}")

            LoginPop(driver).submit_login()
            allure_step(step_title=f"点击登录按钮，提交登录表单")

            # 断言
            expected_url = full_url
            logger.debug(f"断言--> 浏览器地址是否一致----预期：{expected_url} 实际：{driver.current_url}")
            assert expected_url == driver.current_url
            allure_step(step_title=f"断言--> 浏览器地址是否一致----预期：{expected_url} 实际：{driver.current_url}")

            # 通过定位获取登录后用户的login
            actual_user_login = ProjectsPage(driver).get_avatar().split("/")[-1]
            logger.debug(f"断言--> 用户名是否一致----预期：{case['user']} 实际：{actual_user_login}")
            assert case["user"] == actual_user_login.replace("/", "")
            allure_step(step_title=f"断言--> 用户名是否一致----预期：{case['user']} 实际：{actual_user_login}")

            logger.debug(f"{case['title']}:测试通过！")
            logger.debug(
                "\n------------------------------------------用例执行结束------------------------------------------\n")

    @allure.story(login_page_success["allure_story"])
    @pytest.mark.parametrize("case", login_page_success["cases"],
                             ids=["{}".format(case["title"]) for case in login_page_success["cases"]])
    def test_login_page(self, case, init_drivers):
        """
        名称：正确用户名和密码登录成功 （网页登录）
        步骤：
        1. 打开浏览器，访问GitLink首页
        2. 进入登录页面
        3. 输入用户名和密码
        4. 点击登录按钮
        断言：出现用户昵称以及浏览器地址正确
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

            full_url = HomePage(driver).load(host)
            allure_step(step_title=f"访问：{full_url}")
            time.sleep(5)

            HomePage(driver).click_login_button()
            allure_step(step_title=f"游客状态下 点击 右上角 登录 按钮")

            LoginPage(driver).input_login_info(case["user"], case["password"])
            allure_step(step_title=f"输入--> 用户名: {case['user']}  密码：{case['password']}")

            LoginPage(driver).submit_login()
            allure_step(step_title=f"点击登录按钮，提交登录表单")

            # 断言
            expected_url = f"{host}{case['user']}"
            logger.debug(f"断言--> 浏览器地址是否一致----预期：{expected_url} 实际：{driver.current_url}")
            assert expected_url == driver.current_url
            allure_step(step_title=f"断言--> 浏览器地址是否一致----预期：{expected_url} 实际：{driver.current_url}")

            # 通过定位获取登录后用户的login
            actual_user_login = ProjectsPage(driver).get_avatar().split("/")[-1]
            logger.debug(f"断言--> 用户名是否一致----预期：{case['user']} 实际：{actual_user_login}")
            assert case["user"] == actual_user_login.replace("/", "")
            allure_step(step_title=f"断言--> 用户名是否一致----预期：{case['user']} 实际：{actual_user_login}")

            logger.debug(f"{case['title']}:测试通过！")
            logger.debug("\n------------------------------------------用例执行结束------------------------------------------\n")

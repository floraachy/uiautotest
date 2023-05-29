# -*- coding: utf-8 -*-
# @Version: Python 3.9
# @Time    : 2023/1/9 16:41
# @Author  : chenyinhua
# @File    : test_demo.py
# @Software: PyCharm
# @Desc: python脚本编写的测试用例文件
import time

import pytest
from config.global_vars import GLOBAL_VARS
from loguru import logger
from page.login_page import LoginPop
from page.projects_page import ProjectsPage
from data.login_demo_data import cases_data
from common_utils.data_handle import data_replace, eval_data_process
from case_utils.allure_handle import allure_title
import allure


@allure.feature("登录模块")
@pytest.mark.usefixtures("init_driver")
class TestLoginDemo:
    """
    登录示例
    """

    @allure.story("弹窗登录")
    @pytest.mark.parametrize("case_data", cases_data)
    def test_login_pop_success(self, init_driver, case_data):
        """
        名称：正确用户名和密码登录成功 （弹窗登录）
        步骤：
        1. 打开浏览器
        2. 进入弹窗登录页面
        3. 输入用户名和密码
        4. 点击登录按钮
        断言：出现用户昵称以及浏览器地址正确
        """
        logger.info("-----------------------------START-开始执行用例-----------------------------")

        # 处理用例数据
        case = eval_data_process(data_replace(content=case_data, source=GLOBAL_VARS))
        logger.debug(f"当前执行的用例数据:{case}, {type(case)}")

        # 处理URL
        host = GLOBAL_VARS.get("host", "")

        # 处理用例标题
        GLOBAL_VARS["title"] = case["title"]

        # 添加用例标题作为allure中显示的用例标题
        allure_title(case.get("title", ""))

        # 如果用例数据run=false则跳过该条用例不执行
        if case["run"]:
            for driver in init_driver:
                logger.info(f"当前运行的浏览器驱动是：{driver}")
                # 访问开源项目首页
                full_url = LoginPop(driver).load(host)
                time.sleep(5)
                # 进行登录操作
                LoginPop(driver).login(case["user"], case["password"])

                # 断言
                try:
                    logger.info(f"断言浏览器地址是否一致----预期：{full_url} 实际：{driver.current_url}")
                    assert full_url == driver.current_url
                    # 通过定位获取登录后用户的login
                    actual_user_login = ProjectsPage(driver).get_avatar().split("/")[-1]
                    logger.info(f"断言用户名是否一致----预期：{case['user']} 实际：{actual_user_login}")
                    assert case["user"] == actual_user_login.replace("/", "")
                    logger.info(f"{case['title']}:测试通过！")
                except Exception as e:
                    logger.error(f"断言时遇到了异常：{e}")
                    logger.info(f"{case['title']}:测试失败！")
                    raise e
        else:
            reason = f"标记了该用例为false，不执行\n"
            logger.warning(f"{reason}")
            pytest.skip(reason)

        logger.info("------------------------------------------用例执行结束------------------------------------------\n")

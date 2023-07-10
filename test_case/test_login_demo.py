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
from data.login_demo_data import login_case_data
from common_utils.data_handle import data_replace, eval_data_process
from case_utils.allure_handle import allure_title
import allure

case_common = login_case_data["case_common"]
cases = []
for k, v in login_case_data.items():
    if k != "case_common":
        cases.append(v)

logger.debug(f'{case_common["allure_epic"]} || {case_common["allure_feature"]} || {case_common["allure_story"]}')


@allure.epic(case_common["allure_epic"])
@allure.feature(case_common["allure_feature"])
class TestLoginDemo:
    """
    登录示例
    """

    @allure.story(case_common["allure_story"])
    @pytest.mark.parametrize("case", cases, ids=["{}".format(case["title"]) for case in cases])
    def test_login_pop_success(self, case, init_drivers):
        """
        名称：正确用户名和密码登录成功 （弹窗登录）
        步骤：
        1. 打开浏览器
        2. 进入弹窗登录页面
        3. 输入用户名和密码
        4. 点击登录按钮
        断言：出现用户昵称以及浏览器地址正确
        """
        logger.info("\n-----------------------------START-开始执行用例-----------------------------\n")
        # 处理用例数据
        case = eval_data_process(data_replace(content=case, source=GLOBAL_VARS))
        logger.debug(f"当前执行的用例数据:{case}, {type(case)}")

        # 处理URL
        host = GLOBAL_VARS.get("host", "")

        # 添加用例标题作为allure中显示的用例标题
        allure_title(case.get("title", ""))

        # 如果用例数据run=false则跳过该条用例不执行
        for driver in init_drivers:
            logger.info(f"当前运行的浏览器驱动是：{driver}")
            # 访问开源项目首页
            full_url = LoginPop(driver).load(host)
            time.sleep(5)
            # 进行登录操作
            LoginPop(driver).login(case["user"], case["password"])

            # 断言
            logger.info(f"断言浏览器地址是否一致----预期：{full_url} 实际：{driver.current_url}")
            assert full_url == driver.current_url
            # 通过定位获取登录后用户的login
            actual_user_login = ProjectsPage(driver).get_avatar().split("/")[-1]
            logger.info(f"断言用户名是否一致----预期：{case['user']} 实际：{actual_user_login}")
            assert case["user"] == actual_user_login.replace("/", "")
            logger.info(f"{case['title']}:测试通过！")
        logger.info("\n------------------------------------------用例执行结束------------------------------------------\n")

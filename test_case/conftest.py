# -*- coding: utf-8 -*-
# @Time    : 2023/3/17 18:33
# @Author  : Flora.Chen
# @File    : conftest.py
# @Software: PyCharm
# @Desc:

# 标准库导入
# 第三方库导入
import pytest
import allure
from loguru import logger
# 本地应用/模块导入
from config.settings import RunConfig
from case_utils.get_driver import GetDriver


@pytest.fixture(scope="function", autouse=True)
def case_skip(request):
    """处理跳过用例"""
    # 使用 request.getfixturevalue() 方法来获取测试用例函数的参数值
    # 注意这里的"case"需要与@pytest.mark.parametrize("case", cases)中传递的保持一致
    case = request.getfixturevalue("case")
    if case.get("run") is None or case.get("run") is False:
        reason = f"{case.get('title')}: 标记了该用例为false，不执行\\n"
        logger.warning(f"{reason}")
        pytest.skip(reason)


def pytest_collection_modifyitems(config, items):
    for item in items:
        # 注意这里的"case"需要与@pytest.mark.parametrize("case", cases)中传递的保持一致
        parameters = item.callspec.params["case"]
        # print(f"测试参数：{type(parameters)}     {parameters}")
        if parameters and parameters.get("severity"):
            if parameters["severity"].upper() == "TRIVIAL":
                item.add_marker(allure.severity(allure.severity_level.TRIVIAL))
            elif parameters["severity"].upper() == "MINOR":
                item.add_marker(allure.severity(allure.severity_level.MINOR))
            elif parameters["severity"].upper() == "CRITICAL":
                item.add_marker(allure.severity(allure.severity_level.CRITICAL))
            elif parameters["severity"].upper() == "BLOCKER":
                item.add_marker(allure.severity(allure.severity_level.BLOCKER))
            else:
                item.add_marker(allure.severity(allure.severity_level.NORMAL))
        else:
            item.add_marker(allure.severity(allure.severity_level.NORMAL))


# ------------------------------------- START: 配置浏览器驱动 ---------------------------------------#
@pytest.fixture(scope="session")
def init_drivers():
    # logger.debug(f"此时的driver类型:{RunConfig.driver_type}")
    drivers = GetDriver(drivers_type=RunConfig.driver_type).get_driver()
    RunConfig.drivers = drivers
    yield drivers
    for driver in drivers:
        driver.close()
        driver.quit()
# ------------------------------------- END: 配置浏览器驱动 ---------------------------------------#

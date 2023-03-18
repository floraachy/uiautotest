# -*- coding: utf-8 -*-
# @Time    : 2023/3/17 18:33
# @Author  : Flora.Chen
# @File    : conftest.py
# @Software: PyCharm
# @Desc:

import pytest
from config.settings import drivers_type
from case_utils.get_driver import GetDriver
from loguru import logger


# ------------------------------------- START: 配置浏览器驱动 ---------------------------------------#
@pytest.fixture()
def init_driver():
    drivers = GetDriver(drivers_type).get_driver()
    yield drivers
    for driver in drivers:
        driver.close()
        driver.quit()
# ------------------------------------- END: 配置浏览器驱动 ---------------------------------------#

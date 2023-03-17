# -*- coding: utf-8 -*-
# @Time    : 2023/3/17 18:33
# @Author  : Flora.Chen
# @File    : conftest.py
# @Software: PyCharm
# @Desc:

from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from loguru import logger
from config.settings import driver_type
from selenium import webdriver
# selenium 3
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# selenium 4
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


# ------------------------------------- START: 启动浏览器驱动 ---------------------------------------#
def get_driver():
    """
    获取浏览器驱动
    :return:
    """
    global driver
    try:
        logger.debug(f"运行的浏览器：{driver_type}")
        if driver_type.lower() == "chrome":
            # 本地chrome浏览器
            # selenium 3的写法
            # driver = webdriver.Chrome(ChromeDriverManager().install())
            # selenium 4的写法
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.implicitly_wait(10)
            driver.delete_all_cookies()  # 清除浏览器所有缓存

        elif driver_type.lower() == "firefox":
            # 本地firefox浏览器
            # selenium 3
            # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            # selenium 4
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            driver.maximize_window()
            driver.implicitly_wait(10)
            driver.delete_all_cookies()  # 清除浏览器所有缓存

        elif driver_type.lower() == "edge":
            # 本地firefox浏览器
            # selenium 3
            # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            # selenium 4
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            driver.maximize_window()
            driver.implicitly_wait(10)
            driver.delete_all_cookies()  # 清除浏览器所有缓存

        elif driver_type.lower() == "chrome-headless":
            # chrome headless模式
            # 参数说明，参考地址：https://github.com/GoogleChrome/chrome-launcher/blob/master/docs/chrome-flags-for-tools.md#--enable-automation
            chrome_option = CH_Options()
            chrome_option.add_argument("--headless")
            chrome_option.add_argument("--no-sandbox")  # 注意：linux运行必须要有这个
            chrome_option.add_argument("--window-size=1920x1080")
            # 本地chrome浏览器
            # selenium 3的写法
            # driver = webdriver.Chrome(ChromeDriverManager().install())
            # selenium 4的写法
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option)
            driver.implicitly_wait(10)
            driver.delete_all_cookies()  # 清除浏览器所有缓存

        elif driver_type.lower() == "firefox-headless":
            # firefox headless模式
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--disable-gpu")
            # selenium 3
            # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            # selenium 4
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
            driver.implicitly_wait(10)
            driver.delete_all_cookies()  # 清除浏览器所有缓存

        else:
            logger.error("driver驱动类型定义错误！")
            raise NameError("driver驱动类型定义错误！")
    except Exception as e:
        logger.error(f"初始化dirver的异常，请检查以下几点：1. driver_path的路径是否配置正确 2. driver版本是否与浏览器兼容：{e}")
        raise NameError(f"driver异常，请检查以下几点：1. driver_path的路径是否配置正确 2. driver版本是否与浏览器兼容 {e}")

    return driver


@pytest.fixture()
def init_driver():
    _driver = get_driver()
    yield _driver
    _driver.close()
    _driver.quit()

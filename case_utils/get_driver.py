# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 17:52
# @Author  : Flora.Chen
# @File    : get_driver.py
# @Software: PyCharm
# @Desc:

from selenium.webdriver.chrome.options import Options as CH_Options
from loguru import logger
from selenium import webdriver
# selenium 3
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# selenium 4
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


class GetDriver:
    """
    根据driver_type，自动安装下载浏览器驱动，并返回driver
    :return:driver
    """

    def __init__(self, drivers_type: str):
        # 判断drivers_type是不是列表
        if isinstance(drivers_type, list):
            # 判断drivers_type的浏览器类型是否符合指定类型，不符合则从列表中移除
            for index in reversed(range(len(drivers_type))):
                if drivers_type[index] not in ["chrome", "chrome-headless", "firefox", "firefox-headless", "edge"]:
                    logger.error(
                        f"不支持该浏览器类型：{drivers_type[index]}")
                    # 根据索引移除不支持的浏览器类型
                    drivers_type.pop(index)
            # 判断drivers_type是否为空，为空则报错
            if drivers_type:
                self.drivers_type = drivers_type
            else:
                logger.error("没有支持的浏览器驱动")
                raise NameError("没有支持的浏览器驱动")
        else:
            logger.error(f"drivers_type必须是list类型")
            raise NameError(f"drivers_type必须是list类型")

    def get_driver(self):
        """
        根据driver_type初始化不同的浏览器驱动
        """

        drivers = []

        for driver_type in self.drivers_type:
            driver_type = driver_type.lower()
            if driver_type == "chrome":
                drivers.append(self.chrome_driver())

            if driver_type == "chrome-headless":
                drivers.append(self.chrome_headless_driver())

            if driver_type == "firefox":
                drivers.append(self.firefox_driver())

            if driver_type == "firefox-headless":
                drivers.append(self.firefox_headless_driver())

            if driver_type == "edge":
                drivers.append(self.edge_driver())
        return drivers

    def chrome_driver(self):
        # chrome浏览器
        # selenium 3的写法
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # selenium 4的写法
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()  # 清除浏览器所有缓存
        return driver

    def chrome_headless_driver(self):
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
        return driver

    def firefox_driver(self):
        # firefox浏览器
        # selenium 3
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # selenium 4
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()  # 清除浏览器所有缓存
        return driver

    def firefox_headless_driver(self):
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
        return driver

    def edge_driver(self):
        # Edge浏览器
        # selenium 3
        # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        # selenium 4
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()  # 清除浏览器所有缓存
        return driver

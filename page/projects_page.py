# -*- coding: utf-8 -*-
# @Time    : 2021/12/19 15:36
# @Author  : Administrator
# @File    : project_home_page.py
# @Software: PyCharm
# @Desc: 项目首页

from loguru import logger
import time
from case_utils.basepage import BasePage
from selenium.webdriver.common.by import By
from case_utils.url_handle import url_handle

# ------------------------------ 元素定位 ---------------------------------------#
# 右上角的用户登录后的头像
avatar = (By.XPATH, "//a[@class='ant-dropdown-trigger']")


# ------------------------------ 操作 ---------------------------------------#
class ProjectsPage(BasePage):
    """项目首页"""

    def __init__(self, driver, host):
        """
        host: 项目首页地址
        driver：浏览器驱动
        """
        self.full_url = url_handle(host, "/explore")
        self.driver = driver

    def load(self):
        self.visit(self.full_url)
        logger.info(f"访问项目首页：:{self.full_url}")
        return self

    def get_avatar(self):
        """获取用户头像"""
        return self.get_element_attribute(avatar, "href")

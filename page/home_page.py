# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 17:24
# @Author  : chenyinhua
# @File    : home_page.py
# @Software: PyCharm
# @Desc:


# 第三方库导入
from selenium.webdriver.common.by import By
# 本地应用/模块导入
from case_utils.url_handle import url_handle
from case_utils.basepage import BasePage


# ------------------------------ 元素定位 ---------------------------------------#
# 游客状态下的 登录按钮
login_button = (By.XPATH, "//a[text()='登录']")


# ------------------------------ 首页各项 操作 ---------------------------------------#
class HomePage(BasePage):
    """
    GitLink首页
    """

    def load(self, host):
        """访问首页"""
        full_url = host
        self.visit(full_url)
        return full_url

    def click_login_button(self):
        """
        游客状态下 点击 右上角 “登录”按钮
        """
        self.wait_element_clickable(login_button).click()


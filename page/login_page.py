# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 10:15
# @Author  : Flora.Chen
# @File    : login_page.py
# @Software: PyCharm
# @Desc: 登录页面的元素定位 和 操作

from loguru import logger
import time
from case_utils.basepage import BasePage
from selenium.webdriver.common.by import By
from case_utils.url_handle import url_handle

# 导航栏 登录按钮
login_button = (By.XPATH, "//a[text()='登录']")

# ------------------------------ 登录弹窗元素定位 ---------------------------------------#
# 弹框中的用户名输入框
username_inputbox = (By.XPATH, "//input[@name='username']")
# 弹框中的密码输入框
password_inputbox = (By.XPATH, "//input[@name='password']")
# 弹框中的登录按钮
login_button_on_pop = (By.XPATH, "//div[text()='登录']")
# 弹框的错误提示信息
error_pop = (By.XPATH, "//div[@class='ant-notification-notice-description']")

# ------------------------------ 登录页面元素定位 ---------------------------------------#
# 用户名输入框
login_username = (By.ID, "login_username")
# 密码输入框
login_password = (By.ID, "login_password")
# 登录按钮
login_button_on_page = (By.XPATH, "//span[text()='登 录']/..")
# 下次自动登录
auto_login = (By.XPATH, "//span[contains(text(), '下次自动登录')]")
# 忘记密码
forget_password_button = (By.XPATH, "//span[contains(text(), '下次自动登录')]/../")
# 去注册
go_register_button = (By.XPATH, "//a[contains(text(), '注册')]")


# ------------------------------ 登录 操作 ---------------------------------------#
class LoginPop(BasePage):
    """
    弹窗登录 (除了首页，注册，找回密码页面，其他都是弹窗登录)
    """

    def __init__(self, driver, host):
        """
        host: 环境域名
        driver：浏览器驱动
        """
        self.full_url = url_handle(host, "/explore")
        self.driver = driver

    def load(self):
        """访问项目首页"""
        self.visit(self.full_url)
        logger.info(f"访问项目首页成功：{self.full_url}")
        return self

    def input_login_info(self, username, password):
        """
        弹窗登录操作-输入登录信息
        步骤：
        1. 点击导航栏的登录按钮
        2. 输入用户名
        3. 输入密码
        """
        self.wait_element_clickable(login_button).click()
        self.wait_element_visibility(username_inputbox).send_keys(username)
        self.wait_element_visibility(password_inputbox).send_keys(password)
        time.sleep(5)
        return self

    def login(self, username, password):
        """
        弹窗登录操作
        步骤：
        1. 点击导航栏的登录按钮
        2. 输入用户名
        3. 输入密码
        4. 点击登录按钮
        """
        self.wait_element_clickable(login_button).click()
        self.wait_element_visibility(username_inputbox).send_keys(username)
        self.wait_element_visibility(password_inputbox).send_keys(password)
        time.sleep(5)
        self.wait_element_visibility(login_button_on_pop).click()
        time.sleep(5)
        return self

    def error_pop(self):
        """弹框的错误提示"""
        elems = self.driver.find_elements(*error_pop)
        return [elem.text for elem in elems]

    def login_button_class(self):
        """获取弹框中登录按钮的class属性"""
        return self.get_class(login_button_on_pop)


class LoginPage(BasePage):
    """
    登录页面的一系列操作 (首页，注册，找回密码页面)
    """

    def __init__(self, driver, host):
        self.full_url = host
        self.driver = driver

    def load(self):
        """访问首页"""
        self.visit(self.full_url)
        return self

    def login(self, username, password):
        """
        登录操作
        1. 点击登录按钮
        2. 输入用户名
        3. 输入密码
        4. 勾选自动登录
        5. 点击登录按钮
        """
        # 点击登录按钮
        self.click(login_button)
        # 输入用户名
        self.input(login_username, username)
        # 输入密码
        self.input(login_password, password)
        # 勾选自动登录
        self.click(auto_login)
        # 点击登录按钮
        self.click(login_button_on_page)
        return self

    def click_go_register(self):
        """点击 去注册"""
        self.click(go_register_button)
        return self

    def click_forget_password(self):
        """点击 忘记密码"""
        self.click(forget_password_button)
        return self

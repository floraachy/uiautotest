# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 14:47
# @Author  : chenyinhua
# @File    : common_page.py
# @Software: PyCharm
# @Desc:

# 标准库导入
import time
# 第三方库导入
from selenium.webdriver.common.by import By
# 本地应用/模块导入
from case_utils.basepage import BasePage
from case_utils.allure_handle import allure_step

# ------------------------------ 元素定位 ---------------------------------------#
# 游客状态下的 登录按钮
login_button = (By.XPATH, "//a[text()='登录']")
# 用户登录状态下，右上角新建项目/导入项目/新建组织/加入项目的图标
new_project_icon = (By.XPATH, "//i[contains(@class, 'icon-sousuo')]/following-sibling::img")
# 用户登录状态下，新建项目
create_project = (By.XPATH, "//a[text()='新建项目']")
# 用户登录状态下，导入项目
export_project = (By.XPATH, "//a[text()='导入项目']")
# 用户登录状态下，新建组织
create_organization = (By.XPATH, "//a[text()='新建组织']")
# 用户登录状态下，加入项目
join_project = (By.XPATH, "//a[text()='加入项目']")


# ------------------------------ 公共模块的一些 操作 ---------------------------------------#
class CommonPage(BasePage):
    """
    公共模块的一些操作，如 导航栏，底部，公共弹窗
    """

    def click_login_button(self):
        """
        游客状态下 点击 右上角 “登录”按钮
        """
        self.wait_element_clickable(login_button).click()
        allure_step(step_title=f"游客状态下 点击 右上角 登录 按钮")

    def click_new_icon(self):
        """
        登录状态下，点击 新建 图标
        显示按钮：新建项目，导入项目，新建组织，加入项目
        """
        self.hover(new_project_icon)
        time.sleep(2)
        allure_step(step_title=f"登录状态下，点击右上角 新建 图标，显示：新建项目，导入项目，新建组织，加入项目")

    def click_create_project_button(self):
        """
        登录状态下，点击右上角 新建>新建项目 按钮
        """
        self.click(create_project)
        allure_step(step_title=f"登录状态下，点击右上角 新建>新建项目 按钮")

    def click_export_project_button(self):
        """
        登录状态下，点击右上角 新建>导入项目 按钮
        """
        self.click(export_project)
        allure_step(step_title=f"登录状态下，点击右上角 新建>导入项目 按钮")

    def click_create_org_button(self):
        """
        登录状态下，点击右上角 新建>新建组织 按钮
        """
        self.click(create_organization)
        allure_step(step_title=f"登录状态下，点击右上角 新建>导入项目 按钮")

    def click_join_project_button(self):
        """
        登录状态下，点击右上角 新建>加入项目 按钮
        """
        self.click(join_project)
        allure_step(step_title=f"登录状态下，点击右上角 新建>加入项目 按钮")

# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 15:34
# @Author  : chenyinhua
# @File    : conftest.py
# @Software: PyCharm
# @Desc:

# 标准库导入
# 第三方库导入
import pytest
import requests
from loguru import logger
# 本地应用/模块导入
from config.global_vars import GLOBAL_VARS
from common_utils.base_request import BaseRequest


@pytest.fixture(scope="module")
def login_api():
    """
    获取登录的cookie
    :return:
    """
    host = GLOBAL_VARS.get("host")
    login = GLOBAL_VARS.get('login')
    password = GLOBAL_VARS.get('password')
    # 兼容一下host后面多一个斜线的情况
    if host[-1] == "/":
        host = host[:len(host) - 1]
    req_data = {
        "url": host + "/api/accounts/login.json",
        "method": "POST",
        "request_type": "json",
        "headers": {"Content-Type": "application/json; charset=utf-8;"},
        "payload": {"login": login, "password": password, "autologin": 1}
    }
    # 请求登录接口
    try:
        res = BaseRequest.send_request(req_data=req_data)
        res.raise_for_status()
        # 将cookies转成字典
        cookies = requests.utils.dict_from_cookiejar(res.cookies)
        logger.debug(f"获取用户：{login}登录的cookies成功：{type(cookies)} || {cookies}")
        yield cookies, res.json()
    except Exception as e:
        GLOBAL_VARS["login_cookie"] = None
        logger.error(f"获取用户：{login}登录的cookies失败：{e}")


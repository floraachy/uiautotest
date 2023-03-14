# -*- coding: utf-8 -*-
# @Version: Python 3.9
# @Time    : 2023/1/9 16:41
# @Author  : chenyinhua
# @File    : url_handle.py
# @Software: PyCharm
# @Desc: 根据配置文件中的域名，以及测试用例数据中的url处理访问url

from loguru import logger


def url_handle(host, url):
    """
    将host以及url拼接组成full_url
    """
    if url is None:
        url = ""

    # 如果url是以http开头的，则直接使用该url，不与host进行拼接
    if url.lower().startswith("http"):
        full_url = url
    else:
        # 如果host以/结尾 并且 url以/开头
        if host.endswith("/") and url.startswith("/"):
            full_url = host[0:len(host) - 1] + url
        # 如果host以/结尾 并且 url不以/开头
        elif host.endswith("/") and (not url.startswith("/")):
            full_url = host + url
        else:
            # # 如果host不以/结尾 或者 url不以/开头，则将host和url拼接起来的时候增加/，组成新的url
            full_url = host + "/" + url
    logger.info("处理前的host:{}, 处理前的url: {}, 处理后的full_url：{}".format(host, url, full_url))
    return full_url

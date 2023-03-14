# -*- coding: utf-8 -*-
# @Version: Python 3.9
# @Time    : 2023/1/9 16:41
# @Author  : chenyinhua
# @File    : data_handle.py
# @Software: PyCharm
# @Desc: 处理用例数据，针对用例数据进行替换

from config.global_vars import GLOBAL_VARS
from string import Template
from loguru import logger
import re


def case_data_replace(content):
    """
    用例数据替换的方法
    :param content: 原始的字符串内容
    return content： 替换表达式后的字符串
    """
    if content is None:
        return None

    if len(content) != 0:
        logger.info(f"开始进行字符串替换: 替换字符串为：{content}")
        content = Template(str(content)).safe_substitute(GLOBAL_VARS)
        logger.debug(f"使用模板函数Template替换字符串完成。 替换后的字符串如下：{content}")
        for func in re.findall('\\${(.*?)}', content):
            try:
                content = content.replace('${%s}' % func, exec_func(func))
                logger.debug(f"通过执行函数替换用例数据值 替换字符串后为：{content}")
            except Exception as e:
                logger.exception(e)
        return str_to_python(content)


def exec_func(func) -> str:
    """
    :params func 字符的形式调用函数
    : return 返回的转换成函数执行的结果,已字符串格式返回
    """
    result = eval(func)
    return str(result)


# 将"[1,2,3]" 或者"{'k':'v'}" -> [1,2,3], {'k':'v'}
def str_to_python(content) -> object:
    """
    将字符串包裹的表达式摘出来
    """
    if content is None:
        return None

    try:
        return eval(content)
    except:
        return content

# -*- coding: utf-8 -*-
# @Version: Python 3.9
# @Time    : 2023/1/9 17:09
# @Author  : chenyinhua
# @File    : run.py
# @Software: PyCharm
# @Desc: 框架主入口
"""
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python run.py  (默认在test环境运行测试用例)
  > python run.py -env live 在live环境运行测试用例
  > python run.py -env=test 在test环境运行测试用例
"""

import os
import pytest
from common_utils.loguru_handle import error_only
from loguru import logger
import click
from config.project_path import LOG_DIR, REPORT_DIR, CONF_DIR
from config.settings import REPORT_NAME


@click.command()
@click.option("-env", default=None, help="输入运行环境：test 或 live")
def run(env):
    # 捕获所有日志
    logger.add(os.path.join(LOG_DIR, "runtime_{time}_all.log"), enqueue=True, encoding="utf-8", rotation="00:00",
               format="{time:YYYY-MM-DD HH:mm:ss} {level} From {module}.{function} : {message}")
    # 仅捕获错误日志
    logger.add(os.path.join(LOG_DIR, "runtime_{time}_error.log"), enqueue=True, encoding="utf-8", rotation="00:00",
               filter=error_only, format="{time:YYYY-MM-DD HH:mm:ss} {level} From {module}.{function} : {message}")
    logger.info("""
                     _    _         _      _____         _
      __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
     / _` | "_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
    | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
     \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
          |_|
          Starting      ...     ...     ...
        """)
    # 执行用例
    report_name = os.path.join(REPORT_DIR, REPORT_NAME)
    report_css = os.path.join(CONF_DIR, "report.css")
    arg_list = [f'--html={report_name}', f"--css={report_css}"]
    if env == "live":
        arg_list.append("--env=live")
    pytest.main(args=arg_list)


if __name__ == '__main__':
    run()

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
  > python run.py  (默认在test环境运行测试用例, 报告采用allure)
  > python run.py -m demo 在test环境仅运行打了标记demo用例， 默认报告采用allure
  > python run.py -env live 在live环境运行测试用例
  > python run.py -env=test 在test环境运行测试用例
  > python run.py -report=pytest-html (默认在test环境运行测试用例, 报告采用pytest-html)

pytest相关参数：以下也可通过pytest.ini配置
     --reruns: 失败重跑次数
     --reruns-delay 失败重跑间隔时间
     --count: 重复执行次数
    -v: 显示错误位置以及错误的详细信息
    -s: 等价于 pytest --capture=no 可以捕获print函数的输出
    -q: 简化输出信息
    -m: 运行指定标签的测试用例
    -x: 一旦错误，则停止运行
    --cache-clear 清除pytest的缓存，包括测试结果缓存、抓取的fixture实例缓存和收集器信息缓存等
    --maxfail: 设置最大失败次数，当超出这个阈值时，则不会在执行测试用例
    "--reruns=3", "--reruns-delay=2"

 allure相关参数：
    –-alluredir这个选项用于指定存储测试结果的路径
"""
# 标准库导入
import os
import argparse
# 第三方库导入
import pytest
from loguru import logger
# 本地应用/模块导入
from config.settings import LOG_LEVEL
from config.global_vars import GLOBAL_VARS, ENV_VARS
from config.path_config import REPORT_DIR, LOG_DIR, CONF_DIR, LIB_DIR, ALLURE_RESULTS_DIR, \
    ALLURE_HTML_DIR
from case_utils.platform_handle import PlatformHandle
from case_utils.send_result_handle import send_result
from case_utils.allure_handle import AllureReportBeautiful
from common_utils.files_handle import zip_file, copy_file


def capture_logs(level=LOG_LEVEL):
    logger.info("""
                        _    _         _      _____         _
         __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
        / _` | "_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
       | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
        \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
             |_|
             Starting      ...     ...     ...
           """)
    if level:
        # 仅捕获指定级别日志
        logger.add(
            os.path.join(LOG_DIR, "runtime_{time}.log"),
            enqueue=True,
            encoding="utf-8",
            rotation="00:00",
            level=LOG_LEVEL.upper(),
            format="{time:YYYY-MM-DD HH:mm:ss} {level} From {module}.{function} : {message}",
        )
    else:
        # 捕获所有日志
        logger.add(
            os.path.join(LOG_DIR, "runtime_{time}_all.log"),
            enqueue=True,
            encoding="utf-8",
            rotation="00:00",
            format="{time:YYYY-MM-DD HH:mm:ss} {level} From {module}.{function} : {message}",
        )


def generate_allure_report():
    """
    通过allure生成html测试报告，并对报告进行美化
    """
    # ----------------START: 判断运行的平台，是linux还是windows，执行不同的allure命令----------------
    plat = PlatformHandle()
    allure_path = os.path.join(LIB_DIR, [i for i in os.listdir(LIB_DIR) if i.startswith("allure")][0], "bin")
    cmd = plat.allure[1].format(os.path.join(allure_path, plat.allure[0]), ALLURE_RESULTS_DIR, ALLURE_HTML_DIR)
    os.popen(cmd).read()
    # ----------------END: 判断运行的平台，是linux还是windows，执行不同的allure命令 ----------------
    # ----------------START: 美化allure测试报告 ------------------------------------------
    # 设置打开的 Allure 报告的浏览器窗口标题文案
    AllureReportBeautiful(allure_html_path=ALLURE_HTML_DIR).set_windows_title(
        new_title=ENV_VARS["common"]["project_name"])
    # 修改Allure报告Overview的标题文案
    AllureReportBeautiful(allure_html_path=ALLURE_HTML_DIR).set_report_name(
        new_name=ENV_VARS["common"]["report_title"])
    # 在allure-html报告中往widgets/environment.json中写入环境信息
    env_info = ENV_VARS["common"]
    env_info["run_env"] = GLOBAL_VARS.get("host", None)
    AllureReportBeautiful(allure_html_path=ALLURE_HTML_DIR).set_report_env_on_html(
        env_info=env_info)
    # ----------------END: 美化allure测试报告 ------------------------------------------
    # ----------------START: 压缩allure测试报告，方便后续发送压缩包------------------------------------------
    # 复制http_server.exe以及双击打开Allure报告.bat，以便windows环境下，直接打开查看allure html报告
    allure_config_path = os.path.join(CONF_DIR, "allure_config")
    copy_file(src_file_path=os.path.join(allure_config_path,
                                         [i for i in os.listdir(allure_config_path) if i.endswith(".exe")][0]),
              dest_dir_path=ALLURE_HTML_DIR)
    copy_file(src_file_path=os.path.join(allure_config_path,
                                         [i for i in os.listdir(allure_config_path) if i.endswith(".bat")][0]),
              dest_dir_path=ALLURE_HTML_DIR)

    attachment_path = os.path.join(REPORT_DIR, f'autotest_report.zip')
    zip_file(in_path=ALLURE_HTML_DIR, out_path=attachment_path)
    # ----------------END: 压缩allure测试报告，方便后续发送压缩包------------------------------------------
    return ALLURE_HTML_DIR, attachment_path


def run(env, m, report):
    try:
        # ------------------------ 捕获日志----------------------------
        capture_logs()
        # ------------------------ 设置全局变量 ------------------------
        # 根据指定的环境参数，将运行环境所需相关配置数据保存到GLOBAL_VARS
        GLOBAL_VARS["env_key"] = env.lower()
        if ENV_VARS.get(env.lower()):
            GLOBAL_VARS.update(ENV_VARS[env.lower()])
        # ------------------------ pytest执行测试用例 ------------------------
        arg_list = []
        if m is not None:
            arg_list.append(f"-m {m}")
        if report.lower() == "allure":
            arg_list.extend(['-q', '--cache-clear', f'--alluredir={ALLURE_RESULTS_DIR}', '--clean-alluredir'])
            pytest.main(args=arg_list)
            report_path, attachment_path = generate_allure_report()
        else:
            # 测试报告路径
            report_path = os.path.join(REPORT_DIR, "autotest_report.html")
            attachment_path = report_path
            # 优化测试报告的css路径
            pytest_html_config_path = os.path.join(CONF_DIR, "pytest_html_config")
            report_css = os.path.join(pytest_html_config_path, "pytest_html_report.css")
            # pytest运行的参数
            arg_list.extend([f'--html={report_path}', f"--css={report_css}"])
            # 使用pytest运行测试用例
            pytest.main(args=arg_list)
        # ------------------------ 发送测试结果 ------------------------
        send_result(report_path=report_path, report_type=report, attachment_path=attachment_path)
    except Exception as e:
        raise e


if __name__ == '__main__':
    # 定义命令行参数
    parser = argparse.ArgumentParser(description="框架主入口")
    parser.add_argument("-report", default="allure", help="选择需要生成的测试报告：pytest-html, allure")
    parser.add_argument("-env", default="test", help="输入运行环境：test 或 live")
    parser.add_argument("-m", default=None, help="选择需要运行的用例：python.ini配置的名称")
    args = parser.parse_args()
    run(env=args.env, m=args.m, report=args.report)

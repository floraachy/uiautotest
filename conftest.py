# -*- coding: utf-8 -*-
# @Version: Python 3.9
# @Time    : 2023/2/2 16:05
# @Author  : chenyinhua
# @File    : conftest.py
# @Software: PyCharm
# @Desc: 这是文件的描述信息


from config.global_vars import GLOBAL_VARS
from loguru import logger
import pytest
from config.settings import test, live, RunDriver, REPORT_TITLE, PROJECT_NAME, TESTER, DEPARTMENT
from py._xmlgen import html  # 安装pytest-html，版本最好是2.1.1
from time import strftime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from datetime import datetime
import os
from config.project_path import IMG_DIR


# ------------------------------------- START: 配置运行环境 ---------------------------------------#
def pytest_addoption(parser):
    """
    pytest_addoption 可以让用户注册一个自定义的命令行参数，方便用户将数据传递给 pytest；
    这个 Hook 方法一般和 内置 fixture pytestconfig 配合使用，pytest_addoption 注册命令行参数，pytestconfig 通过配置对象读取参数的值；
    :param parser:
    :return:
    """

    parser.addoption(
        # action="store" 默认，只存储参数的值，可以存储任何类型的值，此时 default 也可以是任何类型的值，而且命令行参数多次使用也只能生效一个，最后一个值覆盖之前的值；
        # action="append"，将参数值存储为一个列表，用append模式将可以在pytest命令行方式执行测试用例的同时多次向程序内部传递自定义参数对应的参数值
        "--env", action="store",
        default="test",
        choices=["test", "live"],  # choices 只允许输入的值的范围
        type=str,
        help="将命令行参数--env添加到pytest配置对象中，通过--env设置当前运行的环境host"
    )


@pytest.fixture(scope="session", autouse=True)
def get_config(request):
    """
    从配置对象中读取自定义参数的值
    """
    # 根据指定的环境，获取指定环境的域名以及用例数据文件类型
    env = request.config.getoption("--env")
    if env.lower() == "live":
        config_data = live
    else:
        config_data = test
    for item in config_data:
        for k, v in item.items():
            GLOBAL_VARS[k] = v

    logger.info(f"当前环境变量为：{GLOBAL_VARS}")


# ------------------------------------- END: 配置运行环境 ---------------------------------------#


# ------------------------------------- START: 启动浏览器驱动 ---------------------------------------#
@pytest.fixture(scope="session", autouse=True)
def init_driver():
    """
    定义浏览器驱动
    :return:
    """
    try:
        driver_type = RunDriver.driver_type
        driver_path = RunDriver.driver_path
        logger.debug(f"运行的浏览器：{driver_type}, 驱动执行路径：{driver_path}")
        if driver_type.lower() == "chrome":
            # 本地chrome浏览器
            # driver = webdriver.Chrome()  # 不指定浏览器驱动路径的写法
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.maximize_window()
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.delete_all_cookies()  # 清除浏览器所有缓存

        elif driver_type.lower() == "firefox":
            # 本地firefox浏览器
            # driver = webdriver.Firefox() # 不指定浏览器驱动路径的写法
            driver = webdriver.Firefox(executable_path=driver_path)
            driver.maximize_window()
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.delete_all_cookies()  # 清除浏览器所有缓存

        elif driver_type.lower() == "chrome-headless":
            # chrome headless模式
            # 参数说明，参考地址：https://github.com/GoogleChrome/chrome-launcher/blob/master/docs/chrome-flags-for-tools.md#--enable-automation
            chrome_option = CH_Options()
            chrome_option.add_argument("--headless")
            chrome_option.add_argument("--no-sandbox")  # 注意：linux运行必须要有这个
            chrome_option.add_argument("--window-size=1920x1080")
            # driver = webdriver.Chrome(options=chrome_option) # 不指定浏览器驱动路径的写法
            driver = webdriver.Chrome(executable_path=driver_path, options=chrome_option)
            driver.implicitly_wait(10)
            driver.delete_all_cookies()  # 清除浏览器所有缓存

        elif driver_type.lower() == "firefox-headless":
            # firefox headless模式
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--disable-gpu")
            # driver = webdriver.Firefox(options=firefox_options) # 不指定浏览器驱动路径的写法
            driver = webdriver.Firefox(options=firefox_options, executable_path=driver_path)
            driver.implicitly_wait(10)
            driver.delete_all_cookies()  # 清除浏览器所有缓存

        else:
            logger.error("driver驱动类型定义错误！")
            raise NameError("driver驱动类型定义错误！")
    except Exception as e:
        logger.error(f"初始化dirver的异常，请检查以下几点：1. driver_path的路径是否配置正确 2. driver版本是否与浏览器兼容：{e}")
        raise NameError(f"driver异常，请检查以下几点：1. driver_path的路径是否配置正确 2. driver版本是否与浏览器兼容 {e}")

    GLOBAL_VARS["driver"] = driver
    yield driver
    # 关闭浏览器
    driver.quit()


# ------------------------------------- END: 启动浏览器驱动  ---------------------------------------#


# ------------------------------------- START: 报告处理 ---------------------------------------#
def pytest_html_report_title(report):
    """
    修改报告标题
    """
    report.title = REPORT_TITLE


def pytest_configure(config):
    """
    # 在测试运行前，修改Environment部分信息，配置测试报告环境信息
    """
    # 给环境表 添加项目名称及开始时间
    config._metadata["项目名称"] = PROJECT_NAME
    config._metadata['开始时间'] = strftime('%Y-%m-%d %H:%M:%S')
    # 给环境表 移除packages 及plugins
    config._metadata.pop("Packages")
    config._metadata.pop("Plugins")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """
    在测试运行后，修改Environment部分信息
    """
    # 给环境表 添加 项目环境
    session.config._metadata['项目环境'] = GLOBAL_VARS.get("host", "")


def pytest_html_results_summary(prefix, summary, postfix):
    """
    修改Summary部分的信息
    """
    prefix.extend([html.p(TESTER)])
    prefix.extend([html.p(DEPARTMENT)])


def pytest_html_results_table_header(cells):
    """
    修改结果表的表头
    """
    # 往表格中增加一列"用例描述"，并且给"用例描述"增加排序
    cells.insert(2, html.th('用例描述', class_="sortable", col="name"))
    # 往表格中增加一列"执行时间"，并且给"执行时间"增加排序
    cells.insert(3, html.th('执行时间', class_="sortable time", col="time"))
    # 移除表格最后一列
    cells.pop()


def pytest_html_results_table_row(report, cells):
    """
    修改结果表的表头后给对应的行增加值
    """
    # 往列"用例描述"插入每行的值
    cells.insert(2, html.td(report.description))
    # 往列"执行时间"插入每行的值
    cells.insert(3, html.td(strftime("%Y-%m-%d %H:%M:%S"), class_="col-time"))
    # 移除表格最后一列
    cells.pop()


def pytest_html_results_table_html(report, data):
    """如果测试通过，则显示这条用例通过啦！"""
    if report.passed:
        del data[:]
        data.append(html.div("这条用例通过啦！", class_="empty log"))


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
    1. 测试方法的文档注释作为结果表的Description的值
    2. 测试用例失败进行截图操作，并将截图追加到测试报告中
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    # 获取调用结果的测试报告，返回一个report对象
    # report对象的属性包括when（steup, call, teardown三个值）、nodeid(测试用例的名字)、outcome(用例的执行结果，passed,failed)
    report = outcome.get_result()
    report.description = ""
    extra = getattr(report, "extra", [])
    if report.when == "call" or report.when == "setup":
        # 将获取到的用例数据的title作为结果表的Description的值
        report.description = GLOBAL_VARS.get("title", "")
        # 报错截图添加到报告
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 定义截图的文件名
            file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
            # 进行截图操作
            GLOBAL_VARS.get("driver").save_screenshot(os.path.join(IMG_DIR, file_name))
            # 如果存在截图，就将截图以html形式插入到报告中
            # 由于img里面必须写相对路径，因此需要对IMG_DIR进行处理
            if "\\" in IMG_DIR:
                image_name = IMG_DIR.split("\\")[-1]
            else:
                image_name = IMG_DIR.split("/")[-1]
            image_path = os.path.join(f"{os.path.join('..', image_name)}", file_name)
            image_path = image_path.replace("\\", "/")  # html标签中需要使用/
            html = f'<div class="image"><img src="{image_path}" onclick="window.open(this.src)"/></div>'
            extra.append(pytest_html.extras.html(html))
        report.extra = extra
    # ------------------------------------- END: 报告处理 ---------------------------------------#

## 一、框架介绍

本框架主要是基于 Python + pytest + selenium + pytest-html/Allure + loguru  + 邮件通知/企业微信通知/钉钉通知 实现的WEB  UI自动化框架。

* git地址: [https://gitlink.org.cn/floraachy/uiautotest.git](https://gitlink.org.cn/floraachy/uiautotest.git)
* 项目参与者: floraachy
* 技术支持邮箱: 1622042529@qq.com
* 个人主页： [https://www.gitlink.org.cn/floraachy](https://www.gitlink.org.cn/floraachy)
* 测试社区地址:  [https://www.gitlink.org.cn/zone/tester](https://www.gitlink.org.cn/zone/tester)
* 入群二维码：[https://www.gitlink.org.cn/floraachy/apiautotest/issues/1](https://www.gitlink.org.cn/floraachy/apiautotest/issues/1)

对于框架任何问题，欢迎联系我！


## 二、实现功能
- 基于PO设计模式结合，该平台可实现测试用例的自动化执行及自动化测试报告的生成同时包括自动化测试执行时，用例失败的截图操作。
- 使用webdriver_manager自动下载webdriver，告别手动下载，再也不用担心webdriver版本问题了。
- 支持通过命令行指定一个或者多个浏览器，多个浏览器可同时运行。
- 支持通过命令行指定运行环境，实现环境一键切换，解决多环境相互影响问题
- 采用loguru管理日志，可以输出更为优雅，简洁的日志
- 钉钉、企业微信通知: 支持多种通知场景，执行成功之后，可选择发送钉钉、或者企业微信、邮箱通知
- 使用pipenv管理虚拟环境和依赖文件，可以使用`pipenv install`一键安装依赖包。
- 多种报告随心选择：框架支持pytest-html以及Allure测试报告，可以动态配置所需报告。
- 支持利用allure设置用例优先级，运行指定优先级的用例。



## 三、目录结构
```
├────case_utils/
│    ├────__init__.py
│    ├────allure_handle.py
│    ├────basepage.py
│    ├────data_handle.py
│    ├────get_driver.py
│    ├────get_results_handle.py
│    ├────platform_handle.py
│    ├────send_result_handle.py
│    └────url_handle.py
├────common_utils/
│    ├────__init__.py
│    ├────base_request.py
│    ├────bs4_handle.py
│    ├────dingding_handle.py
│    ├────files_handle.py
│    ├────time_handle.py
│    ├────wechat_handle.py
│    ├────yagmail_handle.py
│    └────yaml_handle.py
├────config/
│    ├────__init__.py
│    ├────allure_config/
│    │    ├────http_server.exe
│    │    ├────logo.svg
│    │    └────双击打开Allure报告.bat
│    ├────global_vars.py
│    ├────models.py
│    ├────path_config.py
│    ├────pytest_html_config/
│    │    └────pytest_html_report.css
│    └────settings.py
├────data/
│    ├────create_project_data.py
│    └────login_data.py
├────lib/
├────outputs/
├────page/
│    ├────__init__.py
│    ├────common_page.py
│    ├────home_page.py
│    ├────login_page.py
│    └────projects/
│    │    ├────__init__.py
│    │    ├────create_project_page.py
│    │    ├────project_detail_page.py
│    │    └────projects_page.py
└────test_case/
│    ├────__init__.py
│    ├────conftest.py
│    ├────test_login.py
│    └────test_projects/
│    │    ├────__init__.py
│    │    ├────conftest.py
│    │    └────test_create_project.py
├────conftest.py
├────Pipfile
├────Pipfile.lock
├────pytest.ini
├────README.md
├────.gitignore
├────run.py
 ```   

## 四、依赖库
```
jsonpath = "==0.82"
openpyxl = "==3.0.9"
pytest = "==6.2.5"
pyyaml = "==6.0"
requests = "==2.26.0"
loguru = "*"
pytest-rerunfailures = "*"
faker = "*"
deepdiff = "*"
pymysql = "*"
yagmail = "*"
selenium = "*"
pyautogui = "*"
pywinauto = "*"
pytest-html = "==2.1.1"
allure-pytest = "*"
beautifulsoup4 = "*"
webdriver-manager = "*"
requests-toolbelt = "*"
```


## 五、安装教程

1. 通过Git工具clone代码到本地 或者 直接下载压缩包ZIP
```
git clone https://gitlink.org.cn/floraachy/uiautotest.git
```

2. 本地电脑搭建好 python环境，我使用的python版本是3.9


3. 安装pipenv
```
# 建议在项目根目录下执行命令安装
pip install pipenv
```

4. 使用pipenv管理安装环境依赖包：pipenv install （必须在项目根目录下执行）
```
   注意：使用pipenv install会自动安装Pipfile里面的依赖包，该依赖包仅安装在虚拟环境里，不安装在测试机。
```
如上环境都已经搭建好了，包括框架依赖包也都安装好了。

## 六、如何创建用例
### 1. 修改配置文件  `config.settings.py`
1）确认RunConfig的各项参数，可以调整失败重跑次数`rerun`， 失败重跑间隔时间`reruns_delay`，当达到最大失败数，停止执行`max_fail`
2）确认测试完成后是否发送测试结果，由SEND_RESULT_TYPE控制，并填充对应邮件/钉钉/企业微信配置信息
3）指定日志收集级别，由LOG_LEVEL控制


### 2. 修改全局变量，增加测试数据  `config.global_vars.py`
1) ENV_VARS["common"]是一些公共参数，如报告标题，报告名称，测试者，测试部门。后续会显示在测试报告上。如果还有其他，可自行添加
2）ENV_VARS["test"]是保存test环境的一些测试数据。ENV_VARS["live"]是保存live环境的一些测试数据。如果还有其他环境可以继续增加，例如增加ENV_VARS["dev"] = {"host": "", ......}

### 3. 删除框架中的示例用例数据
1）删除 `data`目录下所有文件
2）删除`page`目录下所有文件
3）删除 `test_case`目录下所有编写的用例

### 4. 编写测试用例
#### 1. 在`page`目录新建一个`py`文件，用于管理元素的定位以及页面操作方法

#### 2. 在 `data`目录下新建一个`py`文件，用于管理测试用例中所需的测试数据
- 测试数据中需要存在字典`case_common`，用于配置allure报告，参考如下：
```python
case_common = {
    "allure_epic": "GitLink",
    "allure_feature": "登录模块",
}
```

- 用例实际执行的数据，需要参考如下：

```python
# allure_story以及severity用于配置allure报告，建议配置
# 字典命名可以自定义
# title字段建议保留，涉及到报告上的显示
login_pop_success = {
    "allure_story": "弹窗登录",
    "cases":
        [
            {"title": "弹窗登录: 正确用户名和密码登录成功", "user": "${login}", "password": "${password}",
             "run": False,
             "severity": "critical"}
        ]
}

```

#### 3. 在 `test_case`目录编写测试用例 
- 注意：测试用例命令需要遵循`pytest`命名规则。



## 七、运行自动化测试
### 1.  激活已存在的虚拟环境
- （如果不存在会创建一个）：pipenv shell （必须在项目根目录下执行）

### 2. 运行
```
在pycharm>terminal或者电脑命令窗口，进入项目根路径，执行如下命令（如果依赖包是安装在虚拟环境中，需要先启动虚拟环境）。
  > python run.py  (默认在test环境运行测试用例, 报告采用allure)
  > python run.py -m demo 在test环境仅运行打了标记demo用例， 默认报告采用allure
  > python run.py -env live 在live环境运行测试用例
  > python run.py -env=test 在test环境运行测试用例
  > python run.py -report=pytest-html (默认在test环境运行测试用例, 报告采用pytest-html)
  > python run.py -driver chrome edge  (使用chrome以及edge浏览器运行测试用例)
```
注意：
- 如果pycharm.interpreter拥有了框架所需的所有依赖包，可以通过pycharm直接在`run.py`中右键运行

## 八 、详细功能说明
### todo 待补充

## 九、初始化项目可能遇到的问题
- [测试机安装的是python3.7，但是本框架要求3.9.5，怎么办？](https://www.gitlink.org.cn/zone/tester/newdetail/245)
- [无法安装依赖包或者安装很慢，怎么办？](https://www.gitlink.org.cn/zone/tester/newdetail/244)

## 前言

  基于Python+pytest+selenium+allure搭建的一款适用于WEB UI自动化测试的框架。
  基于PO设计模式结合，该平台可实现测试用例的自动化执行及自动化测试报告的生成同时包括自动化测试执行时，用例失败的截图操作


## 一、框架介绍

本框架主要是基于 Python + pytest + selenium + pytest-html/Allure + loguru  + 邮件通知/企业微信通知/钉钉通知 实现的UI自动化框架。

* git地址: [https://gitlink.org.cn/floraachy/uiautotest.git](https://gitlink.org.cn/floraachy/uiautotest.git)
* 项目参与者: floraachy
* 技术支持邮箱: 1622042529@qq.com
* 个人博客地址:  [https://blog.csdn.net/FloraCHY](https://blog.csdn.net/FloraCHY)

对于框架任何问题，欢迎联系我！


## 二、实现功能
### todo 待补充
* 多浏览器支持，根据配置文件，自动下载浏览器驱动

* 日志模块: 采用loguru管理日志，可以输出更为优雅，简洁的日志

* 钉钉、企业微信通知: 支持多种通知场景，执行成功之后，可选择发送钉钉、或者企业微信、邮箱通知

* 执行环境一键切换，解决多环境相互影响问题

* 使用pipenv管理虚拟环境和依赖文件，提供了一系列命令和选项来帮助你实现各种依赖和环境管理相关的操作。


## 三、目录结构
```
├────.gitignore 
├────case_utils/ 
│ ├────__init__.py 
│ ├────basepage.py 
│ ├────data_handle.py 
│ └────url_handle.py
├────common_utils/ 
│ ├────__init__.py 
│ ├────loguru_handle.py 
│ ├────project_tree.py 
│ └────yaml_handle.py 
├────config/
│ ├────__init__.py 
│ ├────global_vars.py 
│ ├────project_path.py 
│ ├────report.css 
│ └────settings.py 
├────page/ 
│ ├────__init__.py 
│ ├────login_page.py 
│ └────projects_page.py 
├────test_case/ 
│ └────test_login_demo.py 
├────data/ 
│└────login_demo_data.py 
├────outputs/ 
│ ├────image/ 
│ ├────log/ 
│ │ └────runtime_2023-03-14_17-01-20_856212_error.log 
│ ├────report/ 
│ │ └────uiautotest-report.html 
├────conftest.py 
├────Pipfile 
├────Pipfile.lock 
├────pytest.ini
├────README.md 
├────run.py

 ```   

## 四、依赖库
```
python_version = "3.9"
jsonpath = "==0.82"
openpyxl = "==3.0.9"
pytest = "==6.2.5"
pyyaml = "==6.0"
requests = "==2.26.0"
loguru = "*"
click = "*"
pytest-rerunfailures = "*"
faker = "*"
deepdiff = "*"
pymysql = "*"
yagmail = "*"
selenium = "*"
pyautogui = "*"
pywinauto = "*"
pytest-html = "==2.1.1"
```


## 五、安装教程

1. 通过Git工具clone代码到本地 或者 直接下载压缩包ZIP
```
git clone https://gitlink.org.cn/floraachy/uiautotest.git
```

3. 本地电脑搭建好 python环境，我使用的python版本是3.9


5. 安装pipenv
```
# 建议在项目根目录下执行命令安装
pip install pipenv
```

7. 使用pipenv管理安装环境依赖包：pipenv install （必须在项目根目录下执行）
```
   注意：使用pipenv install会自动安装Pipfile里面的依赖包，该依赖包仅安装在虚拟环境里，不安装在测试机。
```
如上环境都已经搭建好了，包括框架依赖包也都安装好了。

## 六、如何创建用例
### todo 待补充

## 六、运行自动化测试
### 1.  激活已存在的虚拟环境
- （如果不存在会创建一个）：pipenv shell （必须在项目根目录下执行）

### 2. 运行
```
在pycharm>terminal或者电脑命令窗口，进入项目根路径，执行如下命令（如果依赖包是安装在虚拟环境中，需要先启动虚拟环境）。
  > python run.py  (默认在test环境运行测试用例, 报告采用allure)
  > python run.py -env live 在live环境运行测试用例
  > python run.py -env=test 在test环境运行测试用例
  > python run.py -report=pytest-html (默认在test环境运行测试用例, 报告采用pytest-html)
```
注意：
- 如果pycharm.interpreter拥有了框架所需的所有依赖包，可以通过pycharm直接在`run.py`中右键运行


## 初始化项目可能遇到的问题
### 1. 测试机安装的是python3.7，但是本框架要求3.9.5，怎么办？
#### 方法一（建议采纳此方法）
1）首先在项目根目录下打开命令窗口，移除虚拟环境：pipenv --rm
2）安装虚拟环境时忽略锁定的版本号，同时安装依赖包：pipenv install --skip-lock
如果使用上述命令报错：Warning: Python 3.9 was not found on your system... Neither 'pyenv' nor 'asdf' could be found to install Python.
请使用如下命令：pipenv install --python 3.7 --skip-lock  (注意：这里的版本号，如果你的是3.8，就应该如下写命令：pipenv install --python 3.8 --skip-lock)

3）激活虚拟环境：pipenv shell

4）运行框架：python run.py

<br/>

#### 方法二
1）首先在项目根目录下打开命令窗口，移除虚拟环境：pipenv --rm
2）更改项目根目录下的Pipfile文件
```
# 如下所示，3.9更改为3.7
[requires]
python_version = "3.7"
```
3）更改项目根目录下的Pipfile.lock文件
```
# 如下所示，3.9更改为3.7
        "requires": {
            "python_version": "3.7"
        },
```
4）安装虚拟环境，同时安装依赖包：pipenv install

5）激活虚拟环境：pipenv shell

6）运行框架：python run.py

### 2. 无法安装依赖包或者安装很慢，怎么办？
检查一下Pipfile文件中的pip的安装源（位置：Pipfile）
以下安装源均可：
```
pip默认的镜像地址是：https://pypi.org/simple
清华大学：https://pypi.tuna.tsinghua.edu.cn/simple 清华大学的pip源是官网pypi的镜像，每隔5分钟同步一次，重点推荐！！！

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/

豆瓣：http://pypi.douban.com/simple/
```
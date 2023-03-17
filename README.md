# python + selenium + pytest+ pytest-html集成的UI自动化测试框架

**对于框架任何问题，欢迎联系我！**

#### 一、框架架构
暂略

#### 二、项目目录结构
├────.gitignore
├────case_utils/
│    ├────__init__.py
│    ├────basepage.py
│    ├────data_handle.py
│    └────url_handle.py
├────common_utils/
│    ├────__init__.py
│    ├────loguru_handle.py
│    ├────project_tree.py
│    └────yaml_handle.py
├────config/
│    ├────__init__.py
│    ├────global_vars.py
│    ├────project_path.py
│    ├────report.css
│    └────settings.py
├────page/
│    ├────__init__.py
│    ├────login_page.py
│    └────projects_page.py
├────test_case/
│    └────test_login_demo.py
├────data/
│    └────login_demo_data.py
├────outputs/
│    ├────image/
│    ├────log/
│    │    └────runtime_2023-03-14_17-01-20_856212_error.log
│    └────report/
│    │    └────uiautotest-report.html
├────conftest.py
├────Pipfile
├────Pipfile.lock
├────pytest.ini
├────README.md
├────run.py



#### 三、框架功能说明

**解决痛点：**

1. 执行环境**一键切换**，解决**多环境**相互影响问题

```
1) 通过pytest_addoption将命令行参数--env添加到pytest配置对象中
2) 通过get_config去配置文件config.settings.py中读取不同环境的配置信息，包括域名，测试账号
3) 在主运行文件run.py中通过click模块，读取输入的-env的值
4) 最后在运行时输入 python run.py -env=test可以指定运行的环境
```

2. 采用luguru管理日志，可以输出更为优雅，简洁的日志

3. 采用webdriver-manage第三方库，自动帮你识别当前运行环境下系统信息以及对应浏览器信息，并自动下载对应的webdriver，再也不用担心webdriver版本问题！！！

#### 四、框架使用说明

1. 拉取代码到本地

2. 使用pipenv管理安装环境。

```
python版本要求：3.9.5
安装pipenv: pip install pipenv（必须在项目根目录下）
创建虚拟环境：pipenv install （必须在项目根目录下执行）
激活已存在的虚拟环境（如果不存在会创建一个）：pipenv shell （必须在项目根目录下执行）
查看项目虚拟环境路径： pipenv --venv
退出虚拟环境：exit

注意：使用pipenv install会自动安装Pipfile里面的依赖包，该依赖包仅安装在虚拟环境里，不安装在测试机。

注意检查一下pip的安装源（位置：Pipfile）
以下安装源均可：
pip默认的镜像地址是：https://pypi.org/simple
清华大学：https://pypi.tuna.tsinghua.edu.cn/simple 清华大学的pip源是官网pypi的镜像，每隔5分钟同步一次，重点推荐！！！

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/

豆瓣：http://pypi.douban.com/simple/
```

3. 更改配置文件config.settings.py，配置test和live环境及测试账号, 测试报告的定制化信息展示, 浏览器驱动类型

4. 在page目录下新建一个py文件，编写某个页面的元素定位及相关操作

5. 在data目录下新建测试用例数据文件，编写测试用例, 测试用例使用py编写，呈现形式是python列表嵌套字典

6. 在test_case下编写测试用例

7. 框架主入口为 run.py文件
```
	必须在项目根目录下，输入命令运行（如果依赖包是安装在虚拟环境中，需要先启动虚拟环境）。
    注意：本机环境中没有安装依赖包的情况下，不要直接在run.py中右键直接run
  > python run.py  (默认在test环境运行测试用例)
  > python run.py -env live 在live环境运行测试用例
  > python run.py -env=test 在test环境运行测试用例
```

#### 三、框架使用过程中遇到的问题
##### 测试机安装的是python3.7，但是本框架要求3.9.5，怎么办？
方法一：建议采纳此方法
1）首先在项目根目录下打开命令窗口，移除虚拟环境：pipenv --rm
2）安装虚拟环境时忽略锁定的版本号，同时安装依赖包：pipenv install --skip-lock
如果使用上述命令报错：Warning: Python 3.9 was not found on your system... Neither 'pyenv' nor 'asdf' could be found to install Python.
请使用如下命令：pipenv install --pyhon 3.7 --skip-lock  (注意：这里的版本号，如果你的是3.8，就应该如下写命令：pipenv install --python 3.8 --skip-lock)

5）激活虚拟环境：pipenv shell

6）运行框架：python run.py


方法二：
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
**第一部分：PYTHON虚拟环境管理工具**
- <a href="#1.1">**1.1.自带环境管理工具之[venv]**</a>
- <a href="#1.2">**1.2.虚拟环境管理工具之[virtualenv + Virtualenvwrapper]**</a>
- <a href="#1.3">**1.3.虚拟环境管理工具之[pipenv]**</a>

**第二部分：PYTHON虚拟环境迁移复制**
- <a href="#2.1">**2.1.虚拟环境迁移至在线环境**</a>
- <a href="#2.2">**2.2.虚拟环境迁移至离线环境**</a>

---
<a id="1.1">**1.1.自带环境管理工具之[venv]**</a>
```html
前言说明：如果你使用python3.3及以上版本，推荐使用标准库内置的venv模块替代virtualenv，两者的使用方式基本相同，唯一不同的是创建虚拟环境的方式。
```
```html
>>>第一步，创建项目目录
mkdir python_venv_demo

>>>第二步，进入改文件目录
cd python_venv_demo

>>>第三步，创建虚拟环境
python -m venv venv_demo  # venv_demo 就是虚拟环境的名字
注意：python3内置了venv，所以不用再pip安装virtualenv了。

>>>第四步，激活虚拟环境（只有激活之后才能进入虚拟环境）
cd venv_demo/Scripts
Windows>： activate.bat
Linux$： source activate

>>>激活成功后，终端提示符会显示虚拟环境的名称。
(venv_demo)>......

>>>第五步：退出虚拟环境
deactivate.bat
```

<a id="1.2">**1.2.虚拟环境管理工具之[virtualenv + Virtualenvwrapper]**</a>
```html
如果你使用python2，那就只能选择virtualenv，你需要额外安装它。我先假设你已经安装了pip，因为在python2 >=2.7.9 或 python3 >=3.4这些版本的python会一并安装pip，其他版本可以参考文档的安装部分。
```
```html
1.安装virtualenv库
# pip install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple
```
```html
2.创建虚拟环境
# virtualenv [虚拟环境名称]  比如：virtualenv venv
# 如果不想使用系统的包,加上–no-site-packeages参数
# virtualenv [虚拟环境名称] --no-site-packages [python可执行程序路径]
```
```html
3.激活虚拟环境
--->Linux系统:
$ cd venv
$ source ./bin/activate

--->Windows系统:
> cd venv
> .\Scripts\activate.bat
```
```html
4.退出虚拟环境
--->Linux系统:
$ deactivate

--->Windows系统:
> .\Scripts\deactivate.bat
```
```html
5.删除虚拟环境
没有使用virtualenvwrapper前，可以直接删除venv文件夹来删除环境
```
```html
6.使用虚拟环境
--->Linux系统
# cd venv
# source activate
(venv)# pip list
(venv)# python
(venv)# deactivate
# ls

--->Windows系统
> cd venv
> .\Scripts\activate.bat
(venv) > pip list
(venv) > python
(venv) > .\Scripts\deactivate.bat
> dir
```

<a id="1.2">**1.2.虚拟环境管理工具之[Virtualenvwrapper]**</a>
```html
1.安装virtualenvwrapper库
--->Windows系统
pip install virtualenvwrapper-win -i https://pypi.tuna.tsinghua.edu.cn/simple

--->MacOS/Linux系统
pip install --user virtualenvwrapper
# then make Bash load virtualenvwrapper automatically
echo "source virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
```
```html
2. 创建虚拟环境
# on macOS/Linux:
mkvirtualenv --python=python3.6 venv
# on Windows
mkvirtualenv --python=python3 venv
```
```html
3. 激活虚拟环境
workon # 列出虚拟环境列表
workon [venv] # 切换环境
```
```html
4. 退出虚拟环境
deactivate
```
```html
5. 删除虚拟环境
rmvirtualenv venv
```

<a id="1.3">**1.3.虚拟环境管理工具之[pipenv]**</a>
```html
	Python官方推荐的包管理工具pipenv。 它综合了virtualenv, pip和pyenv三者的功能。能够自动为项目创建和管理虚拟环境。如果你使用过requests库，就一定会爱上这个库，因为是同一个大神出品。 pipenv使用Pipfile和Pipfile.lock来管理依赖包，并且在使用pipenv添加或删除包时，自动维护Pipfile文件，同时生成 Pipfile.lock来锁定安装包的版本和依赖信息，避免构建错误。相比pip需要手动维护requirements.txt 中的安装包和版本，具有很大的进步。
```
```html
>>> 1. 安装pipenv库
$ pip install pipenv  -i https://pypi.tuna.tsinghua.edu.cn/simple
```
```html
>>> 2. 创建虚拟环境
$ cd myproject
$ pipenv install # 创建环境
$ pipenv install requests # 或者直接安装库同时默认安装虚拟环境

# 如果不存在pipfile,会生成一个pipfile，并且如果有的库添加会自动编辑该文件，不会我们手动更新requirements.txt文件了。
# 当我们安装依赖包时，会生成一个Pipfile.lock文件记录安装的依赖包相关信息
```
```html
>>> 3. 激活虚拟环境
$ pipenv shell
$ python --version
```
```html
>>> 4.pip源加速方法
1.修改Pipfile配置镜像源，格式如下
[[source]]
name = "pypi"
url = "https://pypi.org/simple"--->"https://mirrors.aliyun.com/pypi/simple"  # 此处替换为阿里源
verify_ssl = true

[dev-packages]

[packages]
requests = "*"

[requires]
python_version = "2.7"

2.安装依赖包时指定镜像源地址
pipenv install --pypi-mirror https://mirrors.aliyun.com/pypi/simple
```

```html
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --completion                    Output completion (to be executed by the
                                  shell).

  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.

  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.

  --three / --two                 Use Python 3/2 when creating virtualenv.
  --clear                         Clears caches (pipenv, pip, and pip-tools).
                                  [env var: PIPENV_CLEAR]

  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check      Checks for PyUp Safety security vulnerabilities and against PEP
             508 markers provided in Pipfile.

  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.

  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Uninstalls a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
```

<a id="2.1">**2.1.虚拟环境迁移至在线环境**</a>
```html
>>> 1.在原虚拟环境中收集项目中的依赖包名称及版本，生成依赖清单到文本文件。
方式一：使用pip工具
source activate / activate.bat # 进入虚拟环境
pip freeze > requirements.txt
方式二：使用pipreqs工具
pip install pipreqs -i https://pypi.tuna.tsinghua.edu.cn/simple
cd [project]
pipreqs ./ --encoding=utf-8
```
```html
>>> 2.复制依赖清单文件到新的虚拟环境中，在线安装依赖清单中的全部依赖包。
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

<a id="2.2">**2.2.虚拟环境迁移至离线环境**</a>
**迁移方式1：下载好的依赖包复制到新的环境进行pip安装**
```html
>>> 1.在原虚拟环境中收集项目中的依赖包名称及版本，生成依赖清单到文本文件。
方式一：使用pip工具
source activate / activate.bat # 进入虚拟环境
pip freeze > requirements.txt
方式二：使用pipreqs工具
pip install pipreqs -i https://pypi.tuna.tsinghua.edu.cn/simple
cd [project]
pipreqs ./ --encoding=utf-8
```
```html
>>> 2.批量下载依赖包清单中的依赖包到本地指定文件夹。
pip download -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple  ./pkg
```
```html
>>> 3.批量安装依赖包清单中的依赖包到本地指定文件夹。
1.复制已下载依赖包的文件夹到新的环境中
2.进入虚拟环境，进行批量依赖包的安装
pip install --no-index --find-index= ./pkg -r requirements.txt
```
**迁移方式2：同系统环境下，直接复制原虚拟环境到新环境，修改配置**
```html
背景说明：一般我们在公司进行项目开发时，开发环境和测试环境一般是可以访问互联网的，但是考虑到安全问题生产环境增加了层层防火墙，对外部环境进行了隔离。这时我们上线部署环境时需要安装一些python依赖包就比较棘手，会出现各种的问题。
```
```html
目前隔离的生产环境安装python依赖包用的比较多的方式有两种：一种是在互联网环境下下载所需要的依赖包进行打包，然后上传到生产环境进行手动安装；另一种方式复制原虚拟环境中的site-packages文件夹进行打包，上传到新的虚拟环境中进行解包进行替换(注意此操作要在相同的OS环境之间进行替换)。
```
```html
>>> Windows系统虚拟环境之间复制site-packages
1.进入虚拟环境文件夹(C:\Users\Administrator\venv2.7\Lib)，打包该路径下的site-packages文件夹。
2.把原site-packages文件夹复制到新的虚拟环境文件夹(C:\Users\Administrator\venv2.7\Lib)，替换原来的site-packages文件夹。
3.进入虚拟环境，然后使用pip list测试依赖包是否已经进行了替换安装。
```
```html
>>> Linux系统虚拟环境之间复制site-packages
1.进入虚拟环境文件夹(venv2.7/lib/python2.7)，打包该路径下的site-packages文件夹。
2.把原site-packages文件夹复制到新的虚拟环境文件夹(venv2.7/lib/python2.7)，替换原来的site-packages文件夹。
3.进入虚拟环境，然后使用pip list测试依赖包是否已经进行了替换安装。
```

**参考文档**
[**新一代Python项目环境与依赖管理工具**](https://zhuanlan.zhihu.com/p/37581807)

---
**作者：张星星**
**昵称：码农青葱**
**时间：2019-07-13 21:09:17 星期六**
**邮箱：8374072892@qq.com**
**声明：此文章结合个人开发经验和部分网络知识总结而成，欢迎网友指正分享转载。**
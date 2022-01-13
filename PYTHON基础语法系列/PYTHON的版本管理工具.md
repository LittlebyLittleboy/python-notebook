**第一部分 pyenv works theory**
- <a href="#1.1">**1.1.pyenv基本原理**</a>
- <a href="#1.1">**1.2.pyenv运行过程**</a>

**第二部分：pyenv for windows**
- <a href="#2.1">**2.1.pyenv-win命令行安装**</a>
- <a href="#2.2">**2.2.pyenv-win环境变量配置**</a>
- <a href="#2.3">**2.3.pyenv-win语法使用说明**</a>

**第三部分：pyenv for linux**
- <a href="#3.1">**3.1.pyenv的下载安装**</a>
- <a href="#3.2">**3.2.pyenv环境变量配置**</a>
- <a href="#3.3">**3.3.pyenv语法使用说明**</a>

**第四部分：pyenv for macOS**
- <a href="#4.1">**4.1.pyenv的下载安装**</a>
- <a href="#4.2">**4.2.pyenv环境变量配置**</a>
- <a href="#4.3">**4.3.pyenv语法使用说明**</a>

<a id="1.1">**1.1.pyenv基本原理**</a>
```html
pyenv是利用系统环境变量PATH的优先级，劫持python的命令到pyenv上，根据用户所在的环境或目录，选择使用不同版本的python。
```
```html
在较高级别上，pyenv使用注入到PATH中的shim可执行文件拦截python命令，确定应用程序指定了哪个python版本，并将命令传递到正确的python安装。
```
<a id="1.1">**1.2.pyenv运行过程**</a>
```html
对于系统环境变量PATH，里面包含了一串由冒号分隔的路径，例如[/usr/local/bin:/usr/bin:/bin]。每当在系统中执行一个命令时，
例如python或pip，操作系统就会在PATH的所有路径中从左至右依次寻找对应的命令。因为是依次寻找，因此排在左边的路径具有更高的优先级。在PATH最前面插入一个  $(pyenv root)/shims目录，$(pyenv root)/shims目录里包含名称为python以及 pip 等可执行脚本文件；当用户执行python或 pip 命令时，根据查找优先级，系统会优先执行shims目录中的同名脚本。pyenv正是通过这些脚本，来灵活地切换至我们所需的 python版本。
```
```html
特别提醒：使用pyenv安装的python环境和系统的python或手动安装的python相互隔离。
```

<a id="2.1">**2.1.pyenv-win命令行安装**</a>
```html
系统声明：此处我本人使用的Windows10操作系统进行演示测试
```
```html
>>>安装方式一：使用pip包管理工具进行安装
[Powershell]> pip install pyenv-win --target $HOME\.pyenv
或者
[Git Bash]$ pip install pyenv-win --target $HOME\.pyenv
或者
[cmd.exe]: pip install pyenv-win --target %USERPROFILE%\.pyenv
```
```html
>>>安装方式二：使用zip压缩包解压进行安装
1.压缩包下载: https://github.com/pyenv-win/pyenv-win/archive/master.zip

2.移动安装包：在$HOME or %USERPROFILE%目录下创建一个.pyenv文件夹，提取和移动pyenv-win到$HOME\.pyenv\(Powershell)或%USERPROFILE%\.pyenv\(cmd.exe)

3.检查文件夹：检查%USERPROFILE%\.pyenv\pyenv-win或$HOME\.pyenv\pyenv-win是否存在
```
```html
>>>安装方式三：使用git克隆到本地进行安装
[Powershell]> git clone https://github.com/pyenv-win/pyenv-win.git $HOME/.pyenv
或者
[Git Bash]> git clone https://github.com/pyenv-win/pyenv-win.git $HOME/.pyenv
或者
[cmd.exe]: git clone https://github.com/pyenv-win/pyenv-win.git %USERPROFILE%\.pyenv
```

<a id="2.2">**2.2.pyenv-win环境变量配置**</a>
```html
1.添加系统环境变量
此电脑--->右键属性--->高级系统设置--->环境变量--->系统环境变量--->新建
变量名：PYENV
变量值：%USERPROFILE%\.pyenv\pyenv-win
```
```html
2.添加路径到Path变量
双击Path变量--->新建
新建1：%PYENV%\bin
新建2：%PYENV%\shims
```
```html
3.检查pyenv是否安装成功
添加完以后在命令行输入查询命令看看是否已经安装完
> pyenv --version
如果没有有可能需要重启一下电脑再次查询
> pyenv --version
```

<a id="2.3">**2.3.pyenv-win语法使用说明**</a>
```html
C:\Users\Administrator>pyenv --help
pyenv 2.64.3

Usage: pyenv <command> [<args>]

Some useful pyenv commands are:
   commands     列出全部可用的pyenv命令
   duplicate    创建一个复制的python环境
   local        设置或显示局部python版本
   global       设置或显示全局python版本
   shell        设置或显示指定的python 版本
   install      使用python-build安装一个python版本
   uninstall    卸载指定版本的python
   update       更新缓存的版本库
   rehash       安装新的python版本后刷新pyenv shims
   vname        查看当前python版本
   version      查看当前使用的python版本
   versions     查看所有pyenv已安装的python版本
   exec         执行一个可执行的python版本
   which        显示可执行python版本的全路径
   whence       列出全部包含已给出的可执行python版本
```
```html
# 查询pyenv工具自身的版本号
> pyenv --version
pyenv 2.64.3
```
```html
# 查看全部已安装python版本
> pyenv versions
```
```html
# 查看当前在使用python版本
> pyenv version
```
```html
# 设置局部使用python版本
> pyenv local 3.7.3
```
```html
# 取消局部python版本设置
> pyenv local --unset
或者
删除C:\Users\Administrator\.pyenv\.python-version文件
```
```html
C:\Users\Administrator>pyenv install --help
:: [Info] ::  Mirror: https://www.python.org/ftp/python
Usage: pyenv install [-f] <version> [<version> ...]
       pyenv install [-f] [--32only|--64only] -a|--all
       pyenv install [-f] -c|--clear
       pyenv install -l|--list

  -l/--list   列出全部可用版本
  -a/--all    从缓存安装全部版本
  -c/--clear  删除缓存全部安装包程序
  -f/--force  强制安装忽略是否已安装
  -q/--quiet  安装在用或退出
  --32only    仅32位
  --64only    仅64位
  --help      帮助文档
```
```html
# 安装指定版本的python
> pyenv install 3.7.3

超时问题：由于网络问题，一般在下载安装包的过程中会出现超时异常
解决方法1：修改.pyenv\pyenv-win\libexec\libs\pyenv-install-lib.vbs文件，更换镜像为阿里源或华为源
        Dim mirror
		mirror = objws.Environment("Process")("PYTHON_BUILD_MIRROR_URL")
		If mirror = "" Then mirror = "https://www.python.org/ftp/python"
		修改为
		Dim mirror
		mirror = objws.Environment("Process")("PYTHON_BUILD_MIRROR_URL")
		If mirror = "" Then mirror = "https://npm.taobao.org/mirrors/python/"
解决方法2：从官网或者或内镜像站下载需要安装的软件包到./pyenv/pyenv-win/install_cache文件夹下
		pyenv install 3.7.3 # 跳过下载，直接使用本地./pyenv/pyenv-win/install_cache中的文件进行安装
```
```html
# 卸载某个已安装的版本
> pyenv uninstall 3.7.3
```

<a id="3.1">**3.1.pyenv的下载安装**</a>
```html
系统声明：此处我本人使用的CentOS7操作系统进行演示测试
```
```html
# 使用git克隆到家目录.pyenv(已安装git工具)
$ git clone https://github.com/pyenv/pyenv  ~/.pyenv
```
<a id="3.2">**3.2.pyenv环境变量配置**</a>
```html
[root@centos_7 cache]# cat  ~/.bashrc
```
```html
# .bashrc
# User specific aliases and functions
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi
# 添加最后的三行配置，保存文件
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```
```html
# 使配置生效
$ source  ~/.bashrc
或者 exec  $SHELL -l
```

<a id="3.3">**3.3.pyenv语法使用说明**</a>
```html
说明：pyenv基本语法和Windows相同，此处我们主要介绍使用pyenv安装python部分。
```
```html
1.安装python依赖环境
$ yum install -y python-devel libevent-devel python-pip gcc xz-devel openssl-devel readline-devel sqlite-devel bzip2-devel
```
```html
2.列出可以安装的python版本
$ pyenv install --list
```
```html
3.使用pyenv下载和安装python
	由于pyenv是先将python安装包下载到 ~/.pyenv/cache/目录，然后校验md5值，再安装的。所以在实际安装过程中，如果用pyenv install [版本号]的命令安装python比较慢，则可以手动将python-x.x.x 下载到cache/目录，再用pyenv install x.x.x 命令安装。

(1).下载安装包到~/.pyenv/cache/
# wget http://mirrors.sohu.com/python/3.x.x/Python-3.x.x.tar.xz -P ~/.pyenv/cache/
(2).然后使用命令安装python
# cd ~/.pyenv/cache/
# pyenv install 3.x.x
```
```html
# 安装包下载地址
https://github.com/pyenv/pyenv （pyenv 官网 github仓库）
https://github.com/pyenv/pyenv/wiki （pyenv 官网 github Wiki)
https://github.com/pyenv/pyenv-virtualenv (pyenv-virtualenv 官网 github)
```

<a id="4.1">**4.1.pyenv的下载安装**</a>
```html
>>> 方式一：克隆安装包到本地家目录下
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
>>> 方式二：MacOS的话可以直接用homebrew安装
$ brew update
$ brew install pyenv
```

<a id="4.2">**4.2.pyenv环境变量配置**</a>
```html
# 添加shell配置文件中追加如下: (如zshrc)
export PYENV_ROOR="$HOME/.pyenv"
export PATH=$PYENV_ROOT/shims:$PATH
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
# source一下配置文件, 输入pyenv --version测试一下
```
<a id="4.3">**4.3.pyenv语法使用说明**</a>
```html
说明：pyenv基本语法和Windows相同，此处不再做详细分析，参考Windows部分pyenv语法使用说明。
```

---
**作者：张星星**
**昵称：码农青葱**
**时间：2019-07-12 19:10:17 星期五**
**邮箱：8374072892@qq.com**
**声明：此文章结合个人开发经验和部分网络知识总结而成，欢迎网友指正分享转载。**
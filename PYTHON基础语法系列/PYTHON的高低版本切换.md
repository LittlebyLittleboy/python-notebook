**第一部分：Windows系统下不同版本PYTHON切换**
- <a href="#1.1">**1.1.Windows系统下多版本PYTHON存在问题**</a>
- <a href="#1.2">**1.2.Windows系统下多版本PYTHON切换方式**</a>

**第二部分：Linux系统下不同版本PYTHON切换**
- <a href="#2.1">**2.1.Linux系统下多版本PYTHON存在问题**</a>
- <a href="#2.2">**2.2.Linux系统下多版本PYTHON切换方式**</a>

**第三部分：Mac系统下不同版本PYTHON切换**
- <a href="#3.1">**3.1.Mac系统下多版本PYTHON存在问题**</a>
- <a href="#3.2">**3.2.Mac系统下多版本PYTHON切换方式**</a>

---
<a id="1.1">**1.1.Windows系统下多版本PYTHON存在问题**</a>
```html
	在Windows系统中安装python时，无论python2和python3的可执行文件都是python.exe，同时它们对应的pip都叫pip.exe，在cmd下输入python得到的版本号取决于环境变量里哪个版本的python路径更靠前，因为运行命令时是按照添加环境变量的顺序来执行的。
```
```html
	事实上这个问题在PYTHON官方网站已经给出了解决方案。我们在安装Python3（>=3.3）时，Python的安装包实际上在系统中安装了一个启动器py.exe，默认放置在文件夹C:\Windows\下面。这个启动器允许我们指定使用Python2还是Python3来运行代码（当然前提是你已经成功安装了Python2和Python3）。
```

<a id="1.2">**1.2.Windows系统下多版本PYTHON切换方式**</a>
```html
>>>方式一：修改可执行文件名称，添加环境变量（不推荐使用）
先安装的python版本可执行文件保持不变，后安装的python的可执行文件python.exe对应改成python2.exe/python3.exe，然后添加到环境变量，但修改可执行文件的方式不推荐使用。
```
```html
>>>方式二：使用PYTHON启动器，运行时加参数（推荐使用）
利用py启动器的一个参数来调用不同版本的python,当使用python2时，py -2调用python2解释器，当使用python3时，py -3调用的是python3。
```

```html
# 运行脚本文件时，可选择去掉参数 -2/-3
当python脚本需要python2运行时，只需在脚本前加上#! python2，然后运行py xxx.py即可。
#! python2
当python脚本需要python3运行时，只需在脚本前加上#! python3，，然后运行py xxx.py即可。
#! python3
```

```html
当PYTHON2和PYTHON3同时存在于Windows上时，它们对应的pip都叫pip.exe，所以不能够直接使用 pip install 命令来安装软件包。而是要使用启动器py.exe来指定pip的版本。同时，这也完美解决了在pip在python2和python3共存的环境下报错，提示Fatal error in launcher: Unable to create process using '"'的问题。
```
```shell
# 当需要python2的pip时，只需
> py -2 -m pip install xxx
# 当需要python3的pip时，只需
> py -3 -m pip install xxx
```

```html
# !python2和# coding: utf-8哪个写在前面？

#! python2 需要放在第一行，编码说明可以放在第二行。所以文件开头应该类似于：
#! python2
# coding: utf-8
```

<a id="2.1">**2.1.Linux系统下多版本PYTHON存在问题**</a>
```html
	Linux系统一般默认已安装PYTHON2，当我们编译安装PYTHON3版本到系统环境中，不做任何处理的情况下，需要进入安装包指定python3.x程序运行。
```

<a id="2.2">**2.2.Linux系统下多版本PYTHON切换方式**</a>
```html
	如要全局同时使用PYTHON2和PYHON3，则需要把安装的新版本PYTHON执行程序添加到环境变量，并且创建软链接到/usr/bin目录中。（参考安装部分修改环境变量）
```

<a id="3.1">**3.1.Mac系统下多版本PYTHON存在问题**</a>
```html
类比Linux处理方式
```
<a id="3.2">**3.2.Mac系统下多版本PYTHON切换方式**</a>
```html
类比Linux处理方式
```

---
**作者：张星星**
**昵称：码农青葱**
**时间：2019-07-08 19:20:10 星期一**
**邮箱：8374072892@qq.com**
**声明：此文章结合个人开发经验和部分网络知识总结而成，欢迎网友指正分享转载。**
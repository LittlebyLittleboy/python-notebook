**第一部分：Windows系统安装PYTHON环境**
- <a href="#1.1">**1.1.Windows-PYTHON软件下载**</a>
- <a href="#1.2">**1.2.Windows-PYTHON软件安装**</a>
- <a href="#1.3">**1.3.Windows-PYTHON软件测试**</a>

**第二部分：Linux系统安装PYTHON环境**
- <a href="#2.1">**2.1.Linux-PYTHON软件下载**</a>
- <a href="#2.2">**2.2.Linux-PYTHON依赖安装**</a>
- <a href="#2.3">**2.3.Linux-PYTHON软件安装**</a>
- <a href="#2.4">**2.4.Linux-PYTHON软件测试**</a>

**第三部分：Mac系统安装PYTHON环境**
- <a href="#3.1">**3.1.MacOS-PYTHON软件下载**</a>
- <a href="#3.2">**3.2.MacOS-PYTHON软件安装**</a>
- <a href="#3.3">**3.3.MacOS-PYTHON软件测试**</a>

---
<a id="1.1">**1.1.Windows-PYTHON软件下载**</a>
```html
[官方下载链接：https://www.python.org/downloads]
[国内华为镜像：https://mirrors.huaweicloud.com/python/]
[国内阿里镜像：https://npm.taobao.org/mirrors/python/]
```
![](https://www.showdoc.cc/server/api/common/visitfile/sign/1e855d590b7698fd4fd08b95ffdd1fcf?showdoc=.jpg)

<a id="1.2">**1.2.Windows-PYTHON软件安装**</a>
```html
[注意：添加环境变量到本地，安装方式默认安装/自定义安装，此处默认安装]
```
![](https://www.showdoc.cc/server/api/attachment/visitfile/sign/0a162add8321562075c72ef547c05564?showdoc=.jpg)

![](https://www.showdoc.cc/server/api/common/visitfile/sign/13da1f84dd63196ba2bad7314a77efaa?showdoc=.jpg)

<a id="1.3">**1.3.Windows-PYTHON软件测试**</a>
![](https://www.showdoc.cc/server/api/attachment/visitfile/sign/f2014c5e03bd20ceb06f2237d7497625?showdoc=.jpg)


<a id="2.1">**2.1.Linux-PYTHON源码下载**</a>
```html
Linux系统下一般自安装PYTHON2，此处我们介绍CentOS7系统中PYTHON3源码编译安装。
```
```html
方式一：直接在官方网站下载PYTHON3源码
```
![](https://www.showdoc.cc/server/api/attachment/visitfile/sign/3b788c1d4d8d17fe53be5cbe6d1a10f3?showdoc=.jpg)

```html
方式二：WGET下载工具下载PYTHON3源码
```
```shell
# wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
```

<a id="2.2">**2.2.Linux-PYTHON依赖安装**</a>
```shell
# yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```
<a id="2.3">**2.3.Linux-PYTHON源码安装**</a>

```shell
1.创建安装位置，并解压安装包
# mkdir -p /usr/local/python3
# tar -zxvf Python-3.6.1.tgz -C /usr/local/python3
```

```shell
2.源码编译安装，并建立软连接
# cd /usr/local/python3/Python-3.6.1
# ./configure --prefix=/usr/local/python3
# make && make install
# ln -s /usr/local/python3/bin/python3 /usr/bin/python3
```

```shell
3.添加环境变量，将/usr/local/python3/bin加入PATH
# vim ~/.bash_profile
```
```html
# .bash_profile
# Get the aliases and functions
if [ -f ~/.bashrc ]; then
. ~/.bashrc
fi
# User specific environment and startup programs
PATH=$PATH:$HOME/bin:/usr/local/python3/bin
export PATH
```
```shell
# 修改完按ESC，输入:wq回车退出，然后修改生效
# source ~/.bash_profile
```

<a id="2.4">**2.4.Linux-PYTHON软件测试**</a>
```shell
1.检查PYTHON3及PIP3是否正常可用
# python3 -V
Python 3.6.1
# pip3 -V
pip 9.0.1 from /usr/local/python3/lib/python3.6/site-packages (python 3.6)
# 若pip无法找到，尝试建立软连接到全局，或进行下面步骤进行下载安装
# ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

```shell
2.若未安装pip，则安装pip和setuptools
安装pip前需要前置安装setuptools
# wget --no-check-certificate  https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26
或则
https://pypi.org/project/setuptools/ 浏览器进行下载
```

```shell
# tar -zxvf setuptools-19.6.tar.gz
# cd setuptools-19.6
# python3 setup.py build
# python3 setup.py install
```

```shell
如果前面没布置好环境的话，就要苦逼一下了：
报错： RuntimeError: Compression requires the (missing) zlib module
我们需要在linux中安装zlib-devel包，进行支持。
# yum install zlib-devel
```
```shell
需要对python3.5进行重新编译安装。
# cd python3.6.1
# make && make install
```
```shell
重新安装setuptools
# python3 setup.py build
# python3 setup.py install
```

<a id="3.1">**3.1.MacOS-PYTHON软件下载**</a>
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/3510e5905c7f726a5a81f7f87c40e938?showdoc=.jpg)
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/3e9da0a9773c62b25e620b10316fae4b?showdoc=.jpg)

<a id="3.2">**3.2.MacOS-PYTHON软件安装**</a>
```html
软件下载完毕后，点击安装，自定义或默认安装到磁盘
```

<a id="3.3">**3.4.MacOS-PYTHON软件测试**</a>
```shell
# python3 --version
# pip3 --version
```

---
**作者：张星星**
**昵称：码农青葱**
**邮箱：8374072892@qq.com**
**声明：此文章结合个人开发经验和部分网络知识总结而成，欢迎网友指正分享转载。**


**第一部分：Pycharm安装使用**
- <a href="#1.1">**1.1.Windows环境下安装Pycharm**</a>
- <a href="#1.2">**1.2.Linux环境下安装Pycharm**</a>
- <a href="#1.3">**1.3.MacOS环境下安装Pycharm**</a>
- <a href="#1.4">**1.4.Pycharm快捷使用指南**</a>

**第二部分：Sublime安装使用**
- <a href="#2.1">**2.1.Windows环境下安装Sublime Text**</a>
- <a href="#2.2">**2.2.Linux环境下安装Sublime Text**</a>
- <a href="#2.3">**2.3.MacOS环境下安装Sublime Text**</a>
- <a href="#2.4">**2.4.Sublime Text快捷使用指南**</a>

---
<a id="1.1">**1.1.Windows环境下安装Pycharm**</a>
```html
1.在线下载PyCharm可执行安装包(https://www.jetbrains.com/pycharm/download/#section=windows)到本地。
```
```html
2.双击下载好的PyCharm可执行安装包(pycharm-professional-2020.2.3)，选择软件的安装目录或默认安装目录。
```
```html
3.点击下一步(Next)，选中创建桌面快捷键和创建.py关联，点击下一步进入在安装状态(Installing)等待安装完成。
```
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/fb24fea126042c820dd12954b84663f5?showdoc=.jpg)
```html
4.双击桌面PyCharm快捷键启动应用程序，首次运行需要接受协议和主题配置(选中跳过即可)，进入证书激活界面，选择免费激活。
```
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/802c2275413ca72090468c5bc6a1b586?showdoc=.jpg)

```html
5.进入项目创建配置界面，创建一个测试项目并进入项目，查看免费使用时间(Help--->register)，一般免费30天。
```
```html
6.警告！！！，进入激活主题，提前下载激活包节安装参数包到本地，把jetbrains-agent-latest.zip激活包拖入到项目，按照提示重启PyCharm程序。
```
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/747b091fc4d024c891f0bca5e10a194d?showdoc=.jpg)

```html
7.重新启动PyCharm应用，提示填写安装参数，把之前下载好的安装参数复制进去，重新启动PyCharm应用，然后查看有效期(Help--->register)。
```
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/c5a196f7d73531a378ee06bea52c27ee?showdoc=.jpg)

<a id="1.2">**1.2.Linux环境下安装Pycharm**</a>

<a id="1.3">**1.3.MacOS环境下安装Pycharm**</a>

<a id="1.4">**1.4.Pycharm快捷使用指南**</a>

<a id="2.1">**2.1.Windows环境下安装Sublime Text**</a>
**1.下载Sublime Text软件包**
```
<1>.Sublim官方网站下载Sublime Text3安装包官网地址或者百度云盘
[http://www.sublimetext.com/]
或者
[https://www.macbl.com/app/development/sublime-text-3]
<2>.汉化地址：https://github.com/rexdf/ChineseLocalization
```
![](https://www.showdoc.cc/server/api/common/visitfile/sign/2b88bef68ad0414c99cb6d84df24b5c4?showdoc=.jpg)

**2.安装Sublime Text编辑器**
```html
<1>.默认安装路径或者自定义安装路径
<2>.选中[Add to explorer context menu]，便于选择打开方式
```
![](https://www.showdoc.cc/server/api/common/visitfile/sign/3fdc15453a6d326e2d5494f992c89512?showdoc=.jpg)

**3.安装Sublime Text的License**
```html
<1>.许可证更新地址[https://www.macbl.com/app/development/sublime-text-3]
<2>.Help--->Enter License
```
```html
— BEGIN LICENSE —–
ZYNGA INC.
50 User License
EA7E-811825
927BA117 84C9300F 4A0CCBC4 34A56B44
985E4562 59F2B63B CCCFF92F 0E646B83
0FD6487D 1507AE29 9CC4F9F5 0A6F32E3
0343D868 C18E2CD5 27641A71 25475648
309705B3 E468DDC4 1B766A18 7952D28C
E627DDBA 960A2153 69A2D98A C87C0607
45DC6049 8C04EC29 D18DFA40 442C680B
1342224D 44D90641 33A3B9F2 46AADB8F
—— END LICENSE ——
```
![](https://www.showdoc.cc/server/api/common/visitfile/sign/c34c57e697623996771d30605c9fb5fb?showdoc=.jpg)

**4.Sublime Text编辑器配置Python语言**
```html
<1>.点击"首选项/浏览包"（Reference/Brower Packages），点开之后出来一个目录图形窗口，我们找到python文件夹，如果没有我们新建一个python文件夹

<2>.在python文件夹里，我们再建一个文件命名为 Python.sublime-commands并写入如下配置内容。
{"cmd":["python.exe", "-u", "$file"],
"path":"D:\python3.6",
"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
"selector": "source.python"}

<3>.修改好之后我们点击保存，我们点击"Tools/Bulid System/Python"选择语言

<4>.然后我们回到之前的python文件，我们点击"Tools/Bulid"(快捷键是Ctrl+B,后面就按快捷键了)，可以看到运行的结果
```
**5.安装Package Control**
```html
前文提到Sublime Text支持大量插件，如何找到并管理这些插件就成了一个问题，Package Control正是为了解决这个问题而出现的，利用它我们可以很方便的浏览、安装和卸载Sublime Text中的插件。
```
```html
1.进入Package Control的官网（服务器较远，可能需要VPN），里面有详细的安装教程。Package Control支持Sublime Text 2和3，本文只给出3的安装流程：官方指导

2.使用Ctrl + (Esc键下边那个键)打开Sublime Text控制台。

3.将下面的代码粘贴到控制台里：
import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)

4.等待Package Control安装完成。之后使用Ctrl + Shift + P打开命令板，输入PC应出现Package Control：安装完成后，在工具栏Preferences下面查找Package Control，如果存在Package Control则说明安装成功。

解决Sublime Text3安装插件时报there are no packages available for installation问题:
第一种原因：
是因为 ipv6 的问题，导致无法访问 sublime 官网，解决方法：在 hosts 文件中添加对应IP，请注意！不要使用网上教程中的IP地址，需要你自己ping sublime.wdvob.net，因为这个有可能是变化的，本机屏的IP：74.207.232.232；在 hosts 文件中添加如下对应 IP 
74.207.232.232       sublime.wbond.net

第二种原因：
因为连接不上 json 文件导致
测试下你能否打开 https://packagecontrol.io/channel_v3.json 这个地址，无法打开导致读取不到插件列表。

打开 首选项 > package settings > package control > settings - default

第6行，默认是 "https://packagecontrol.io/channel_v3.json"，

打开 Preferences > package settings > package control > settings > user 替换成你的下载 的channel_v3.json 就好了，我的channel_v3.json放在\Sublime Text 3\Packages路径下。

Preferences > package settings > package control > settings > user Package Control.sublime-settings：
{
	"bootstrapped": true,
	"in_process_packages":
	[
	],
	"installed_packages":
	[
		"Package Control"
	],
	"channels": [
		"C:/Users/Administrator/AppData/Roaming/Sublime Text 3/Packages/channel_v3.json"
	]
}

5.成功安装Package Control之后，我们就可以方便的安装使用Sublime Text的各种插件：
使用快捷键 Ctrl + Shift + P，打开Package Control，输入install，选择Install Package，回车，在输入Chinese，选择ChineseLocalization 插件，该插件将自动安装。安装完成后一般会自动将程序语言切换为简体中文，也可以在帮助（Help）中的Language下选择语言，目前有简体中文、繁体中文、日语、英语可供选择。(尽量使用英文，否则被阉割)

6.Sublim Text3插件的安装
pylinter：Python基本主题
Terminal：打开一个命令窗口，用于各种命令操作
AutoPep8：python开发规范pep8
Anaconda：自动匹配关键字等实用功能，有效提高开发效率
SublimeREPL：直接运行当前文件，可以方便调试

7.Markdown插件的安装
MarkdownEditing
Markdown编辑器，是Markdown写作者必备的插件，不仅可以高亮显示Markdown语法还支持很多编程语言的语法高亮显示。
特别注意：MarkdownEditing只针对 md\mdown\mmd\txt 格式文件才启用。
特性
MarkdownEditing 从视觉和便捷性上针对 Markdown 文档的编辑进行了一系列的优化。如：
颜色方案仿 Byword及iA writer
自动匹配星号（*）、下划线（_）及反引号（`）
选中文本按下以上符号能自动在所选文本前后添加配对的符号
方便粗体、斜体和代码框的输入
MarkdownLivePreview
功能
实时预览Markdown文件，左侧为md文件，右侧为预览结果。可配合MarkdownEditing一起使用。
使用
MarkdownLivePreview默认关闭实时预览，既然安装这个插件了，那肯定是要用的。打开方式为在Preferences -> Package Settings -> MarkdownLivePreview -> Settings 的设置的右侧加一条 "markdown_live_preview_on_open": true,，重启sublime即可。
为什么不能直接将左侧对应的false改为true，这是因为左侧为默认配置，是不能改的（只读），右侧的编辑区才是用户自定义区。
```


<a id="2.2">**2.2.Linux环境下安装Sublime Text**</a>
**1.下载Sublime Text软件包**
```
<1>.Sublim官方网站下载Sublime Text3安装包官网地址或者百度云盘
[http://www.sublimetext.com/]
或者
[https://www.macbl.com/app/development/sublime-text-3]
<2>.汉化地址：https://github.com/rexdf/ChineseLocalization
```
![](https://www.showdoc.cc/server/api/attachment/visitfile/sign/89094356b31471ebd5fa5803b7d7bba8?showdoc=.jpg)

**2.安装Sublime Text编辑器**
```shell
<1>.解压软件包
$ sudo tar zxvf sublime_text_3_build_3211_x64.tar.bz2  -C /opt

<2>.创建软连接
$ sudo cd /opt/sublime_text_3
$ sudo ln -s /opt/sublime_text_3/sublime_text  /usr/bin/sublime
$ sudo sublime

<3>.建立桌面快捷
$ sudo cp /opt/sublime_text_3/sublime_text.desktop /usr/share/applications
$ sudo cd /usr/share/applications
$ sudo vim sublime_text.desktop

<4>.修改内容如下
$ sudo cp /opt/sublime_text/sublime_text.desktop /usr/share/applications
修改 Icon=/opt/sublime_text_3/Icon/48x48/sublime-text.png
```

**3.安装Sublime Text的License**
```html
<1>.许可证更新地址[https://www.macbl.com/app/development/sublime-text-3]
<2>.Help--->Enter License
```
```html
— BEGIN LICENSE —–
ZYNGA INC.
50 User License
EA7E-811825
927BA117 84C9300F 4A0CCBC4 34A56B44
985E4562 59F2B63B CCCFF92F 0E646B83
0FD6487D 1507AE29 9CC4F9F5 0A6F32E3
0343D868 C18E2CD5 27641A71 25475648
309705B3 E468DDC4 1B766A18 7952D28C
E627DDBA 960A2153 69A2D98A C87C0607
45DC6049 8C04EC29 D18DFA40 442C680B
1342224D 44D90641 33A3B9F2 46AADB8F
—— END LICENSE ——
```
![](https://www.showdoc.cc/server/api/common/visitfile/sign/c34c57e697623996771d30605c9fb5fb?showdoc=.jpg)

**4.Sublime Text编辑器配置Python语言**
```html
<1>.点击"首选项/浏览包"（Reference/Brower Packages），点开之后出来一个目录图形窗口，我们找到python文件夹，如果没有我们新建一个python文件夹

<2>.在python文件夹里，我们再建一个文件命名为 Python.sublime-commands并写入如下配置内容。
{"cmd":["python.exe", "-u", "$file"],
"path":"D:\python3.6",
"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
"selector": "source.python"}

<3>.修改好之后我们点击保存，我们点击"Tools/Bulid System/Python"选择语言

<4>.然后我们回到之前的python文件，我们点击"Tools/Bulid"(快捷键是Ctrl+B,后面就按快捷键了)，可以看到运行的结果
```
**5.安装Package Control（同上）**

<a id="2.3">**2.3.MacOS环境下安装Sublime Text**</a>
```html
后续更新。。。。。。
```

<a id="2.4">**2.4.Sublime Text快捷使用指南**</a>
```html
Sublime Text 使用手册：https://www.w3cschool.cn/sublimetext/
```

---
**作者：张星星**
**昵称：码农青葱**
**时间：2019-07-05 20:30:29 星期五**
**邮箱：8374072892@qq.com**
**声明：此文章结合个人开发经验和部分网络知识总结而成，欢迎网友指正分享转载。**
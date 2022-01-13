**第一部分：PYTHON语言类型**
- <a href="#1.1">**1.1.什么是高级编程语言？**</a>
- <a href="#1.2">**1.2.什么是解释型的语言？**</a>
- <a href="#1.3">**1.3.什么是编译型的语言？**</a>
- <a href="#1.5">**1.4.解释型语言的执行过程以及原理**</a>
- <a href="#1.5">**1.5.编译型语言的执行过程以及原理**</a>
- <a href="#1.4">**1.6.解释型语言和编译型语言的区别**</a>

**第二部分：PYTHON基本概述**
- <a href="#2.1">**2.1.PYTHON的基本概念**</a>
- <a href="#2.2">**2.2.PYTHON的实现版本**</a>
- <a href="#2.3">**2.3.PYTHON的功能特点**</a>
- <a href="#2.4">**2.4.PYTHON的运行机制**</a>
- <a href="#2.5">**2.5.PYTHON的应用领域**</a>
- <a href="#2.6">**2.6.PYTHON的应用公司**</a>

---
<a id="1.1">**1.1.什么是高级编程语言？**</a>
```html
    高级语言（High-level programming language）是一种独立于机器，面向过程或对象的语言。计算机语言具有高级语言和低级语言之分。而高级语言又主要是相对于汇编语言而言的，它是较接近自然语言和数学公式的编程，基本脱离了机器的硬件系统，用人们更易理解的方式编写程序。编写的程序称之为源程序
```
```html
    计算机不能直接的理解高级语言，只能直接理解机器语言，所以必须要把高级语言翻译成机器语言，计算机才能执行高级语言的编写的程序。翻译的方式有两种，一个是编译，一个是解释。两种方式只是翻译的时间不同。
```

<a id="1.2">**1.2.什么是解释型的语言？**</a>
```html
    解释性语言是指它常用的执行机制是使用一个“解释器”来执行，解释器对于程序是一句一句“翻译”成机器语言来一句一句执行，例如Python和Shell就是典型的解释型语言。解释型语言具有独立于平台的一大优势，只要字节码和虚拟机版本一致，就可以在任何平台上运行
```

<a id="1.3">**1.3.什么是编译型的语言？**</a>
```html
    编译型语言是指它常用的执行机制是使用一个“编译器”来编译成机器语言，然后你就可以直接运行（执行）这个编译成的“可执行文件”。例如C语言就是典型的编译型语言。
```

<a id="1.4">**1.4.解释型语言的执行过程以及原理**</a>
```html
   <人类可读的代码>
for (int i=0;i<100;i++)
        |
      字节码（如：pyc文件）
        |
        V
   虚拟机(解释器)
        |
      二进制
        |
        V
      处理器

解释性语言的执行顺序如上流程
```

<a id="1.5">**1.5.编译型语言的执行过程以及原理**</a>
```html
   <人类可读的代码>
for (int i=0;i<100;i++)
        |
      二进制
        |
        V
      处理器

编译性性语言的执行顺序如上流程
```

<a id="1.6">**1.6.解释型语言和编译型语言的区别**</a>
```html
    不管是解释性语言还是编译型都可编译或解释，前提是有这样的编译器或解释器，所谓的“解释性”和“编译”指的是执行机制上的不同。
```
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/bf4227c4d8e02e103ff32ec5dd80cc0a?showdoc=.jpg)

<a id="2.1">**2.1.PYTHON概念介绍**</a>
```html
    PYTHON是一种高级程序设计语言，也称为解释型、动态数据类型、脚本开发语言(胶水语言)。第一个公开发行版发行于1991年，源代码同样遵循GPL(GNU General Public License)协议。官方宣布，2020年1月1日，停止PYTHON2的更新，PYTHON2.7确定为最后一个PYTHON2.X版本。PYTHON3.X并非完全向下兼容，两个大版本之间存在较大差异。
```
<a id="2.2">**2.2.PYTHON实现版本**</a>
```html
    PYTHON的主要实现版本使用C语言编写的，被称为CPython。当人们提到PYTHON时通常指的就是它。随着该语言的不断演化，C语言实现也随着改变。除了C语言实现之外，PYTHON也提供了其他的实现版本，以保持对主流的跟踪。这些实现版本通常比CPython要落后几个版本，但也为PYTHON在特定环境中的使用和宣传提供了巨大的机会。
```
```html
    PYTHON的其他版本中，Jython是PYTHON语言的Java实现版本，它将其代码编译成Java字节码，因此开发人员可以在PYTHON模块中自由的使用Java类；
```
```html
    IronPython将PYTHON引入了.NET环境。该项目是由微软提供支持的，IronPython的主开发人员供职于该公司。他能够在ASP.NET环境中使用，开发人员在.NET应用程序中使用PYTHON代码的方法和在Java环境中使用Jython一样；
```
```html
    PyPY或许是各种实现版本中最有趣的一款，其目标是用PYTHON语言重写PYTHON。在PyPy中，PYTHON解释程序本身就是用PYTHON编写的，PyPy实现版本中，这个C代码层将彻底用纯PYTHON语言重写。PyPy的运行速度远低于CPython。
```
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/187c176f410a32ec65cae402f2d16f01?showdoc=.jpg)

<a id="2.4">**2.4.PYTHON的运行机制**</a>
**1.准备测试文件**
```python
# add_test.py
def add(a, b):
    c = a + b
    print(c)
    return c

# sub_test.py
def sub(a, b):
    c = a - b
    print(c)
    return c

# main.py
from add_test import add
from sub_test import sub


def func():
    print("Hello, world!")


if __name__ == "__main__":
    func()
    add(1, 2)
    sub(2, 1)
```

**2.运行测试文件**
```shell
$ python main.py
> Hello, world!
> 3
> 1

$ ls
> __pycache__/  add_test.py  main.py  sub_test.py

$ cd __pycache__/
$ ls
add_test.cpython-38.pyc  sub_test.cpython-38.pyc

$ vim add_test.cpython-38.pyc
U^M
^@^@^@^@<k`_7^@^@^@ã^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^B^@^@^@@^@^@^@s^L^@^@^@d^@d^A<84>^@Z^@d^BS^@)^Cc^B^@^@^@^@^@^@^@^@^@^@^@^C^@^@^@^B^@^@^@C^@^@^@s^T^@^@^@|^@|^A^W^@}^Bt^@|^B<83>^A^A^@|^BS^@)^AN)^AÚ^Eprint)^CÚ^AaÚ^AbÚ^Ac©^@r^E^@^@^@ú3C:\Users\Administrator\Desktop\pyc_test\add_test.pyÚ^Cadd^A^@^@^@s^F^@^@^@^@^A^H^A^H^Ar^G^@^@^@N)^Ar^G^@^@^@r^E^@^@^@r^E^@^@^@r^E^@^@^@r^F^@^@^@Ú^H<module>^A^@^@^@ó^@^@^@^@
```

```html
	当执行python main.py后，python解释器(Cpython)会将main.py编译成一个字节码对象PyCodeObject，在PYTHON中一切都是对象，PYTHON解释器编译出来的字节码也是对象，而我们看见的.pyc文件其实就是PyChodeObject这个字节对象在硬盘上的表现形式。
```
```html
	当运行PYTHON程序（.py文件）时，我们会发现生成了一种.pyc文件，.pyc文件中存储着PYTHON程序编译后的字节码（字节码并不是机器码，而是可由解释器执行的低级指令集合）。
```
```html
	PYTHON运行机制：首先将.py文件编译成字节码，存储在.pyc文件中（该字节码在虚拟机上运行非cpu）。当PYTHON程序第二次运行时，首先程序会在硬盘中寻找.pyc文件并且修改时间相同，如果找到直接运行，否则重复上述过程。由于引入了字节码，其加载速度比之前的.py文件有所提高，而且还可以实现源码隐藏，一定程度上可以反编译。
```

**3.查看代码字节码**
```html
	我们可以通过dis这个python标准库来获得代码对应的字节码，这些字节码就是PyCodeObject对象中的内容（也是pyc文件中的内容）。之所以要通过dis库是因为pyc文件中存储的是二进制字节数据，无法直接阅读
```
```html
In [1]: import dis

In [2]: dis.dis(lambda x, y, z: (x+y)*z)
  1           0 LOAD_FAST                0 (x) # x进栈
              2 LOAD_FAST                1 (y) # y进栈
              4 BINARY_ADD                     # 栈上的数相加，也就是x与y相加
              6 LOAD_FAST                2 (z) # z进栈
              8 BINARY_MULTIPLY                # 栈上的数相乘，x与y相加的结果与z相乘
             10 RETURN_VALUE                   # 返回值，整个操作就是  (x+y)*z
```
```html
In [6]: main = open("main.py").read()

In [7]: com = compile(main, "main.py", "exec")

In [8]: import dis

In [9]: dis.dis(com)
  1           0 LOAD_CONST               0 (0)
              2 LOAD_CONST               1 (('add',))
              4 IMPORT_NAME              0 (add_test)
              6 IMPORT_FROM              1 (add)
              8 STORE_NAME               1 (add)
             10 POP_TOP

  2          12 LOAD_CONST               0 (0)
             14 LOAD_CONST               2 (('sub',))
             16 IMPORT_NAME              2 (sub_test)
             18 IMPORT_FROM              3 (sub)
             20 STORE_NAME               3 (sub)
             22 POP_TOP

  5          24 LOAD_CONST               3 (<code object func at 0x000001B176417
A80, file "main.py", line 5>)
             26 LOAD_CONST               4 ('func')
             28 MAKE_FUNCTION            0
             30 STORE_NAME               4 (func)

  9          32 LOAD_NAME                5 (__name__)
             34 LOAD_CONST               5 ('__main__')
             36 COMPARE_OP               2 (==)
             38 POP_JUMP_IF_FALSE       66

 10          40 LOAD_NAME                4 (func)
             42 CALL_FUNCTION            0
             44 POP_TOP

 11          46 LOAD_NAME                1 (add)
             48 LOAD_CONST               6 (1)
             50 LOAD_CONST               7 (2)
             52 CALL_FUNCTION            2
             54 POP_TOP

 12          56 LOAD_NAME                3 (sub)
             58 LOAD_CONST               7 (2)
             60 LOAD_CONST               6 (1)
             62 CALL_FUNCTION            2
             64 POP_TOP
        >>   66 LOAD_CONST               8 (None)
             68 RETURN_VALUE

Disassembly of <code object func at 0x000001B176417A80, file "main.py", line 5>:
  6           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('Hello, world!')
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE

```
```html
	上面编译出来的字节码其实也就是12个区块，每个区块都对应着一行代码，main.py总共12行代码。当main.py被PYHON编译器编译后，Python虚拟机会从编译得到的PyCodeObject对象中依次读入每一条字节码指令，在当前的上下文环境中执行这条字节码，PYTHON程序就这样跑起来了。
```

**4.[.pyc]文件的组成部分**
```html
在一个pyc文件中，包含了三部分内容，分别是：
- 1.python的magic number（类似于python版本号）
- 2.pyc文件创建时间信息
- 3.PyCodeObject对象
```
```html
1.magic number是PYTHON定义的一个整数值，一般说，不同版本的python都会定义不同的magic number，目的是保证PYTHON的兼容性。因为不同版本的python生成的字节码可能不同，所以每次python运行时，解释器都要检查magic number是否与当前运行版本python的magic number不同，如果不做检查，python虚拟机执行时就可能会报错

2.pyc文件创建时间信息主要的作用就是判断pyc文件是否需要重新生成，在运行python代码时，如果python发现已经存在相应的pyc，就会去检查对应python文件的修改时间，如果pyc文件的创建时间与python文件的修改时间不同，说明python文件发生了变动，此时就会重新生成pyc文件
```

**5.为什么主文件main.py未生成pyc文件**
```html
在main.py中我们使用了内置属性__name__，python程序在运行时，会自动为每个module都设置__name__属性，通常的作用就是这个module的名字，也就是文件名，唯一的例外就是主module，主module会的__name__会被设置为__main__。
```
```html
利用这个特性，我们可以通过对不同的模块进行测试，当这个模块以主模块运行时，if __name__ == '__main__'下的代码就会执行，而当我们import该模块时，if __name__ == '__main__'下的代码不会执行
```
```html
python只会对那些以后可能会被继续使用和载入的module生成pyc文件，python认为import指令对应的module属于这类，所以myfun.py生成了相应的pyc文件，而那些临时只使用一次的模块不会生成pyc，python将主模块当成这种类型的文件，这也就是main.py不会生成pyc文件的原因
```



<a id="2.5">**2.5.PYTHON功能特点**</a>

```html
    PYTHON主要特点：可读性强；简洁性；面向对象；免费开源；可移植性和跨平台；丰富的库（标准库和扩展库）；可扩展性（胶水式语言）
```
```html
    PYTHON是由C语言开发，但是不再有C语言中指针等复杂数据类型，PYTHON的简洁性，让程序的开发难度和代码幅度大大降低，开发任务大大简化，具有很大开发优势。
```
```html
    PYTHON是动态语言，在C++等静态语言中，必须先声明变量类型，并在编译的时候检查所有的差异，而PYTHON作为弱类型语言，检查变量类型和执行操作的有效性由解释器完成，故PYTHON不用先声明变量。
```
```html
    动态类型提高了代码的自由度，但同时也提高了代码的风险，有时也难以调优
PYTHON经常被指责“速度慢”，因为每一次解释字节码需要许多额外工作
```

<a id="2.6">**2.6.PYTHON应用领域**</a>
```html
    WEB网站开发、数据分析、组件集成、网络服务、图像处理、数值计算、科学计算、云计算、人工智能、爬虫、自动化等应用领域。
```

<a id="2.6">**2.6.PYTHON应用公司**</a>
```html
谷歌：Google App Engine、Google earth 、谷歌爬虫、Google广告等项目都在大量使用Python开发。
```
```html
CIA: 美国中情局网站就是用Python开发的。
```
```html
NASA: 美国航天局(NASA)大量使用Python进行数据分析和运算。
```
```html
Facebook:大量的基础库均通过Python实现的。
```
```html
Dropbox:美国最大的在线云存储网站，全部用Python实现，每天网站处理10亿个文件的上传和下载。
```
```html
Instagram:美国最大的图片分享社交网站，每天超过3千万张照片被分享，全部用python开发。
```
```html
Redhat: 世界上最流行的Linux发行版本中的yum包管理工具就是用Python开发的。
```
```html
豆瓣: 公司几乎所有的业务均是通过Python开发的。
```
```html
春雨医生：国内知名的在线医疗网站是用Python开发的。
```
```html
除上面之外，还有搜狐、金山、腾讯、盛大、网易、百度、阿里、淘宝 、土豆、新浪、果壳等公司都在使用Python完成各种各样的任务。
```

---
**作者：张星星**
**昵称：码农青葱**
**邮箱：8374072892@qq.com**
**声明：此文章结合个人开发经验和部分网络知识总结而成，欢迎网友指正分享转载。**
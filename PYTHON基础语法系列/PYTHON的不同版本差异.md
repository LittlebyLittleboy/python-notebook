<a href='#1'>**①.判断当前版本(sys or platform)**</a>
<a href='#2'>**②.打印输出(print or print())**</a>
<a href='#3'>**③.键盘输入(raw_input() or input())**</a>
<a href='#4'>**④.编码类型(unicode or utf-8)**</a>
<a href='#5'>**⑤.除法取模运算(/ or //)**</a>
<a href='#6'>**⑥.异常捕获(except as or except (a,b...) as)**</a>
<a href='#7'>**⑦.迭代对象(xrange or range)**</a>
<a href='#8'>**⑧.不等运算(<> or !=)**</a>
<a href='#9'>**⑨.数据类型(bytes)**</a>
<a href='#10'>**⑩.多个模块命名变化**</a>

```html
前言：2020年1月1日官方正式抛弃Python2.x版本，拥抱Python3.x版本，今天我们探讨下Python2.x和Python3.x版本的主要语法的区别。
```
<a id='1'>**①.判断当前版本(sys or platform)**</a>

```python
# 方法一
import sys
version_detail = sys.version
version_tuple = sys.version_info
```
```python
# 应用实例
import sys
if sys.version.startswith('3'):
	print('Hello, Python3, World!')
else:
	print 'Hello, Python2, World!'
```

```python
# 方法二
import platform
version_code = platform.platform.python_version()
```
```python
# 应用实例
import platform
if platform.python_version().startswith('3'):
	print('Hello, Python3, World!')
else:
	print 'Hello, Python2, World!'
```

<a id='2'>**②.打印输出(print or print())**</a>
```html
在Python3.x中删掉了[print + 内容]语法打印输出，只能使用[print(内容)]语法打印输出；
py3.x以上版本示例：print('Hello, world.')
```

```html
在Python2.6和Python2.7中已经部分支持[print(内容)]语法打印输出；
py2.6/2.7版本示例：print 'Hello, world.'/print ('Hello, world.')/print('Hello, world.')
```
```html
在Python2.6以下版本中只支持[print + 内容]语法打印输出。
py2.6以下版本示例：print 'Hello, world.'
```

<a id='3'>**③.键盘输入(raw_input() or input())**</a>
```html
在python2.x中raw_input()和input( )，两个函数都存在，其中区别为：<1>.raw_input()：将所有输入作为字符串看待，返回字符串类型
<2>.input()：只能接收"数字"的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（int, float）
```
```html
在python3.x中raw_input()和input( )进行了整合，去除了raw_input()，仅保留了input()函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
```

<a id='4'>**④.编码类型(unicode or utf-8)**</a>
```html
在Python2.x版本中有ASCII str()类型，unicode()是单独的，不是byte类型。
```
```html
在Python3.x中，有了Unicode(utf-8)字符串以及一个字节类(byte和 bytearrays)。
```
```html
Python3.x版本源码文件默认使用utf-8编码，所以使用中文就更加方便了，中文乱码问题得到了解决。
```

<a id='5'>**⑤.除法取模运算(/ or //)**</a>
```html
Python中的除法有两个运算符，/ 和 //两种除法运算。
```
```html
<1>.在Python2.x版本中 / 除法就跟我们熟悉的大多数语言，比如Java和C语言 ，整数相除的结果是一个整数，把小数部分完全忽略掉，浮点数除法会保留小数点的部分得到一个浮点数的结果。
<2>.在Python3.x版本中 / 除法不再这么做了，对于整数之间的相除，结果也会是浮点数，得到实际相除得到的结果，而 // 的功能为两数相除取整。
```
```html
In [1]: 1 / 2
Out[1]: 0

In [2]: 1.0 / 2.0
Out[2]: 0.5
```
```html
In [3]: 1/2
Out[3]: 0.5
```
```html
而对于 // 除法，这种除法叫做向下取整除法，会对除法的结果自动进行一个向下取整操作，在Python2.x版本和Python3.x版本中是一致的。
```
```python
# python2.x
In [1]: 1 // 2
Out[1]: 0

In [2]: -1 // 2
Out[2]: -1
```
```python
# python3.x
In [1]: 1 // 2
Out[1]: 0

In [2]: -1 // 2
Out[2]: -1
```

<a id='6'>**⑥.异常捕获(except as or except (a,b...) as)**</a>
```html
在Python3.x版本中处理异常也轻微的改变了，在Python3.x版本中我们现在使用as作为关键词。捕获异常的语法由 except exc, var 改为 except exc as var。使用语法except (exc1, exc2) as var 可以同时捕获多种类别的异常。在Python2.6过渡版本已经支持这两种语法。
```
```html
1. 在2.x版本中，所有类型的对象都是可以被直接抛出的，在3.x版本中，只有继承自BaseException的对象才可以被抛出。
2. 在2.x版本中，raise语句使用逗号将抛出对象类型和参数分开，3.x版本中取消了这种奇葩的写法，直接调用构造函数抛出对象即可。
```
```html
在2.x版本中，异常在代码中除了表示程序错误，还经常做一些普通控制结构应该做的事情，在3.x版本中可以看出，设计者让异常变的更加专一，只有在错误发生的情况才能去用异常捕获语句来处理。
```

<a id='7'>**⑦.迭代对象(xrange or range)**</a>
```html
在Python2.x版本中xrange()创建迭代对象的用法是非常流行的。比如：for循环或者是列表/集合/字典推导式。这个表现十分像生成器（比如。"惰性求值"）。
```
```html
但是这个 xrange-iterable是无穷的，意味着你可以无限遍历。由于它的惰性求值，如果你不得仅仅不遍历它一次，xrange() 函数 比 range() 更快（比如 for 循环）。尽管如此，对比迭代一次，不建议你重复迭代多次，因为生成器每次都从头开始。
```
```html
在Python3.x版本中，range()是像xrange()那样实现以至于一个专门的xrange()函数都不再存在（在Python3.x版本中xrange()会抛出命名异常）。
```

Python 2.x示例
```python
import timeit

n = 10000
def test_range(n):
    return for i in range(n):
        pass

def test_xrange(n):
    for i in xrange(n):
        pass   
```
```python
print 'Python', python_version()

print '\ntiming range()' 
%timeit test_range(n)

print '\n\ntiming xrange()' 
%timeit test_xrange(n)

Python 2.7.6

timing range()
1000 loops, best of 3: 433 µs per loop


timing xrange()
1000 loops, best of 3: 350 µs per loop
```

Python 3.x示例
```python
print('Python', python_version())

print('\ntiming range()')
%timeit test_range(n)

Python 3.4.1

timing range()
1000 loops, best of 3: 520 µs per loop
print(xrange(10))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-5-5d8f9b79ea70> in <module>()
----> 1 print(xrange(10))

NameError: name 'xrange' is not defined
```

<a id='8'>**⑧.不等运算(<> or !=)**</a>
```html
在Python2.x版本中不等于有两种写法 != 和 <>
```
```html
在Python3.x中去掉了<>, 只有!=这一种写法
```

<a id='9'>**⑨.数据类型(bytes)**</a>
```html
1）Py3.X去除了long类型，现在只有一种整型——int，但它的行为就像2.X版本的long
2）新增了bytes类型，对应于2.X版本的八位串，定义一个bytes字面量的方法如下：

In [1]: b = b'china'
In [2]: type(b)
Out[2]: <type 'bytes'>
```
```html
str对象和bytes对象可以使用.encode() (str -> bytes) 或 .decode() (bytes -> str)方法相互转化。

In [3]: s = b.decode()
In [4]: s
Out[4]: 'china'

In [5]: b1 = s.encode()
In [6]: b1
Out[6]: b'china'
```

<a id='10'>**⑩.多个模块命名变化**</a>
```html
python2.x---------->python3.x
_winreg             winreg
ConfigParser        configparser
copy_reg            copyreg
Queue               queue
SocketServer        socketserver
repr                reprlib
```
```html
python2.x中的StringIO模块现在被合并到新的io模组内。python2.x中的new, md5, gopherlib等模块被删除。 Python 2.6已经支援新的io模组。
```
```html
python2.x中的httplib, BaseHTTPServer, CGIHTTPServer, SimpleHTTPServer, Cookie, cookielib被合并到http包内。
```
```html
python3.x取消了exec语句，只剩下exec()函数。 Python 2.6已经支持exec()函数。
```

---
**作者：张星星**
**昵称：码农青葱**
**邮箱：8374072892@qq.com**
**声明：此文章结合个人开发经验和部分网络知识总结而成，欢迎网友指正分享转载。**
**第一部分：主流编码类型**
- <a href="#1.1">**1.1.ASCII编码**</a>
- <a href="#1.2">**1.2.Unicode编码**</a>
- <a href="#1.3">**1.3.UTF-8编码**</a>
- <a href="#1.4">**1.4.GBK编码**</a>

**第二部分：编码兼容问题**
- <a href="#2.1">**2.1.PYTHON的编码格式**</a>
- <a href="#2.2">**2.2.PYTHON的编码问题**</a>
- <a href="#2.3">**2.3.PYTHON编码的兼容方法**</a>
- <a href="#2.4">**2.4.PYTHON字符串编码问题**</a>

---
<a id="1.1">**1.1.ASCII编码**</a>
```html
	ASCII只有127个字符，表示英文字母的大小写、数字和一些符号，一个字符用8位(bit)即1字节(byte)表示，如：A(65)，Z(90)，a(97)，z(122)。但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以中国制定了GB2312编码，用来把中文编进去，同样其他国家的语言也有属于自己的编码格式。
```

<a id="1.2">**1.2.Unicode编码**</a>
```html
	由于每个国家的语言都有属于自己的编码格式，在多语言编辑文本中会出现乱码，这样Unicode即万国码应运而生，Unicode就是将这些语言统一到一套编码格式中，通常两个字节表示一个字符，而ASCII是一个字节表示一个字符，这样如果你编译的文本是全英文的，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。
```

<a id="1.3">**1.3.UTF-8编码**</a>
```html
	为了节省空间又出现了把Unicode编码转化为“可变长编码”的UTF-8编码，UTF-8编码将Unicode字符按数字大小编码为1-6个字节，英文字母被编码成1个字节，常用汉字被编码成3个字节，如果你编译的文本是纯英文的，那么用UTF-8就会非常节省空间，并且ASCII码也是UTF-8的一部分。
```

<a id="1.4">**1.4.GBK编码**</a>
```html
	国标码，只包含英文字符和自己国家的字符，用8位(bit)1字节(byte)表示英文字符，用16位(bit)2字节(byte)表示中文字符。
```

```html
计算机系统通用的字符编码工作方式
(1)在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
(2)用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件。
```
[![](https://www.showdoc.cc/server/api/common/visitfile/sign/0eac0dea2efbf98db87646f085ff53d6?showdoc=.jpg)]()


```html
字母A用ASCII编码是十进制的65，二进制的01000001；
字符0用ASCII编码是十进制的48，二进制的00110000；
```
```html
汉字'中'已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101;

如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 00110000;

如果把ASCII编码的0用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001;
```
```html
▷1位 = 1bit
▷8bits = 1bytes = 1字节
▷1024bytes = 1KB
▷1024KB = 1MB
▷1024MB = 1GB
▷1024GB = 1TB
```

<a id="2.1">**2.1.PYTHON的编码格式**</a>
```html
PYTHON2.x默认使用ASCII编码，PYTHON3.x默认使用UTF-8编码
```
```html
# 查看当前版本的编码格式
import sys
encode_type = sys.getdefaultencoding()
```

<a id="2.2">**2.2.PYTHON的编码问题**</a>
```python
# python2_test.py

message = "Hello, China!"
print(message)
print(len(message))

message = "你好，中国！"
print(message)
print(len(message))

# 报错如下：
"""
File "python2_test.py", line 5
SyntaxError: Non-ASCII character '\xe4' in file py2_test.py on line 5, 
but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
"""

# 报错原因：
"""
PYTHON2默认ASCII编码格式，也就是默认使用ASCII编码格式将代码读入内存，由于ASCII码中没有中文字符导致报错。
"""
```
```python
# python3_test.py

message = "Hello, China!"
print(message)
print(len(message))

message = "你好，中国！"
print(message)
print(len(message))

# 结果：
"""
Hello, China!
13
你好，中国！
18
"""
# 说明：
"""
PYTHON3默认UTF-8编码格式，也就是默认使用UTF-8编码格式将代码读入内存，由于UTF-8是可变的Unicode编码，所以可以读取中文和英文。
"""
```

```python
# -*- coding: utf-8 -*-
message = "Hello, China!"
print(message)
print(len(message))

message = "你好，中国！"
print(message)
print(len(message))

# 结果：
"""
Hello, China!
13
你好，中国！
18
"""
```

<a id="2.3">**2.3.PYTHON编码的兼容方法**</a>
**①.编码问题分析**
```html
PYTHON2.X开发环境：输出 "Hello, World!"，英文没有问题，但是如果你输出中文字符 "你好，世界" 就有可能会碰到中文编码问题。
```
```html
报错产生：如果在我们的PY脚本程序中存在中文，运行文件时会报错；如果不含有中文就不会出现问题。
```
```html
原因分析：PYTHON2.X中默认的编码格式是ASCII 格式，在没修改编码格式时无法正确打印输出汉字，所以在读取中文时会报错。
```
```html
处理方法：只要在文件开头加入 # -*- coding: UTF-8 -*-或者# coding=utf-8，注意：# coding=utf-8的'='号两边不要空格。
```
```html
注意事项：Python3.X 源码文件默认使用utf-8编码，所以可以正常解析中文，无需指定 UTF-8 编码。另外如果你使用编辑器，同时需要设置python文件存储的格式为UTF-8，否则会出现类似错误信息。
```
```html
Pycharm设置步骤：进入 file > Settings，在输入框搜索 encoding。找到 Editor > File encodings，将 IDE Encoding 和 Project Encoding 设置为utf-8。
```
**②.编码问题处理**
```html
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：
```

<a id="2.4">**2.4.PYTHON字符串编码问题**</a>
**①.python2.x和python3.x中文输出的对比**
```html
# python2的中文输出
python2_string = u'中国'
print(python2_string)

# python3的中文输出
python3_string = '中国'
print(python3_string)
```
```html
代码分析：在Python2.x中，字符串是以ASCII编码形式读到内存中，由于ASCII码长度不足以读取到中文字符，则需要转码为Unicode编码后读到内存中；在Python3.x中，字符串是以Unicode编码读到内存中的，即字符串支持多语言。
```

**②.单个字符的ASCII/Unicode编码转换**
```html
# 单个字符的编码转换
<1>.ord()函数获取字符的整数形式表示
ord('A')
ord('a')
ord('中')
ord('国')
<2>.chr()函数把编码转换为对应的字符
chr(65)
chr(97)
chr(20013)
chr(22269)
<3>.已知字符整数编码十六进制表示中文
s = '\u4e2d\u56fd' -> 中国
```

**③.str类型和bytes类型的对比**
```html
基础理论：在Python中字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。bytes类型的数据用带b前缀的单引号或双引号表示。
```
```html
s1 = 'hello'
print(s1)
s2 = b'hello'
print(s2)
```
```html
代码分析：前者s1是str类型，后者s2是bytes类型，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
```

**④.str类型和bytes类型的转换**
```html
基础理论：Unicode表示的str字符串通过encode()方法可以编码为指定的bytes。
```
```html
s1 = 'hello'.encode('utf8')
# > b'hello'

s2 = 'hello'.encode('ascii')
# > b'hello'

c_bytes1 = '中国'.encode('utf8')
# > b'\xe4\xb8\xad\xe5\x9b\xbd'

c_tytes2 = '中国'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```
```html
代码说明：英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，解释器会报错。另外在bytes中，无法显示为ASCII字符的字节，用\x##显示。
```

```html
基础理论：如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。就需要用decode()方法把bytes变为str。
```
```html
s1 = b'hello'.decode('ascii')
# > 'hello'
s2 = b'hello'.decode('utf-8')
# > 'hello'
s3 = b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf-8')
# > '中国'
s4 = b'\xe4\xb8\xad\xe5\x9b\xbd\xff'.decode('utf-8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 6: invalid start byte
```
```html
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
s = b'\xe4\xb8\xad\xe5\x9b\xbd\xff'.decode('utf-8', errors='ignore')
# > '中国'
```

****⑤.str类型和bytes类型的长度****

```html
基础理论：str包含多少个字符，可以用len()函数，len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数.
```
```html
s_len = len('hello')
# > 5
b_len = len(b'hello')
# > 5
c_len = len(b'\xe4\xb8\xad\xe5\x9b\xbd')
# > 6
c_len= len('中国'.encode('utf-8'))
# > 6
```
```html
代码分析：1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
```
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/465e1e25aea062cd62a0fed9834f87da)

---
**作者：张星星**
**昵称：码农青葱**
**邮箱：8374072892@qq.com**
**声明：此文章结合个人开发经验和部分网络知识总结而成，欢迎网友指正分享转载。**
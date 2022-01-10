**第一节：Pandas基础概念**

- <a href="#1.1">**1.1.Pandas基本介绍**</a>
- <a href="#1.2">**1.2.Pandas功能特点**</a>
- <a href="#1.3">**1.3.Pandas部分优势**</a>
- <a href="#1.4">**1.4.Pandas实例分析**</a>
---

<a id="1.1">**1.1.Pandas基本介绍**</a>

> Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

> Pandas是一个开源、基于BSD协议的库，为Python语言项目提供高性能、易用数据类型。Pandas基于Numpy实现，经常与Numpy和Matplotlib结合起来一同使用。

> Pandas[Python Data Analysis]的缩写，是Python中基于Numpy和Matplotlib的第三方数据分析库，与后两者共同构成了Python数据分析的基础工具包，享有数据分析三剑客之名。

> 正因为Pandas是在Numpy基础上实现，其核心数据结构与Numpy的ndarray十分相似，但Pandas与Numpy的关系不是替代，而是互为补充。

```html
Pandas是一个强大的分析结构化数据的工具集；它的使用基础是Numpy（提供高性能的矩阵运算）；用于数据挖掘和数据分析，同时也提供数据清洗功能。
```
```html
```
Pandas速度很快。Pandas的很多底层算法都用Cython优化过。然而，为了保持通用性，必然要牺牲一些性能，如果专注某一功能，完全可以开发出比 Pandas 更快的专用工具。



<a id="1.2">**1.2.Pandas功能特点**</a>

- 按索引匹配的广播机制，这里的广播机制与Numpy广播机制还有很大不同
- 常用的数据分析与统计功能，丰富的时间序列向量化处理接口，包括基本统计量、分组统计分析等
- 集成Matplotlib的常用可视化接口，无论是series还是dataframe，均支持面向对象的绘图接口
- 便捷的数据读写操作，相比于Numpy仅支持数字索引，pandas的两种数据结构均支持标签索引，包括bool索引也是支持的
- 类比Excel的数据透视表功能，Excel中最为强大的数据分析工具之一是数据透视表，这在pandas中也可轻松实现
- 自带正则表达式的字符串向量化操作，对pandas中的一列字符串进行通函数操作，而且自带正则表达式的大部分接口
- 类比SQL的join和groupby功能，Pandas可以很容易实现SQL这两个核心功能，实际上SQL的绝大部分DQL和DML操作在Pandas中都可以实现

- **从数据结构上看：**
	- Numpy的核心数据结构是ndarray，支持任意维数的数组，但要求单个数组内所有数据是同质的，即类型必须相同；而Pandas的核心数据结构是series和dataframe，仅支持一维和二维数据，但数据内部可以是异构数据，仅要求同列数据类型一致即可。
	- Numpy的数据结构仅支持数字索引，而Pandas数据结构则同时支持数字索引和标签索引。

- **从功能定位上看：**
	- Numpy虽然也支持字符串等其他数据类型，但仍然主要是用于数值计算，尤其是内部集成了大量矩阵计算模块，例如基本的矩阵运算、线性代数、fft、生成随机数等，支持灵活的广播机制。
	- Pandas主要用于数据处理与分析，支持包括数据读写、数值计算、数据处理、数据分析和数据可视化全套流程操作。

<a id="1.3">**1.3.Pandas部分优势**</a>

- 处理浮点与非浮点数据里的缺失数据，表示为NaN；
- 大小可变：插入或删除DataFrame等多维对象的列；
- 自动、显式数据对齐：显式地将对象与一组标签对齐，也可以忽略标签，在Series、DataFrame计算时自动与数据对齐；
- 强大、灵活的分组（group by）功能：拆分-应用-组合数据集，聚合、转换数据；
- 把Python和NumPy数据结构里不规则、不同索引的数据轻松地转换为DataFrame对象；
- 基于智能标签，对大型数据集进行切片、花式索引、子集分解等操作；
- 直观地合并（merge）、**连接（join）**数据集；
- 灵活地重塑（reshape）、**透视（pivot）**数据集；
- 轴支持结构化标签：一个刻度支持多个标签；
- 成熟的IO工具：读取文本文件（CSV 等支持分隔符的文件）、Excel文件、数据库等来源的数据，利用超快的HDF5格式保存/加载数据；
- 时间序列：支持日期范围生成、频率转换、移动窗口统计、移动窗口线性回归、日期位移等时间序列功能。

<a id="1.4">**1.4.Pandas实例分析**</a>
```python
```
# Pandas样例分析
import pandas as pd
# 创建一个一维Series
series = pd.Series(range(10))
print(series, type(series))
```html
......
In [10]: print(series, type(series))
0    0
1    1
2    2
3    3
```
9    9
dtype: int64 <class 'pandas.core.series.Series'>

```python
```
# Pandas样例分析
import pandas as pd
# 创建一个二维Dataframe
dataframe =  pd.DataFrame(data=[['Jack', 18], ['Rose', 20]], columns=['name', 'age'])
print(dataframe, type(dataframe))
```html
```
In [11]: print(dataframe, type(dataframe))
   name  age
0  Jack   18
1  Rose   20 <class 'pandas.core.frame.DataFrame'>

参考文档：

[Pandas中文教程](https://www.pypandas.cn/docs/getting_started/overview.html#%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)
[公众号小志数据](https://mp.weixin.qq.com/s/OHflBhjPj46GT5t1532cnw)

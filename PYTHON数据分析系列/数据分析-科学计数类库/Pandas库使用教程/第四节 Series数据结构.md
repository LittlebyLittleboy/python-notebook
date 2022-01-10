**第四节 Series数据结构**
- <a href="#1.1">**1.1.Series结构原理**</a>
- <a href="#1.2">**1.2.Series对象创建**</a>
- <a href="#1.3">**1.3.Series功能特点**</a>
- <a href="#1.4">**1.4.Series对象属性**</a>
- <a href="#1.5">**1.5.Series接口方法**</a>

---
<a id="1.1">**1.1.Series结构原理**</a>

> Series是带标签的一维数组，可存储整数、浮点数、字符串、Python对象等类型的数据，轴标签统称为索引。即Series类型是由一组数据及与之相关数据的索引组成。

```html
# 数据结构
	索   引 ---> 数  据
	index_0 ---> data_a
	index_1 ---> data_b
	index_2 ---> data_c
	index_3 ---> data_d
```

<a id="1.2">**1.2.Series对象创建**</a>
```html
# Series创建接口函数
	名称： pandas.Series
	功能： 创建一维Series序列
	语法： pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
	参数：
		   - data : array-like, dict, or scalar value（多维数组, 列表，字典, 或标量值）
		   - index : array-like or Index (1d)（一维轴标签列表，默认None）
		   - dtype : numpy.dtype or None（数据类型，NumPy数据类型或None）
		   - name：str, optional（给Series定义名称）
		   - copy : boolean, default False（是否复制，布尔类型，默认为False）
```
```python
# 导入numpy和pandas模块
import string
import numpy as np 
import pandas as pd 
```
```python
"""
功能：从多维数组创建Series数据对象
特点：data是多维数组时，index长度必须与data长度一致。没有指定index参数时，创建数值型索引，即[0, ..., len(data) - 1]。
报错：当index长度与data长度不一致，ValueError: Length of passed values is 3, index implies 2.
"""
array_series = pd.Series(data=np.random.randn(3), index=['a', 'b', 'c'])
```
```html
In [5]: print(array_series, type(array_series))
a   -0.021449
b   -0.011615
c    0.900459
dtype: float64 <class 'pandas.core.series.Series'>
```
```python
array_series = pd.Series(data=np.random.randn(3))
```
```html
In [30]: print(array_series, type(array_series))
0    0.279323
1    1.296261
2    1.096373
dtype: float64 <class 'pandas.core.series.Series'>
```

```python
"""
功能：从列表创建Series数据对象
特点：data是列表时，index长度必须与data长度一致。没有指定index参数时，创建数值型索引，即[0, ..., len(data) - 1]。
报错：当index长度与data长度不一致，ValueError: Length of passed values is 3, index implies 2.
"""
list_series = pd.Series(data=[1, 3, 5], index=list(string.ascii_uppercase[:3]), dtype=np.float64)
```
```html
In [9]: print(list_series, type(list_series))
A    1.0
B    3.0
C    5.0
dtype: float64 <class 'pandas.core.series.Series'>
```
```python
list_series = pd.Series(data=[1, 3, 5], dtype=np.float64)
```
```html
In [32]: print(list_series, type(list_series))
0    1.0
1    3.0
2    5.0
dtype: float64 <class 'pandas.core.series.Series'>
```

```python
"""
功能：从字典创建Series数据对象
特点：data是字典时，index长度可以与data长度不一致。没有指定index参数时，直接使用字典的键做为index标签。
指定标签是要和字典的键保持相同，相当于通过键获取数据，标签长度大于字典长度时填充NAN，反之数据长度等于标签长度。
"""
dict_series = pd.Series(data={'a':1.0, 'b':2.2, 'c':3.3}, index=['a', 'b', 'c'], dtype=np.float64)
```
```html
In [28]: print(dict_series, type(dict_series))
a    1.0
b    2.2
c    3.3
dtype: float64 <class 'pandas.core.series.Series'>
```
```python
dict_series = pd.Series(data={'a':1.0, 'b':2.2, 'c':3.3}, dtype=np.float64)
```
```html
In [28]: print(dict_series, type(dict_series))
a    1.0
b    2.2
c    3.3
dtype: float64 <class 'pandas.core.series.Series'>
```
```python
dict_series = pd.Series(data={'a':1.0, 'b':2.2, 'c':3.3}, index=['a', 'b'], dtype=np.float64)
```
```html
In [41]: print(dict_series, type(dict_series))
a    1.0
b    2.2
c    3.3
d    NaN
dtype: float64 <class 'pandas.core.series.Series'>
```
> 注意:Pandas 用 NaN（Not a Number）表示缺失数据。


```python
"""
功能：从标量创建Series数据对象
特点：data是标量值时，必须提供索引。Series按索引长度重复该标量值。
"""
const_series = pd.Series(data=5., index=['a', 'b', 'c'], dtype=np.float64)
```
```html
In [44]: print(const_series, type(const_series))
a    5.0
b    5.0
c    5.0
dtype: float64 <class 'pandas.core.series.Series'>
```

<a id="1.3">**1.3.Series功能特点**</a>
```html
Series类似多维数组: Series操作与ndarray类似，支持大多数NumPy函数，还支持索引切片。
```
```python
import string
import numpy as np
import pandas as pd

s = pd.Series(data=np.random.randn(10), index=list(string.ascii_uppercase[:10]), dtype=np.float64)
```
```html
In [13]: s[0]
Out[13]: 0.4691122999071863

In [14]: s[:3]
Out[14]: 
a    0.469112
b   -0.282863
c   -1.509059
dtype: float64

In [15]: s[s > s.median()]
Out[15]: 
a    0.469112
e    1.212112
dtype: float64

In [16]: s[[4, 3, 1]]
Out[16]: 
e    1.212112
d   -1.135632
b   -0.282863
dtype: float64

In [17]: np.exp(s)
Out[17]: 
a    1.598575
b    0.753623
c    0.221118
d    0.321219
e    3.360575
dtype: float64
```

```html
Series类似字典: Series类似固定大小的字典，可以用索引标签提取值或设置值。
```
```python
import string
import numpy as np
import pandas as pd

s = pd.Series(data={index: np.random.random() for index in string.ascii_lowercase[:10]}, index=list(string.ascii_lowercase[:10]), dtype=np.float64)
```
```html
In [85]: s
Out[85]:
a    0.230574
b    0.341985
c    0.014964
.............
h    0.934682
i    0.358530
j    0.016448
dtype: float64

In [86]: s['a']
Out[86]: 0.23057440629043668

In [87]: s['e']
Out[87]: 0.4095823236680498

In [88]: 'd' in s
Out[88]: True

In [89]: 'k' in s
Out[89]: False

In [27]: s.get('f', np.nan)
Out[27]: nan
```
```html
Series矢量计算: Series和NumPy数组一样，都不用循环每个值，而且Series支持大多数NumPy多维数组的方法。
```
```python
import string
import numpy as np
import pandas as pd

s = pd.Series(data={index: np.random.random() for index in string.ascii_lowercase[:10]}, index=list(string.ascii_lowercase[:10]), dtype=np.float64)
```
```html
In [90]: s + s
Out[90]:
a    0.461149
b    0.683971
.............
h    1.869364
i    0.717061
j    0.032896
dtype: float64

In [91]: s * 2
Out[91]:
a    0.461149
b    0.683971
.............
i    0.717061
j    0.032896
dtype: float64

In [92]: np.exp(s)
Out[92]:
a    1.259323
b    1.407740
.............
i    1.431225
j    1.016584
dtype: float64
```

<a id="1.4">**1.4.Series对象属性**</a>
```html

```
<a id="1.5">**1.5.Series接口方法**</a>
```html

```



参考文档：

[Pandas中文教程](https://www.pypandas.cn/docs/getting_started/dsintro.html#series)
[Pandas接口教程](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html?highlight=series#pandas.Series)
[公众号小志数据](https://mp.weixin.qq.com/s/OHflBhjPj46GT5t1532cnw)
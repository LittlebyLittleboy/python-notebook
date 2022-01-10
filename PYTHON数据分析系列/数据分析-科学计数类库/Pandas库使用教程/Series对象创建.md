**Series对象创建**
- <a href="#1.1">**1.1.Series结构原理**</a>
- <a href="#1.2">**1.2.Series创建接口**</a>
- <a href="#1.3">**1.3.Series来源数组**</a>
- <a href="#1.4">**1.4.Series来源列表**</a>
- <a href="#1.5">**1.5.Series来源字典**</a>
- <a href="#1.6">**1.6.Series来源标量**</a>
- <a href="#1.7">**1.7.Series类似数组**</a>
- <a href="#1.8">**1.8.Series类似字典**</a>
- <a href="#1.9">**1.9.Series矢量计算**</a>

---
<a id="1.1">**1.1.Series结构原理**</a>
```html
Series是带标签的一维数组，可存储整数、浮点数、字符串、对象等类型的数据，轴标签统称为索引。
```
```html
          index     data    axis=1
         —— —— —— —— —— —— —— —— —— ——>
        | index0--->data_a
        | index1--->data_b
        | index2--->data_c
axis=0  | index3--->data_d
        | ................
        | indexn--->data_x
        V

index: 标签，data: 数据，axis：轴向，0代表纵轴，1代表横轴
```

<a id="1.2">**1.2.Series创建接口**</a>
```html
接口：pandas.Series
语法：pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
功能：具有轴标签(包括时间序列)的一维数组。
参数：
    - data：array-like, dict, or scalar value（数组, 列表，字典, 或标量值，默认值为None）
    - index：array-like or Index (1d)（一维轴标签列表，默认值为None）
    - dtype：numpy.dtype or None（数据类型，NumPy数据类型或None，默认值为None）
    - name：str, optional（给Series定义名称，默认值为None）
    - copy：boolean, default False（是否复制，布尔类型，默认为False）
```

<a id="1.3">**1.3.Series来源数组**</a>
```python
"""
功能：当数据来源data为一维数组时获取Series对象。
特点：index长度必须与data长度一致。
    - 当指定index标签列表时，index长度必须与data长度一致，否则程序会报错。
    - 当不指定index标签列表时，默认创建数值型索引，即[0, ..., len(data) - 1]。
"""

array_series = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]))
print(array_series, type(array_series))
array_series = pd.Series(data=np.random.randn(3))
print(array_series, type(array_series))
```
```html
a    0.348622
b    0.071211
c   -1.400806
dtype: float64 <class 'pandas.core.series.Series'>
0    0.375085
1    0.817804
2    0.858395
dtype: float64 <class 'pandas.core.series.Series'>
```

<a id="1.4">**1.4.Series来源列表**</a>
```python
"""
功能：当数据来源data为列表时获取Series对象。
特点：index长度必须与data长度一致。
    - 当指定index标签列表时，index长度必须与data长度一致，否则程序会报错。
    - 当不指定index标签列表时，默认创建数值型索引，即[0, ..., len(data) - 1]。
"""

list_series = pd.Series(data=[1, 3, 5], index=list(string.ascii_lowercase[:3]))
print(list_series, type(list_series))
list_series = pd.Series(data=[1, 3, 5])
print(list_series, type(list_series))
```
```html
a    1
b    3
c    5
dtype: int64 <class 'pandas.core.series.Series'>
0    1
1    3
2    5
dtype: int64 <class 'pandas.core.series.Series'>
```

<a id="1.5">**1.5.Series来源字典**</a>
```python
"""
功能：当数据来源data为字典时获取Series对象。
特点：index长度可以与data长度不一致。
    - 当指定index标签列表时，指定标签要和字典的键保持相同的值。
        - 当标签长度大于字典长度时，数据默认填充NAN
        - 当标签长度小于字典长度时，不加载无对应标签的数据
    - 当不指定index标签列表时，默认使用字典的键做为index标签。
注意：Pandas用NaN（Not a Number）表示缺失数据。
"""

dict_series = pd.Series(data={'a':1.0, 'b':2.2, 'c':3.3}, index=['a', 'b', 'c'], dtype=np.float64)
print(dict_series, type(dict_series))
dict_series = pd.Series(data={'a':1.0, 'b':2.2, 'c':3.3}, dtype=np.float64)
print(dict_series, type(dict_series))
dict_series = pd.Series(data={'a':1.0, 'b':2.2, 'c':3.3}, index=['a', 'b'], dtype=np.float64)
print(dict_series, type(dict_series))
```
```html
a    1.0
b    2.2
c    3.3
dtype: float64 <class 'pandas.core.series.Series'>
a    1.0
b    2.2
c    3.3
dtype: float64 <class 'pandas.core.series.Series'>
a    1.0
b    2.2
c    3.3
d    NaN
dtype: float64 <class 'pandas.core.series.Series'>
```

<a id="1.6">**1.6.Series来源标量**</a>
```python
"""
功能：当数据来源data为标量时获取Series对象。
特点：当data是标量值时，必须提供索引。Series按索引长度重复该标量值。
"""
const_series = pd.Series(data=5., index=['a', 'b', 'c'], dtype=np.float64)
print(const_series, type(const_series))
```
```html
a    5.0
b    5.0
c    5.0
dtype: float64 <class 'pandas.core.series.Series'>
```

<a id="1.7">**1.7.Series类似数组**</a>
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

<a id="1.8">**1.8.Series类似字典**</a>
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

<a id="1.9">**1.9.Series矢量计算**</a>
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

---
**参考文档**
[**Pandas中文教程**](https://www.pypandas.cn/docs/getting_started/dsintro.html#series)
[**Pandas接口教程**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html?highlight=series#pandas.Series)
[**公众号小志数据**](https://mp.weixin.qq.com/s/OHflBhjPj46GT5t1532cnw)

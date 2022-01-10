**Series属性访问**
- <a href="#1.1">**1.1.Series固定属性**</a>
- <a href="#1.2">**1.2.Series属性方法**</a>

---
<a id="1.1">**1.1.Series固定属性**</a>

|固定属性|功能描述|
|---|---|
|Series.array|返回支持该Series或Index的数据的ExtensionArray扩展数组|
|Series.values|返回根据dtype将Series返回为ndarray或类似ndarray的形式。|
|Series.index|返回Series的索引（轴标签）。|
|Series.dtype|返回基础数据的dtype对象。|
|Series.dtypes|返回基础数据的dtype对象。|
|Series.ndim|返回基础数据的维数1。|
|Series.shape|返回基础数据形状的元组。|
|Series.size|返回基础数据中的元素数。|
|Series.axes|返回行轴标签的列表。|
|Series.nbytes|返回基础数据中的字节数。|
|Series.T|返回转置，根据定义，转置为本身。|
|Series.hasnans|如果我有nans，请返回；启用各种性能提升。|
|Series.is_unique|如果对象中的值唯一，则返回布尔值。|
|Series.empty|返回Series数据是否为空。|

**<1>.Series.array**
```
"""
功能：返回支持该Series或Index的数据的ExtensionArray扩展数组
说明：0.24.0版中的新功能。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.array)
```
```html
Out[6]: <PandasArray>
[0.469112, 1.40383557, -1.20443032]
Length: 3, dtype: float64
```

**<2>.Series.values**
"""
功能：返回根据dtype将Series返回为ndarray或类似ndarray的形式。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.values)
```
```html
Out[6]: [ 1.40383557 -1.20443032 -1.24502045]
```

**<3>.Series.index**
"""
功能：返回Series的索引（轴标签）。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.index)
```
```html
Out[6]: Index(['a', 'b', 'c'], dtype='object')
```

**<4>.Series.dtype/dtypes**
"""
功能：返回基础数据的dtype对象。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.dtype)
s = pd.Series(data=[1, "v", 2.2], index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.dtypes)
```
```html
Out[6]: float64
Out[6]: object
```

**<5>.Series.ndim**
"""
功能：返回基础数据的维数1。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.values)
```
```html
Out[6]: 1
```

**<6>.Series.shape**
"""
功能：返回基础数据形状的元组。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.shape)
```
```html
Out[6]: (3,)
```

**<7>.Series.size**
"""
功能：返回基础数据中的元素数。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.size)
```
```html
Out[6]: 3
```

**<8>.Series.axes**
"""
功能：返回行轴标签的列表。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.axes)
```
```html
Out[6]: [Index(['a', 'b', 'c'], dtype='object')]
```

**<9>.Series.nbytes**
"""
功能：返回基础数据中的字节数。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.nbytes)
```
```html
Out[6]: 24
```

**<10>.Series.T**
"""
功能：返回转置，根据定义，转置为本身。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.T)
```
```html
Out[6]: 
a    2.791213
b    0.175730
c    1.321150
dtype: float64
```

**<11>.Series.hasnans**
"""
功能：如果我有nans，请返回；启用各种性能提升。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.hasnans)
```
```html
Out[6]: False
```

**<12>.Series.is_unique**
"""
功能：如果对象中的值唯一，则返回布尔值。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.is_unique)
```
```html
Out[6]: True
```

**<13>.Series.empty**
"""
功能：返回Series数据是否为空。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.empty)
```
```html
Out[6]: True
```

<a id="1.2">**1.2.Series属性方法**</a>

|属性方法|功能描述|
|---|---|
|Series.loc|通过标签或布尔数组访问一组行和列。|
|Series.iloc|基于位置的纯基于整数位置的索引。|
|Series.at|访问行/列标签对的单个值。|
|Series.iat|通过整数位置访问行/列对的单个值。|


**<1>.Series.loc**
"""
功能：通过标签或布尔数组访问一组行和列。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.loc['a'])
 print(s.loc[['a','b']])
```
```html
Out[6]: -0.42845055380450714
Out[6]: 
a    1.140748
b    0.816493
dtype: float64
```

**<2>.Series.iloc**
"""
功能：基于位置的纯基于整数位置的索引。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.iloc[0])
print(s.iloc[[0,1]])
```
```html
Out[6]: 0.21868934127283207
Out[6]: 
a    0.218689
b   -0.174536
dtype: float64
```

**<3>.Series.at**
"""
功能：访问行/列标签对的单个值。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.at['a'])
```
```html
Out[6]: -0.42845055380450714
```

**<4>.Series.iat**
"""
功能：基于位置的纯基于整数位置的索引。
"""
s = pd.Series(data=np.random.randn(3), index=list(string.ascii_lowercase[:3]), dtype=np.float64)
print(s.iat[0])
```
```html
Out[6]: 0.21868934127283207
```

---
**参考文档**
[**Pandas中文教程**](https://www.pypandas.cn/docs/getting_started/dsintro.html#series)
[**Pandas接口教程**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html?highlight=series#pandas.Series)
[**公众号小志数据**](https://mp.weixin.qq.com/s/OHflBhjPj46GT5t1532cnw)



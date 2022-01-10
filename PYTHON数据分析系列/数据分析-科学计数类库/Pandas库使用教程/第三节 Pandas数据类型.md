**第三节：Pandas数据类型**
- <a href="#1.1">**1.1.Pandas数据结构介绍**</a>
- <a href="#1.2">**1.2.Pandas数据结构对比**</a>

---
<a id="1.1">**1.1.Pandas数据结构介绍**</a>
```html
Pandas的核心数据结构是Series(一维数据)与DataFrame(二维数据)，二者可以分别看做是在NumPy一维数组和二维数组的基础上增加了相应的标签信息。这两种数据结构足以处理金融、统计、社会科学、工程等领域里的大多数典型用例。
```
```html
Pandas数据结构就像是低维数据的容器。比如：DataFrame是Series的容器。Series则是标量的容器。使用这种方式可以在容器中以字典的形式插入或删除对象。
```
```html
Pandas所有数据结构的值都是可变的，但数据结构的大小并非都是可变的，比如:Series的长度不可改变，但DataFrame里就可以插入列。
```
```html
Pandas中，绝大多数方法都不改变原始的输入数据，而是复制数据，生成新的对象。 一般来说，原始输入数据不变更稳妥，更加安全。
```

<a id="1.2">**1.2.Pandas数据结构对比**</a>

- **Series和DataFrame数据结构对比表**

|数据结构  |数据维度	|描述|
|---      |---      |---|
|Series   | 一维     |带标签的一维同构数组，类字典结构|
|DataFrame|	二维    |带标签的，大小可变的，二维异构表格，类嵌套字典结构|

- **从数组和字典理解Series和DataFrame**
	- Series和DataFrame分别是一维和二维数组，因为是数组，所以NumPy中关于数组的用法基本可以直接应用到这两个数据结构，包括数据创建、切片访问、通函数、广播机制等。

	- Series是带标签的一维数组，所以还可以看做是类字典结构：标签是key，取值是value；而DataFrame则可以看做是嵌套字典结构，其中列名是key，每一列的Series是value。所以从这个角度讲，pandas数据创建的一种灵活方式就是通过字典或者嵌套字典，同时也自然衍生出了适用于Series和DataFrame的类似字典访问的接口，即通过loc索引访问。

> 注意，这里强调series和dataframe是一个类字典结构而非真正意义上的字典，原因在于series中允许标签名重复、dataframe中则允许列名和标签名均有重复，而这是一个真正字典所不允许的。


参考文档：
[Pandas中文教程](https://www.pypandas.cn/docs/getting_started/overview.html#%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)
[公众号小志数据](https://mp.weixin.qq.com/s/OHflBhjPj46GT5t1532cnw)

### 第二节 Pandas模块安装
- <a href="#2.1">**2.1.Anaconda环境下安装Pandas模块**</a>
- <a href="#2.2">**2.2.Python环境下安装Pandas模块**</a>

---
<a id="2.1">**2.1.Anaconda环境下安装Pandas模块**</a>
```
# 安装Anaconda发行版自带Pandas，直接使用即可，安装Anaconda简版，使用conda管理工具安装后即可使用
$ conda create -n name_of_my_env python  # 创建新的虚拟环境
$ source activate name_of_my_env         # Linux启动虚拟环境
$ activate name_of_my_env                # Winds启动虚拟环境
$ conda search Pandas                    # 搜索Pandas安装包
$ conda install Pandas                   # 安装Pandas安装包
```
```html
# 如果出现网络问题导致安装报错或者无法联网，可以尝试如下两种解决方式进行Pandas安装：

方式1：尝试添加国内的conda源，比如口碑比较好的清华源和阿里源，然后重新安装，可以通过如下步骤解决
<a>.conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
<b>.conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
<c>.conda config --set show_channel_urls yes

方式2：如果你要安装的包国内源都没有，只能通过'Anaconda cloud'在线安装时，可以通过如下步骤解决：
<a>.在联网的电脑上，下载该安装包到本地；
<b>.将下载好的安装包拷贝到anaconda安装路径下的pkgs路径下（ ~/Anaconda3/pkgs/）；
<c>.将该安装包的下载路径添加到pkgs路径下的“urls.txt”文件中（pl, ~/Anaconda3/pkgs/urls.txt）；
<d>.重新安装。（备注：安装包的下载路径一般在安装因为网络原因中断时，错误提示中有）
```

<a id="2.2">**2.2.Python环境下安装Pandas模块**</a>
```shell
# 互联网在线环境安装Pandas模块：直接使用PIP包管理工具进行安装
$ pip | pip3 install Pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
```
```shell
# 互联网在线环境下载Pandas模块：官网下载Pandas模块及依赖模块或PIP包管理工具下载Pandas模块及依赖模块
$ pip | pip3 download -d ./[dir] -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
$ pip | pip3 install Pandas --no-index --find-links=./[dir] -r requirements.txt
```

**Pandas必须依赖库**
|依赖名称|最低支持版本|
|---|---|
|setuptools|24.2.0|
|NumPy|1.13.3|
|python-dateutil|2.6.1|
|pytz|2017.2|

```html
注意：若不提前安装依赖库会报错，在安装Pandas库时会导致安装失败。
```

**Pandas推荐依赖库**
|依赖名称|最低支持版本|
|---|---|
|numexpr|2.6.2|
|bottleneck|1.2.1|

```html
注意：强烈建议您安装这些库，因为它们可以提高处理速度，尤其是在处理大型数据集时。
```

**Pandas可选依赖库**
|依赖名称|	最低版本|	对应功能|
|---|---|---|
|BeautifulSoup4|	4.6.0|	HTML parser for read_html (see note)|
|Jinja2|		|Conditional formatting with DataFrame.style|
|PyQt4|		|Clipboard I/O|
|PyQt5|		|Clipboard I/O|
|PyTables|	3.4.2|	HDF5-based reading / writing|
|SQLAlchemy|	1.1.4|	SQL support for databases other than sqlite|
|SciPy|	0.19.0|	Miscellaneous statistical functions|
|XLsxWriter|	0.9.8|	Excel writing|
|blosc|		|Compression for msgpack|
|fastparquet|	0.2.1|	Parquet reading / writing|
|gcsfs|	0.2.2	|Google Cloud Storage access|
|html5lib|		|HTML parser for read_html (see note)|
|lxml|	3.8.0	|HTML parser for read_html (see note)|
|matplotlib|	2.2.2|	Visualization|
|openpyxl|	2.4.8	|Reading / writing for xlsx files|
|pandas-gbq|	0.8.0|	Google Big Query access|
|psycopg2|		|PostgreSQL engine for sqlalchemy|
|pyarrow|	0.9.0	|Parquet and feather reading / writing|
|pymysql|	0.7.11	|MySQL engine for sqlalchemy|
|pyreadstat|		|SPSS files (.sav) reading|
|pytables|	3.4.2	|HDF5 reading / writing|
|qtpy|		|Clipboard I/O|
|s3fs|	0.0.8	|Amazon S3 access|
|xarray|	0.8.2	|pandas-like API for N-dimensional data|
|xclip|		|Clipboard I/O on linux|
|xlrd|	1.1.0	|Excel reading|
|xlwt|	1.2.0	|Excel writing|
|xsel|		|Clipboard I/O on linux|
|zlib|		|Compression for msgpack|

```html
注意：推荐依赖库根据使用的功能进行安装，比如：项目存在Excel读写操作就需要安装xlrd和xlwt。
```

**参考文档**
[Pandas中文教程](https://www.pypandas.cn/docs/installation.html)
[公众号小志数据](https://mp.weixin.qq.com/s/OHflBhjPj46GT5t1532cnw)

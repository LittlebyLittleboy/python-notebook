# !/usr/bin/python3
# coding: utf-8
"""
简单的Web服务：hello_tornado.py源代码
"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		greeting = self.get_argument("greeting", "Hello")
		self.write(greeting + ", friendly user!")

if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()



# 程序启动
"""
第一部分：命令行启动服务

你可以在命令行里尝试运行这个程序来测试输出
$ python hello_tornado.py --port=8000
注意：服务端口参数--port可选，不写则使用默认端口启动服务
"""
"""
第二部分：请求后台返回数据

在浏览器中打开地址栏中输入：http://localhost:8000，回车显示响应结果
或者打开另一个终端窗口使用curl工具测试我们的应用是否正常响应数据：
$ curl http://localhost:8000/
Hello, friendly user!
$ curl http://loaclhost:8000/?greeting=Salutations
Salutations, friendly user!
"""

# 代码说明
"""
第一部分：必备模块的导入

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

在程序最顶部，导入一些该应用必备的Tornado模块，Tornado包括了一个有用的模块（tornado.options）来从命令行中读取设置。
我们在这里使用这个模块指定我们的应用监听HTTP请求的端口。它的工作流程如下：
如果一个与define语句中同名的设置在命令行中被给出，那么它将成为全局options的一个属性。
如果用户运行程序时使用了--help选项，程序将打印出所有你定义的选项以及你在define函数的help参数中指定的文本。
如果用户没有为这个选项指定值，则使用default的值进行代替。Tornado使用type参数进行基本的参数类型验证，当不合适的类型被给出时抛出一个异常。
因此，我们允许一个整数的port参数作为options.port来访问程序。如果用户没有指定值，则默认为8000。
"""
"""
第二部分：请求处理函数类

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')


这是Tornado的请求处理函数类。当处理一个请求时，Tornado将这个类实例化，并调用与HTTP请求方法所对应的方法。
在这个例子中，我们只定义了一个GET方法，也就是说这个处理函数将对HTTP的GET请求作出响应。我们稍后将看到实现不止一个HTTP方法的处理函数。

greeting = self.get_argument('greeting', 'Hello')

Tornado的RequestHandler类有一系列有用的内建方法，包括get_argument，我们在这里从一个查询字符串中取得参数greeting的值。
（如果这个参数没有出现在查询字符串中，Tornado将使用get_argument的第二个参数作为默认值。）

self.write(greeting + ', friendly user!')
RequestHandler的另一个有用的方法是write，它以一个字符串作为函数的参数，并将其写入到HTTP响应中。
在这里，我们使用请求中greeting参数提供的值插入到greeting中，并写回到响应中。
"""
"""
第三部分：服务启动总入口
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])

这是真正使得Tornado运转起来的语句。首先，我们使用Tornado的options模块来解析命令行。
然后我们创建了一个Tornado的Application类的实例。
传递给Application类__init__方法的最重要的参数是handlers。它告诉Tornado应该用哪个类来响应请求。

http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
从这里开始的代码将会被反复使用：一旦Application对象被创建，我们可以将其传递给Tornado的HTTPServer对象，
然后使用我们在命令行指定的端口进行监听（通过options对象取出。）
最后，在程序准备好接收HTTP请求后，我们创建一个Tornado的IOLoop的实例。
"""
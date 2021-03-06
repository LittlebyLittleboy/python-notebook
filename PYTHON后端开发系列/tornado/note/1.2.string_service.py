# !/usr/bin/python3
# coding: utf-8
"""
简单的字符串服务：string_service.py源代码
"""
import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))
        
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/reverse/(\w+)", ReverseHandler),
            (r"/wrap", WrapHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



# 程序启动
"""
第一部分：命令行启动服务

你可以在命令行里尝试运行这个程序来测试输出
$ python string_service.py --port=8000
注意：服务端口参数--port可选，不写则使用默认端口启动服务
"""
"""
第二部分：请求后台返回数据

这个程序是一个通用的字符串操作的Web服务端基本框架。到目前为止，你可以用它做两件事情。
其一，到/reverse/string的GET请求将会返回URL路径中指定字符串的反转形式。
$ curl http://localhost:8000/reverse/stressed
desserts
$ curl http://localhost:8000/reverse/slipup
pupils

其二，到/wrap的POST请求将从参数text中取得指定的文本，并返回按照参数width指定宽度装饰的文本。
下面的请求指定一个没有宽度的字符串，所以它的输出宽度被指定为程序中的get_argument的默认值40个字符。

$ http://localhost:8000/wrap -d text=Lorem+ipsum+dolor+sit+amet,+consectetuer+adipiscing+elit.
Lorem ipsum dolor sit amet, consectetuer
adipiscing elit.
"""

# 代码说明
"""
字符串服务示例和上一节示例代码中大部分是一样的。让我们关注那些新的代码。
首先，让我们看看传递给Application构造函数的handlers参数的值：
app = tornado.web.Application(handlers=[
    (r"/reverse/(\w+)", ReverseHandler),
    (r"/wrap", WrapHandler)
])
在上面的代码中，Application类在"handlers"参数中实例化了两个RequestHandler类对象。
第一个引导Tornado传递路径匹配下面的正则表达式的请求：/reverse/(\w+)
"""
"""
正则表达式告诉Tornado匹配任何以字符串/reverse/开始并紧跟着一个或多个字母的路径。
括号的含义是让Tornado保存匹配括号里面表达式的字符串，并将其作为请求方法的一个参数传递给RequestHandler类。
让我们检查ReverseHandler的定义来看看它是如何工作的：

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

你可以看到这里的get方法有一个额外的参数input。这个参数将包含匹配处理函数正则表达式第一个括号里的字符串。
（如果正则表达式中有一系列额外的括号，匹配的字符串将被按照在正则表达式中出现的顺序作为额外的参数传递进来。）
"""
"""
class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))

WrapHandler类处理匹配路径为/wrap的请求。这个处理函数定义了一个post方法，也就是说它接收HTTP的POST方法的请求。
我们之前使用RequestHandler对象的get_argument方法来捕获请求查询字符串的的参数。同样，我们也可以使用相同的方法来获得POST请求传递的参数。
（Tornado可以解析URLencoded和multipart结构的POST请求）。一旦我们从POST中获得了文本和宽度的参数，
我们使用Python内建的textwrap模块来以指定的宽度装饰文本，并将结果字符串写回到HTTP响应中。
"""
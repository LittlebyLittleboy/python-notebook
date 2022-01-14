# !/usr/bin/env python3
# author:156***@139.com
"""
功能：重写响应体错误消息Web应用程序
1.导入必备模块及函数
2.编写请求处理函数类
3.定义命令传入行参数
4.开启并监听后台服务
"""
"""
1.开启服务：
$ python hello_errors.py --port=8000
2.接口测试：
$ curl -d foo=bar http://localhost:8000/
Gosh darnit, user! You caused a 405 error.
"""
"""
你可以使用RequestHandler类的set_status()方法显式地设置HTTP状态码。Tornado会自动地设置HTTP状态码。常见情况如下：

404 Not Found：Tornado会在HTTP请求的路径无法匹配任何RequestHandler类相对应的模式时返回404（Not Found）响应码。
400 Bad Request：如果你调用了一个没有默认值的get_argument函数，并且没有发现给定名称的参数，自动返回一个400响应码。
405 Method Not Allowed：如果传入的请求使用了RequestHandler中没有定义的HTTP方法。
500 Internal Server Error：当程序遇到任何不能让其退出的错误时，你代码中任何没有捕获的异常也会导致500响应码。
200 OK：如果响应成功，并且没有其他返回码被设置，Tornado将默认返回一个200（OK）响应码。
"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options


# matched with (r"/", IndexHandler)
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

    def write_error(self, status_code, **kwargs):
        self.write("Gosh darnit, user! You caused a %d error." % status_code)

if __name__ == "__main__":
    # define commond param, port from external or default value
    define("port", default=8000, help="run on the given port", type=int)
    # parse commond line param as global variable
    tornado.options.parse_command_line()
    # init app and define the url view func map
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    # listen to the port and start app server
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
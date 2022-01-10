# !/usr/bin/env python3
# author:156***@139.com
"""
功能：简单的Web应用程序
1.导入必备模块及函数
2.编写请求处理函数类
3.定义命令传入行参数
4.开启并监听后台服务
"""
"""
1.开启服务：
$ python hello_tornado.py --port=8000
2.接口测试：
$ curl http://localhost:8000/?greeting=tornado
"""

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options


# matched with (r"/", IndexHandler)
class IndexHandler(tornado.web.RequestHandler):
	# inherit tornado.web.RequestHandler and rewrite get method
	def get(self):
		# call get_argument method and get param or default value
		greeting = self.get_argument("greeting", "Hello")
		# write a string result to http response body 
		self.write(greeting + ", friendly user!")


if __name__ == '__main__':
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

# !/usr/bin/env python3
# author:156***@139.com
"""
功能：简单示例：Poem Maker Pro
1.导入必备模块及函数
2.编写请求处理函数类
3.定义命令传入行参数
4.开启并监听后台服务
"""
"""
1.开启服务：
$ python poemmaker.py --port=8000
2.接口测试：
$ curl http://localhost:8000/
$ curl -X POST -d "noun1=tom&noun2=jav&noun3=ros&verb=bal" http://localhost:8000/poem
"""

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options


class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		# self.render("index.html")
		self.write("<html><body><h1>Welcome!</h1></body></html>")


class PoemPageHandler(tornado.web.RequestHandler):
	def post(self):
		noun1 = self.get_argument("noun1")
		noun2 = self.get_argument("noun2")
		verb = self.get_argument("verb")
		noun3 = self.get_argument("noun3")
		self.render("poem.html", roads=noun1, wood=noun2, made=verb, difference=noun3)


if __name__ == "__main__":
	define("port", default=8000, help="run one the given port")
	app = tornado.web.Application(
		handlers = [(r"/", IndexHandler), (r"/poem", PoemPageHandler)], 
		template_path=os.path.join(os.path.dirname(__file__),"templates"),
		debug=True
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()


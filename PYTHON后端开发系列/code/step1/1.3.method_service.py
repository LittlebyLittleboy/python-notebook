# !/usr/bin/env python3
# author:156***@139.com
"""
功能：简单的字符串Web应用程序
1.导入必备模块及函数
2.编写请求处理函数类
3.定义命令传入行参数
4.开启并监听后台服务
"""
"""
1.开启服务：
$ python method_service.py --port=8000
2.接口测试：
$ curl http://localhost:8000/frob/10
$ curl http://localhost:8000/widget_id
$ curl http://localhost:8000/widget_id -d text=10
"""

import json
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options


# matched with (r"/widget/(\d+)", WidgetHandler)
class WidgetHandler(tornado.web.RequestHandler):
    def get(self, widget_id):
        widget = self.retrieve_from_db(widget_id)
        self.write(widget)

    @staticmethod
    def save_to_db(widget):
    	print("start to save_to_db......")

    @staticmethod
    def retrieve_from_db(frob_id):
        print("start to retrieve_from_db......")
        data = json.dumps({"id": frob_id})
        return data

    def post(self, widget_id):
        widget = self.retrieve_from_db(widget_id)
        widget['foo'] = self.get_argument('foo')
        self.save_to_db(widget)


# matched with (r"/frob/(\d+)", FrobHandler)
class FrobHandler(tornado.web.RequestHandler):
    def head(self, frob_id):
        frob = self.retrieve_from_db(frob_id)
        if frob is not None:
            self.set_status(200)
        else:
            self.set_status(404)

    @staticmethod
    def retrieve_from_db(frob_id):
        print("start to retrieve_from_db......")
        data = json.dumps({"id": frob_id})
        return data

    def get(self, frob_id):
        frob = self.retrieve_from_db(frob_id)
        self.write(frob)


if __name__ == '__main__':
    # define commond param, port from external or default value
    define("port", default=8000, help="run on the given port", type=int)
    # parse commond line param as global variable
    tornado.options.parse_command_line()
    # init app and define the url view func map
    app = tornado.web.Application(
        handlers=[
        (r"/widget/(\d+)",WidgetHandler),
        (r"/frob/(\d+)",FrobHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    # listen to the port and start app server
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
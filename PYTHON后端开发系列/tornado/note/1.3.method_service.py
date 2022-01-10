# !/usr/bin/python3
# coding: utf-8
"""
简单的method服务：method_service.py源代码
"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# matched with (r"/widget/(\d+)", WidgetHandler)
class WidgetHandler(tornado.web.RequestHandler):
    def get(self, widget_id):
        widget = retrieve_from_db(widget_id)
        self.write(widget.serialize())

    @staticmethod
    def save_to_db(widget):
    	print("start to save_to_db......")

    def post(self, widget_id):
        widget = retrieve_from_db(widget_id)
        widget['foo'] = self.get_argument('foo')
        self.save_to_db(widget)


# matched with (r"/frob/(\d+)", FrobHandler)
class FrobHandler(tornado.web.RequestHandler):
    def head(self, frob_id):
        frob = retrieve_from_db(frob_id)
        if frob is not None:
            self.set_status(200)
        else:
            self.set_status(404)

    @staticmethod
    def retrieve_from_db(frob_id):
    	print("start to retrieve_from_db......")
    	return frob_id

    def get(self, frob_id):
        frob = self.retrieve_from_db(frob_id)
        self.write(frob.serialize())


if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/widget/(\d+)",WidgetHandler),
		(r"/frob/(\d+)",FrobHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:156***@139.com
import json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from tornado.escape import json_encode, json_decode


class ProductHandler(tornado.web.RequestHandler):

	def post(self):
		"""功能：新增商品"""
		line = json.loads(self.request.body)
		print("insert line into database.")
		options.db["product"].append(line)
		self.write(json.dumps(line))

	def index(self, id):
		"""功能：获取索引"""
		for index, line in enumerate(options.db["product"]):
			if line.get("id") == id:
				return index

	def delete(self, id):
		"""功能：删除商品"""
		delete_index = self.index(int(id))
		print("delete line from database.")
		options.db["product"].pop(delete_index)
		self.write(json.dumps({"id": id}))

	def put(self, id):
		"""功能：修改商品"""
		line = json.loads(self.request.body)
		delete_index = self.index(int(id))
		options.db["product"].pop(delete_index)
		options.db["product"].append(line)
		print("update line in database.")
		self.write(json.dumps(line))

	def get(self, id):
		"""功能：获取商品"""
		index = self.index(int(id))
		line = options.db["product"][index]
		print("get line from database.")
		self.write(json.dumps(line))

	def write_error(self, status_code, **kwargs):
		"""功能：重写错误"""
		self.write("Gosh darnit, user! You caused a %d error." % status_code)


class OrderHandler(tornado.web.RequestHandler):

	def post(self):
		"""功能：新增订单"""
		line = json.loads(self.request.body)
		print("insert line into database.")
		options.db["order"].append(line)
		self.write(json.dumps(line))

	def index(self, id):
		"""功能：获取索引"""
		for index, line in enumerate(options.db["order"]):
			if line.get("id") == id:
				return index

	def delete(self, id):
		"""功能：删除订单"""
		delete_index = self.index(int(id))
		print("delete line from database.")
		options.db["order"].pop(delete_index)
		self.write(json.dumps({"id": id}))

	def put(self, id):
		"""功能：修改订单"""
		line = json.loads(self.request.body)
		delete_index = self.index(int(id))
		options.db["order"].pop(delete_index)
		options.db["order"].append(line)
		print("update line in database.")
		self.write(json.dumps(line))

	def get(self, id):
		"""功能：获取订单"""
		index = self.index(int(id))
		line = options.db["order"][index]
		print("get line from database.")
		self.write(json.dumps(line))

	def write_error(self, status_code, **kwargs):
		"""功能：重写错误"""
		self.write("Gosh darnit, user! You caused a %d error." % status_code)


if __name__ == '__main__':
	# 定义样例数据以全局变量形式声明到全局，每对外层键值为一张表
	database = {
		"product":[
					{"id":1, "product_code": "P20200829001", "product_name": "华为P30", "product_price": 3999, "price_unit": "￥"},
					{"id":2, "product_code": "P20200829002", "product_name": "华为P40", "product_price": 4999, "price_unit": "￥"},
					{"id":3, "product_code": "P20200829003", "product_name": "小米8", "product_price": 2999, "price_unit": "￥"},
					{"id":4, "product_code": "P20200829004", "product_name": "红米8", "product_price": 1999, "price_unit": "￥"},
					{"id":5, "product_code": "P20200829005", "product_name": "苹果10", "product_price": 3888, "price_unit": "￥"},
					{"id":6, "product_code": "P20200829006", "product_name": "苹果11", "product_price": 5999, "price_unit": "￥"},
					], 
		"order":[
					{"id": 1, "order_code":"020200829001", "store_name":"上海华为体验店", "order_name": "华为P40"},
					{"id": 2, "order_code":"020200829002", "store_name":"北京华为体验店", "order_name": "华为P30"},
					{"id": 3, "order_code":"020200829003", "store_name":"南京小米体验店", "order_name": "红米8"},
					{"id": 4, "order_code":"020200829004", "store_name":"广州小米体验店", "order_name": "小米8"},
					{"id": 5, "order_code":"020200829005", "store_name":"深圳苹果体验店", "order_name": "苹果10"},
					{"id": 6, "order_code":"020200829006", "store_name":"西安苹果体验店", "order_name": "苹果11"},
					]
	}
	# 定义命令行参数作为全局变量，并设置变量的默认值和数据类型
	define("db", default=database, help="database store data lines",type=dict)
	define("port", default=8000, help="run on the given port",type=int)
	# 解析命令行参数，赋值给已定义的全局变量
	tornado.options.parse_command_line()
	# 声明应用实例，添加路由表，设置调试模式
	app = tornado.web.Application(handlers=[
			(r"/product/insert", ProductHandler),
			(r"/product/delete/(\d+)", ProductHandler),
			(r"/product/update/(\d+)", ProductHandler),
			(r"/product/select/(\d+)", ProductHandler),
		], 
		debug=True
	)
	# 注册应用实例为后台服务
	http_server = tornado.httpserver.HTTPServer(app)
	# 指定监听后台服务端口号
	http_server.listen(options.port)
	# 异步开启并监听后台服务
	tornado.ioloop.IOLoop.instance().start()


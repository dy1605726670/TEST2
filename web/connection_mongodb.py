import pymongo

'''
	服务器端
	连接并操作数据库
'''

class My_db(object):
	def __init__(self):
		# 连接数据库
		mongo_client = pymongo.MongoClient('localhost', 27017)

		# 获取数据库
		db = mongo_client.my_data

		# 获取集合
		self.collection = db.my_data

		# 当前温度
		self.data = self.query()


	# 从数据库查询获取数据
	def query(self):	
		# 查询 collection 中的第一条数据 返回一个字典
		data = self.collection.find_one()

		# 返回内容（字典）
		return data   


	# 修改数据
	def update(self, value):
		# 1、获取修改的内容
		update_data = self.query()

		# 2、指定要修改成的值
		new_update_data = {"$set" : {"temperature" : value}}

		# 3、更新数据库
		self.collection.update_one(update_data, new_update_data)

		# 4、更新当前温度
		self.data = self.query()


if __name__ == '__main__':
	a = My_db()
	# a.update(value=12345)
	a.query()
	print(a.data["temperature"])
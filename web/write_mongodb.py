import connection_mongodb
from time import sleep

# 从文本文件读取数据取最末值为当前数据
def read_data():
	with open("data.txt", "r", encoding="gbk") as f:
		data = f.read()

	data = data[:-1]   # 去掉最后一个回车符号
	data = data.split("\n")   # 拆分为列表 
	return data


# 将最末值写入数据库
def write_data(data_ls):
	f = connection_mongodb.My_db()  
	f.update(data_ls[-1])   # 将最新数据写入数据库


def main():
	data = read_data()
	write_data(data)


if __name__ == '__main__':
	while True:
		main()
		sleep(1)
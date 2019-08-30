from socket import *

''' 服务器 '''

def main():
	# 1 创建套接字
	tcp_server_socket = socket(AF_INET, SOCK_STREAM)
 
	# 2 bind 绑定 IP 和 port
	tcp_server_socket.bind(("127.0.0.1", 7890))
 
	# 3 listen 使套接字变为被动链接
	tcp_server_socket.listen(128)
 
	# 4 accept 等待客户端的链接 返回值（新套接字：为客户端服务，客户端信息）
	while True:
		print("等待客户端连接中...")
		new_socket, addr = tcp_server_socket.accept()  # 堵塞状态
		print("客户端已连接...")
 
		# 5 接收发送数据
		while True:
			try:
				recv_data = new_socket.recv(1024)   # 接受客户端的请求 最大 1024 接收二进制字节流
				
				if recv_data.decode("gbk") == "hcasjaasfc":   # 结束服务
					return 

				# 解码并写入文本文件
				data = recv_data.decode("gbk")   # 解码
				if type(data) is str:
					with open("data.txt", "a", encoding="gbk") as f:
						f.write(data + "\n")
				else:
					data = str(data)
					with open("data.txt", "a", encoding="gbk") as f:
						f.write(data + "\n")
				# my_database.update(value = data)   # 写入数据库

				

				if recv_data:
					new_socket.send("**ok**".encode("gbk"))   # 回复客户端表示收到请求
				else:
					break
			except:
				break
 
		# 6 关闭 accept 返回的套接字 表示不再为该客户端服务
		new_socket.close()
	# 关闭 tcp_server_socket 套接字
	tcp_server_socket.close()
 
if __name__ == '__main__':
	main()

# 导入所需的模块
from socket import *

# 设置服务器端口号
serverPort = 15000

# 创建一个 IPv4 的 UDP 套接字
serverSocket = socket(AF_INET, SOCK_DGRAM)

# 绑定服务器的 IP 地址和端口号
serverSocket.bind(('127.0.0.3', serverPort))

# 打印服务器就绪信息
print("The server is ready to receive")

# 进入接收循环
while True:
    # 接收来自客户端的数据和客户端地址
    data, clientAddress = serverSocket.recvfrom(4096)

    # 通过分隔符'\n'将文件名和文件内容分开
    file_name, file_content = data.decode().split('\n', 1)

    # 将收到的文件内容写入新建的文件中
    with open(file_name, 'w') as file:
        file.write(file_content)

    # 构建响应消息
    modifiedMessage = "File received"

    # 将响应消息发送回客户端
    # 使用 encode() 方法将消息字符串转换为字节流，然后使用 sendto() 方法发送到客户端的地址
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
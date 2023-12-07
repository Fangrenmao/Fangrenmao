# 导入所需的模块
from socket import *

# 创建一个 IPv4 的 UDP 套接字
clientSocket = socket(AF_INET, SOCK_DGRAM)

# 获取服务器的 IP 地址和端口号
serverName = input('请输入 server ip:')
serverPort = int(input('请输入 server port:'))

# 获取要发送的文件名
filename = input('请输入文件名:')

# 读取要传输的文件内容
with open(filename, 'r') as file:
    fileContent = file.read()

# 将文件名和文件内容组合成一个字符串，用`\n`分隔
message = filename + '\n' + fileContent

# 发送消息到指定的服务器
# 使用 encode() 方法将消息字符串转换为字节流，然后使用 sendto() 方法发送到指定的服务器和端口
clientSocket.sendto(message.encode(), (serverName, serverPort))

# 接收来自服务器的响应，并获取响应消息和服务器地址
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# 将接收到的响应消息解码为字符串，并打印输出
print(modifiedMessage.decode())

# 关闭客户端的套接字连接
clientSocket.close()
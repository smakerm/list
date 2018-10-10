# fork + tcp 并发

from socketserver import *

#创建服务器类
class Server(ThreadingMixIn,TCPServer):
    pass

# class Server(ForkingTCPServer):
#     pass

#创建处理类
class Handler(StreamRequestHandler):
    #当有客户端链接时候调用该函数自动处理
    #客户段请求事件
    def handle(self):
        print("connect from ",self.client_address)
        while True:
            #self.request 为tcp中为我们自动生成的
            #和客户端交互的套接字
            data = self.request.recv(1024).decode()
            if not data:
                break
            print("服务器收到：",data)
            self.request.send(b'receive your message')

#使用创建的服务器类来生产服务器
server = Server(('172.60.50.218',9999),Handler)
#运行服务器
server.serve_forever()
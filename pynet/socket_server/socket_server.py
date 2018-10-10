from socketserver import *

#1. 创建服务器类
class Server(ForkingMixIn, TCPServer):
    pass

#class Server(ForkingTCPServer):
#    pass

#2. 创建处理类
class Handler(StreamRequestHandler):
    #当有客户端链接的时候，调用该函数自动处理
    #客户端请求事件
    def handle(self):
        print("connect from", self.client_address)
        while True:
            #self.request 为tcp中为我们自动生成的和客户端交互的套接字
            data = self.request.recv(1024).decode()
            if not data:
                break
            print("收到了：", data)
            n = self.request.send(b"Recv your message")
        


#3. 使用创建的服务器类来生产服务器
server = Server(('127.0.0.1', 8889), Handler)
#运行服务
server.serve_forever()

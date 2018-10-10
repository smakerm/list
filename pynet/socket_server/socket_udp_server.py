from socketserver import *


class Server(ForkingUDPServer):
    pass

class Handler(DatagramRequestHandler):
    def handle(self):
        data = self.rfile.readline()
        print("接收到了：", data.decode())
        self.wfile.write(b"receive message ")


server = Server(('0.0.0.0', 8888), Handler)
server.serve_forever()


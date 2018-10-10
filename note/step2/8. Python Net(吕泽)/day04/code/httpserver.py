#导入HTTPSERVER类　　兼容python3 and python2
try:
    from BaseHTTPServer import \
    BaseHTTPRequestHandler,HTTPServer
except ImportError:
    from http.server import \
    BaseHTTPRequestHandler,HTTPServer

#具体的请求处理类
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("do method get")
        fd = open('index.html','rb')
        content = fd.read() 
        #设置响应码
        self.send_response(200)
        #设置响应头
        self.send_header('Content-type','text/html')
        #响应头设置完毕
        self.end_headers()
        #发送响应体
        self.wfile.write(content)
        return

    def do_POST(self):
        pass 

#搭建启动服务器
address = ('127.0.0.1',8000)
server = HTTPServer(address,RequestHandler)
server.serve_forever()

OSI模型
```flow
应用层：提供用户服务，例如处理应用程序，文件传输，数据管理
表示层：做数据的转换和压缩，解密，加密等
会话层：决定了进程间的连接建立，选择使用什么样的传输层协议
传输层：建立网络连接，提供合适的连接传输服务，提供流量控制
网络层：控制分组传输，进行路由选择，网络互联
链路层：提供链路交换，具体的数据收发
物理层：网络交换设备，传输介质，网卡网口的选择
```

```
应用层
传输层
网络层
物理链路层
```

五层（TCP/IP）模型
```
应用层
传输层
网络层
链路层
物理层
```

字节序
小端序：低字节存在低地址位
大端序：高字节存在低地址位

网络字节序：大端序


###TCP
使用情况：对传输质量要求较高，需要可靠的

三次握手四次挥手
客户端向服务端发送连接请求（发送一个试探性的标志位字符给服务器 ACK）
服务器端接受到请求后告知客户端可以连接
再次告知服务器客户端已收到回复，下面要开始发送具体消息
主动方发送标志告知被动方要断开连接
被动方返回相应的标志信息告知主动方我已经接受到你的请求
被动方会再次发送标志位信息表示已经准备就绪可以断开
主动方断开连接告知被动方

####TCP粘包
指的是发送方发送若干次数据的时候，因为是数据流的传输方式，导致数据粘连在一起，接收方一次将多次发送的数据一起接收，产生接收数据的粘连
粘包是tcp传输特有的现象，因为tcp传输没有消息边界。如果是发送连续的内容比如文件等则粘包没有影响，如果是每次大宋为单独需要处理内容则需要处理粘包

如何处理粘包
1. 将消息格式化
2. 发送消息的同时，发送一个消息长度的标志
3. 让消息的发送延迟，使接收端每次的后能够有时间接收一个消息


基于tcp协议的scoket编程

* s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
设置端口不保存

服务端
1. 创建一个tcp流式套接字
socket(family=AF_INET, type=SOCK_STREAM, proto=0)
功能：创建一个套接字
参数：	family 协议族类型
		type 套接字类型	SOCK_STREAM
							SOCK_DGRAM
							SOCK_RAM
		proto	子协议类型	一般为0
返回值：套接字对象

2. 绑定本机IP和端口号
bind(address)
功能：绑定本机的IP和端口号
参数：是一个包含两个元素的元组，元组的第一个元素是主机名，第二个是使用的端口号
e.g.	('',8888)
		('0.0.0.0',8888)

3. 将套接字变为可监听的套接字
listen(n)
功能： 将套接字设置为监听套接字，并且设置一个连接等待队列
参数： 是一个正整数 >=1

4. 套接字等待客户端的请求
accept()
功能： 阻塞等待客户端的连接
参数：无
返回值：	第一个为和客户端交互的新的套接字
			第二个为客户端的地址

5. 	消息的收发
recv()
功能：	接收网络消息
参数：	buffer 表示一次从缓冲区中拿到的消息的字节数
返回值：	返回接收到的消息
* 当接收的网络缓冲中没有内容时会阻塞
* 当连接断开后，recv会结束阻塞返回一个空字符串
* recv会不断的取出缓冲区中的内容，如果一次没有拿完，那么下次会继续收取没拿完的消息



send()
功能：	发送网络消息
参数：	要发送的内容
返回值：	实际发送的字节数
*python3中，参数必须是bytes

sendall(data)
返回值：如果成功发送，返回none 发送失败报异常

6. 关闭套接字

客户端
1. 创建一个tcp流式套接字
connect(address)


###UDP连接

使用情况：	对实时性要求较高
			对网络情况不佳的时候
			对数据的准确性没有严格要求
			建立必要的非连接的情况（广播）

####服务端：
1. 创建数据报套接字
2. 绑定本地IP和端口
3. 收发消息
recvfrom(buffersize)
功能：	在UDP中接收消息
参数：	buffersize 表示一次最多可以接收的字节数
返回值：	data：	接收到的消息
			addr：	表示从那个客户端接收到的消息
* recvfrom每次只能接收一个数据包，如果数据包的大小曹国recvfrom的设置大小则会出现数据丢失

sendto(data, addr)
功能：	向一个网络终端发送消息
参数：	data	要发送的消息（bytes）
		addr	发送对象的地址
	
4. 关闭套接字

####客户端
1. 创建数据报套接字
2. 消息收发
3. 关闭套接字


socket模块和套接字属性

getpeername()
功能：用作服务器连接套接字，查看连接的客户端的地址
getsockname
功能：获取套接字绑定的ip和端口
fileno()
功能：获取套接字的文件描述符号码
文件描述符：系统会给进程中的每一个IO操作对象分配一个>=0的正整数作为标号，我们称之为该IO操作的文件描述符。一个进程中所有IO的文件描述符不会重复
setsockopt(level, optname, value)
功能：	设置套接字选项
参数：	level	要定义的选项类型
		 e.g. 	SOL_SOCKRT IPPROTO_IP IPPROT_TCP
		optname 每种类型都有具体的选项，根据具体的需求选择选项进行设置
		 e.g.	SOL_SOCKET ----> SO_REUSERADDR
		value 将选择的选项设置为什么值
getsockopt(level, optname)
功能：获取相应选项的值
返回值：获取到的值
s.type 套接字类型







```python
In [1]: import socket

In [2]: socket.gethostname()
Out[2]: 'room9pc01.tedu.cn'
In [3]: socket.gethostbyname('localhost')
Out[3]: '127.0.0.1'

In [4]: socket.gethostbyname('room9pc01.tedu.cn')
Out[4]: '172.240.2.192'

In [9]: socket.gethostbyaddr("155.239.210.27")

In [10]: socket.inet_aton("192.168.0.1")
Out[10]: b'\xc0\xa8\x00\x01'

In [11]: socket.inet_ntoa( b'\xc0\xa8\x00\x01')
Out[11]: '192.168.0.1'

In [13]: socket.inet_ntop( socket.AF_INET,b'\xc0\xa8\x00\x01')
Out[13]: '192.168.0.1'

In [14]: socket.inet_pton(socket.AF_INET6,'')
                        
                        
In [8]: socket.getservbyname('mysql')
Out[8]: 3306

In [15]: socket.getservbyport(443)
Out[15]: 'https'

                            
```



###**socketserver**
'BufferedIOBase',
'DatagramRequestHandler',
'ForkingMixIn',
'ForkingTCPServer',
'ForkingUDPServer',
'StreamRequestHandler',
'TCPServer',
'ThreadingMixIn',
'ThreadingTCPServer',
'ThreadingUDPServer',
'UDPServer',

步骤：
1. 创建服务器类
2. 创建处理类
3. 使用创建的服务器类来生产服务器


FTP服务器：
客户端：
1. 查看目录  ls
2. 下载文件  wget filename path
3. 上传文件  wput filename path

服务端：


os.listdir(path)
os.path.isfile(filename)

os.path.isfile(protobuf-java-2.5.0.jar)



###**IO 服务器模型：**

IO的分类：	
1. 阻塞IO 

2. 非阻塞IO
在遇到原本阻塞的条件是不再阻塞，去执行其他内容，但往往需要不断轮询阻塞事件是否可以执行 
3. IO多路复用 
同时监控多个IO时间，当IO哪个事件就绪就执行哪个IO事件，形成一种并发效果

4. 异步IO

IO多路复用
import select

win 	--->  select
linux ---> 	select poll epoll

(rlist, wlist, xlist) = select(rlist, wlist, xlist[, timeout])
功能：	通过select方法监控IO事件
参数：	rlist 列表	存放要监控的读IO事件	我们将要处理的IO事件
		wlist 列表	存放要监控的写IO事件	要主动处理的IO事件
		xlist 列表	存放要监控的IO事件		希望发生异常通知你处理的IO事件
返回值：当select监控的IO事件中有一个或多个可以处理的时候结束阻塞，进行返回
		r		列表	参数rlist中如果有可以处理的IO放在这个列表
		w		列表	参数wlist中如果有可以处理的IO放在这个列表
		x		列表	参数xlist中如果有可以处理的IO放在这个列表


多路复用的特点：
1. 可以同时监听多种IO事件
2. 当任意IO事件发生时会处理
3. 当处理每一个事件是不能死循环（长期占有服务器）
4. IO多路复用，是基于IO的处理，不是多进程或多线程


####poll多路复用：
1. 创建poll对象
`p = select.poll()`

2. 加入关注的IO事件
`p.register(s)`
 
3. 监控哪个IO事件发生
```
events = p.poll()
返回值：[(1,evtnt),(2,event),(3,event)...]
```
元组中第一个元素为就绪的IO的fileno
第二个元素为具体的就是事件（read write error）
* 往往需要写一个字典 让IO对象个和fileno对应起来


4. 将事件移除监控范围
p.unregister(s)


poll 和 epoll 中事件的分类：
POLLIN		POLLOUT	POLLERR	PULLUP		POLLPRI	POLLVAL
rlist		wlist		xlist		紧急链接	紧急处理	无效数据

event & POLLIN  如果为True 表示该类型的数据准备就绪

####epoll
也是IO多路复用的方式，效率比select和poll要高一点
不仅支持水平触发，也支持边缘触发


###协程服务器模型
协程（微线程，纤程） 本质单线程
定义：是一种用户态的轻量级线程

1. 轻量级，创建消耗资源非常少
2. 不涉及内核

优点：	无需上下文切换的开销
		无需同步互斥操作
		有较高的并发型（IO并发）
		创建消耗资源少
缺点：	无法利用计算机的多核资源
		遇到死循环等阻塞状态会影响整个程序的运行

greenlet 
gevent 
evenless


进程 + 协程 方案完成高并发
1. 什么是协程 （单线程 优点 缺点 高并发量的 IO 操作）
2. 协程是如何运行的 （在线程栈内进行跳转，是应用层的技术，遇到IO阻塞进行协程选择）
3. 写过什么协程代码



###非阻塞IO和超时检测

非阻塞IO：	在遇到原本阻塞的IO情形时，不再进行阻塞等待，如果满足条件即执行，不满足条件就不执行

sockfd.setblocking(False)
功能：	设置一个套接字的阻塞状态
参数：	默认为True 表示套接字为阻塞套接字
		如果设置为False则表示非阻塞，此时套接字使用阻塞函数是，如果无法执行则抛出 blocking 异常

监听套接字设置为非阻塞 accept 不再阻塞
连接套接字设置为非阻塞 recv 不再阻塞

超时检测
在阻塞状态下，设置程序超时时间。当到达事件后程序不再阻塞等待
e.g.
multiprocessing/threading ---->join
Queue ---> get put
select ---> select
Event ---> wait

sockdf.settimeout(5)

功能：设置套接字的超时检测时间
参数：超时时间

####网络广播
udp 数据报套接字
广播地址：	255
设置为可以发送接收广播的套接字
s.setsockopt(SOL_SOCKET,SO_BROADCST,1)

* 在网络中如果存在大量的广播会产生广播风暴，占用大量带宽


####本地套接字

作用：	用作本地两个进程间的通信
传输方式： 字节流的方式进行数据传输

创建本地套接字

socket(AF_UNIX, SOCK_STREAM)

通信介质：	通过套接字文件实现通信


###HTTP

http协议的特点
1. 支持典型的客户端服务器模式
2. 灵活简单
3. 几乎支持所有的数据格式
4. 是无状态的
5. http1.0 无连接  http1.1 持续连接

####请求
1. 请求格式：

请求行：	要发送什么类型的请求
请求头：	对发送请求信息的描述
空行
请求体：	具体的请求参数或请求内容

GET			/index.heml	HTTP/1.1
请求方法	请求格式		协议版本

GET			获取URL标识的网络资源
POST		提交一定的附加数据，用以获取相应的返回

HEAD		获取URL所标识的相应信息报头
PUT			获取服务器的资源
DELETE		删除一个服务器资源
TRACE		用于测试和诊断
CONNECT	保留的方法
OPTIONS	请求获取服务器性能，查询相关数据

Accept:


请求体

get请求：	请求体即为get请求的参数
post请求：	请求体即为post请求提交的内容

####响应
响应行：反馈响应情况
响应头：对响应的内容的描述
空行
响应体：根据请求返回给客户端的内容

http/1.1		200		ok
协议版本		响应码	响应码对应信息


python3	http.server.BaseHTTPSERVER
python2	BaseHTTPServer




































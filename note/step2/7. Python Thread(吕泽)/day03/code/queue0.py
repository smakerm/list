from multiprocessing import Queue 

#创建消息队列对象
q = Queue(3)

i = 0
# 存放消息　
while True:
    #判断队列是否满了
    if q.full():
        print("queue is full")
        break
    q.put("hello" + str(i))
    i += 1

print("当前队列有%d条消息"%q.qsize())

for i in range(q.qsize()):
    print("获取消息%s"%q.get())

print("is empty?",q.empty())

print(q.get(True,3))

print("process over")
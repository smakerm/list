from multiprocessing import Event 

#生成事件对象　
e = Event() 

#检测事件对象，如果被设置则返回True否则返回false
print(e.is_set())

#设置事件对象
e.set()

#提供事件的阻塞
e.wait()

print("wait.....")
#清除对事件的设置
e.clear()

e.wait()

print("wait...wait.....")



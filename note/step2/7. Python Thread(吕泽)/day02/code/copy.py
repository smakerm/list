import os 

#获取文件的大小
size = os.path.getsize('file')

#在创建进程前获取文件对象,子进程接受后父子
#进程使用同一个文件偏移量会造成混乱
# f = open('file','r')

pid = os.fork() 

if pid < 0:
    print("不想动")
#子进程拷贝前半部分
elif pid == 0:
    n = size // 2 
    fw = open('child','w')
    with open('file','r') as f:
        while True:
            if n < 64:
                data = f.read(n)
                fw.write(data)
                break
            data = f.read(64)
            fw.write(data)
            n -= 64
    fw.close()

#父进程后半部分
else:
    fw = open('parent','w')
    with open('file') as f:
        f.seek(size // 2,0)
        while True:
            data = f.read(64)
            if not data:
                break 
            fw.write(data)
    fw.close()

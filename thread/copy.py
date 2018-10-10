import os

wfile = '../deamon.py' 
size = os.path.getsize(wfile)

pid = os.fork()

if pid < 0:
    print()
elif pid == 0:
    n = size / 2
    fw = open('child', 'w')
    with open('wfile', 'r') as f:
        while True:
            if n < 64:
                data = f.read(n)
                fw.write(data)
                break
            data = f.read(64)
            fw.write(data)
            n -= 64
    fw.close()

else:
    fw = open('parent','w')
    with open(wfile) as f:
        f.seek(size // 2, 0)
        while True:
            data = f.read(64)
            if not data:
                break
            fw.write(data)
    fw.close()


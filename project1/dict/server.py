# 1.数据库要存储注册人员信息和历史记录
# 2.要允许多个用户能够同时操作
# 3.建议使用tcp完成网络传输
# 4.单词使用单词本进行处理
# 提示 ： 单词本每个单词占一行
#         单词和解释之间一定有空格
# 	单词按照顺序排列

from socket import *
import select
import queue
import pymysql

massage_queue = {}


def do_reg(db, data):
    name = data[1]
    password = data[2]

    sql = "select * from user where name = '%s'" % name
    data = db.execute(sql)
    # print('data:', data)
    if not data:
        sql = "insert into user values ('%s','%s') " % (name, password)
        db.execute(sql)
        return True
    else:
        return False

def do_history():
    pass


def do_quit():
    pass


def main():
    HOST = '127.0.0.1'
    PORT = 8888
    ADDR = (HOST, PORT)
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    db = pymysql.connect('127.0.0.1', 'root', '123456')
    cur = db.cursor()
    cur.execute('use dict')


    rlist = [s]
    wlist = []
    xlist = [s]

    while True:
        rs, ws, es = select.select(rlist, wlist, xlist)
        # print(len(rs), len(ws), len(es))
        for r in rs:
            if r is s:
                c, addr = r.accept()
                print("Client %s:%s connected" % addr)
                rlist.append(c)
                massage_queue[c] = queue.Queue()

            else:
                try:
                    # 如果不是连接请求，直接获取数据，进行处理
                    # data格式：'标示位 信息'
                    data = r.recv(1024).decode()
                    data = data.split()
                    if data[0] == 'R':
                        if do_reg(cur, data):
                            db.commit()
                            msg = 'ok'
                            massage_queue[r].put(msg)
                        else:
                            msg = 'fail'
                            massage_queue[r].put(msg)

                    elif data[0] == 'O':
                        send_msg = do_history()
                        massage_queue[r].put(send_msg)

                    elif data[0] == 'Q':
                        send_msg = do_quit()
                        massage_queue[r].put(send_msg)
                    # massage_queue[r].put(data)

                    if r not in wlist:
                        wlist.append(r)
                except Exception:
                    rlist.remove(r)
                    # print("Client %s disconnected" % (r.getpeername()))
                    del massage_queue[r]

        for w in ws:
            try:
                if not massage_queue[w].empty():
                    send_msg = massage_queue[w].get()
                    print(send_msg)
                    w.send(send_msg.encode())
                    print(send_msg)

                else:
                    wlist.remove(w)

            except Exception as e:
                # except ConnectionResetError or BrokenPipeError:
                del massage_queue[w]
                wlist.remove(w)
                print("Client %s:%s disconnected" % w.getpeername())

        for e in es:
            pass


if __name__ == '__main__':
    main()

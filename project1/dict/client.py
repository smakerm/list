from socket import *
import sys
import time


# 1.用户注册
def reg(c):

    '''用于用户注册
    '''
    while True:
        name = input("name:")
        passwd = input("password:")
        passwd1 = input("password again:")
        if passwd == passwd1:
            data = "R %s %s"%(name, passwd)
            c.send(data.encode())
        else:
            print("passwords do not match,try again")
            continue
        data = c.recv(128).decode()
        if data == 'ok':
            print('successfully')
            break
        else:
            print("failed")
            continue




# 2.登录  登陆后才能进行其他操作
def login():
    pass

def quit():
    pass
# 3.单词查询
# 		显示 ：    hi   单词解释
# 4.查看历史记录
# 		显示 ：    张三    2018-4-5 12：12：12   hi
# 5.退出

def main():
    if len(sys.argv) != 3:
        print('parm error')
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    c = socket()
    c.connect(ADDR)




    while True:
        print(
            '''
            ===========================
            1.登陆    2.注册    3.退出
            ===========================
            ''')
        opt = input("请输入操作:")
        if opt == '1':
            login()
        elif opt == '2':
            reg(c)
        elif opt =='3':
            quit()
        else:
            print("输入错误请重新输入")





if __name__ == '__main__':
    main()
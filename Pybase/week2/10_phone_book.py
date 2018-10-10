

def write_phone():
    while True:
        name = input("请输入姓名：")
        if not name:
            break
        number = input("请输入电话：")

        with open('phone_book.txt', 'a') as f:
            f.writelines('%s %s\n' %(name, number))

def show_book():
    tab_head = '''
+----------+---------------+
|   name   |   number      |
+----------+---------------+'''
    tab_tail = '''+----------+---------------+'''
    print(tab_head)
    with open('phone_book.txt') as f:
        while True:
            info = f.readline()
            if not info:
                break
            name, number = info.split()
            print('|%s|%s|'%(name.center(10), number.center(15)))
    print(tab_tail)

#write_phone()
show_book()

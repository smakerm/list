import re
import time 
import sys

#匹配具体内容
def reg(data,port):
    pattern = r'^\S+'
    re_obj = re.compile(pattern)
    try:
        head_word = re_obj.match(data).group()
    except Exception:
        return None
    if port == head_word:
        pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
        try:
            match_obj = re.search(pattern,data)
            return match_obj.group(1)
        except Exception:
            return None
    else:
        return None



def main(port):
    fd = open('1.txt','r')
    fd.readline()
    fd.readline()

    while True:
        data = ''
        while True:
            s = fd.readline()
            if s == '\n':
                break 
            if s == '':
                print("search over")
                return
            data += s 
        # 将每段数据传入函数进行匹配
        result = reg(data,port)
        if result:
            print("address is :",result)
            return 
 
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("argv error")
        sys.exit(1)
    main(sys.argv[1])


def get_lines(): 
    L = []
    
    while True:
        n = input("请输入：")
        if n == '':
            break
        L.append(n)
    return L

def print_text(lst):
    for i in enumerate(lst,start = 1):
        print("第%d行：%s" %i)

if __name__ == '__main__':
    print_text(get_lines())

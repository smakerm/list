from student import Student


## 添加学生信息
def input_info(students):
    while True:
        ## 输入学生信息
        name = input('请输入学生姓名：')
        if name == '':
            break
        age = input('请输入学生年龄：')
        score = input('请输入学生成绩：')
        ## 将学生信息写入信息表
        students.append(Student(name, age, score))


## 查看所有学生信息
def output_info(students):
    
    ## 获取姓名最大长度，用来调整格式
    if students != []:
            
        
        ## 输出表头
        line1 = ' ' * 10 + '+' +  '-' * 15 + '+' + '-' * 5 + '+' + '-' * 7 + '+'
        line2 = ' ' * 10 + '|%s|%s|%s|' %('name'.center(15), 'age'.center(5),'score'.center(7))
        
        print(line1)
        print(line2)
        print(line1)

        
        ## 输出表格内容
        for i in students:
#            n, a, s = i.get_info
            print(' ' * 10 + '|%s|%s|%s|' %(i.get_name().center(15),str(i.get_age()).center(5),str(i.get_score()).center(7)))
        
        
        ## 输出最后一行
        print(line1)
    

##  修改学生信息
def update_info(students):
    name = input('请输入学生姓名：')
    for d in students:
        if d.is_exist(name):
            score = int(input('请输入学生成绩：'))
            d.set_score(score)
            print("修改 %s 的成绩为：%d" %(name, score))
    else:
        print('没有此学生')

##  删除学生信息
def delet_student(students):
    name = input('请输入学生姓名：')
    for d in students:
        if d.is_exist(name):
            students.remove(d)
            break
    else:
        print('没有此学生')


##  年龄升序
def sort_by_age_desc(docs):
    L = sorted(docs,key = lambda k : k.get_age())
    output_info(L)

##  年龄降序
def sort_by_age_asc(docs):
    L = sorted(docs,key = lambda k : k.get_age(),
                reverse = True)
    output_info(L)

##  分数升序
def sort_by_score_desc(docs):
    L = sorted(docs,key = lambda k : k.get_score())
    output_info(L)

##  分数降序
def sort_by_score_asc(docs):
    L = sorted(docs,key = lambda k : k.get_score(),
                reverse = True)
    output_info(L)

def save_to_file(docs, filename = 'si.txt'):
    try:
        f = open(filename, 'w')
        for stu in docs:
            stu.write_to_file(f)
        f.close()
    except OSError:
        print("打开文件失败")
        

def read_to_file(filename = 'si.txt'):
    L = []
    try:
        f =open(filename)
        for line in f:
            s =line.rstrip()
            s.split(',')
            name, age, score = s
            age = int(age)
            score = int(score)
            L.append(Student(name, age, score))

        f.close()

    except OSError:
        print("打开文件失败")

    return L

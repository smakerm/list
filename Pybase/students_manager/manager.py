


#students = [] 


##  显示菜单
def show_mune():
    mune = '''
            +---------------------+
            | 1）添加学生信息     |
            | 2）查看所有学生信息 |
            | 3）修改学生信息     |
            | 4）删除学生信息     |
            | 5）以年龄升序排序   |
            | 6）以年龄降序排序   |
            | 7）以成绩升序排序   |
            | 8）以成绩降序排序   |
            | q）退出             |
            +---------------------+
            '''
    print(mune)

##  选择操作
def swith_op(students):
    while True:
        show_mune()
        flag = input("请选择：")

        if flag == '1':
            input_info(students)
        elif flag == '2':
            output_info(students)
        elif flag == '3':
            update_info(students)
        elif flag == '4':
            delet_student(students)
        elif flag == '5':
            sort_by_age_desc(students)
        elif flag == '6':
            sort_by_age_asc(students)
        elif flag == '7':
            sort_by_score_desc(students)
        elif flag == '8':
            sort_by_score_asc(students)
        elif flag == 'q':
            exit(0)
        else:
            print('输入错误')
#        op = {
#            '1': input_info,
#            '2': output_info,
#            '3': update_info,
#            '4': delet_student,
#        }.get(flag, False)
#        if flag == 'q':
#            exit(0)
#        op(students) if op else print('输入错误！')
        
    

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
        students.append(dict(name = name, age = age ,score = score))


## 查看所有学生信息
def output_info(students):
    
    ## 获取姓名最大长度，用来调整格式
    if students != []:
            
        w = max([len(students[i]['name']) for i in range(len(students))])
        w += 2
        
        ## 输出表头
        line1 = ' ' * 10 + '+' +  '-' * w + '+' + '-' * 5 + '+' + '-' * 7 + '+'
        line2 = ' ' * 10 + '|%s|%s|%s|' %('name'.center(w), 'age'.center(5),'score'.center(7))
        
        print(line1)
        print(line2)
        print(line1)

        
        ## 输出表格内容
        for i in students:
            print(' ' * 10 + '|%s|%s|%s|' %(i['name'].center(w),i['age'].center(5),i['score'].center(7)))
        
        
        ## 输出最后一行
        print(line1)
    

##  修改学生信息
def update_info(students):
    name = input('请输入学生姓名：')
    for stu in students:
        if stu['name'] == name:
            index = students.index(stu)
            students[index]['age'] = input('请输入学生年龄：')
            students[index]['score'] = input('请输入学生成绩：')
            break
    else:
        print('没有此学生')

##  删除学生信息
def delet_student(students):
    name = input('请输入学生姓名：')
    for stu in students:
        if stu['name'] == name:
            students.remove(stu)
            break
    else:
        print('没有此学生')


##  年龄升序
def sort_by_age_desc(docs):
    L = sorted(docs,key = lambda k : k['age'])
    output_info(L)

##  年龄降序
def sort_by_age_asc(docs):
    L = sorted(docs,key = lambda k : k['age'],
                reverse = True)
    output_info(L)

##  分数升序
def sort_by_score_desc(docs):
    L = sorted(docs,key = lambda k : k['score'])
    output_info(L)

##  分数降序
def sort_by_score_asc(docs):
    L = sorted(docs,key = lambda k : k['score'],
                reverse = True)
    output_info(L)

##  main() 函数
def main():
    students = [
    		{'name':'xiaozhang','age':'25','score':'97'},
    		{'name':'xiaowang','age':'23','score':'99'},
    		{'name':'xiaoli','age':'19','score':'90'},
    		]
    swith_op(students)




main()

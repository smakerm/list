from student_info import *

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
            | 9) 保存信息到文件   |
            | 10)从文件中读取数据 |
            | q）退出             |
            +---------------------+
            '''
    print(mune)

##  选择操作
def swith_op():
    students = []
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
        elif flag == '9':
            save_to_file(students)
        elif flag == '10':
            students = read_from_file()
        elif flag == 'q':
            exit(0)
        else:
            print('输入错误')



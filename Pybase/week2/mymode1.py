#__all__ 列表  form import *时，只导入__all__列表内的属性

#模块中以 '_' 开头的属性 在from import * 时 不被导入，称为隐藏属性

'''这是文档字符串的标题

这是文档字符串的描述，与标题隔一行
'''

__all__ = ['f1', 'var1']

def f1():
    pass

def _f2():
    pass

var1 = 3.1415
var2 = 'pi'

import re

re_obj = re.compile('abcd',re.I)

l = re_obj.findall("hi,abcd,ABCD,abCD")

print(l)


s = '''hello world
nihao china
'''

l1 = re.findall('.*',s,re.S)
print(l1)


obj = re.search('world$',s,re.M)
print(obj.group())
obj = re.search('^nihao',s,re.M)
print(obj.group())

re_obj = re.compile('''
    (ab)cd
    (?P<word>ef) # This is a group
    ''',re.X)


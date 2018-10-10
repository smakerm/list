import re

obj = re.compile('foo')

iter_obj = obj.finditer('foo,food on the table')

for i in iter_obj:
    print(i.group())

print("**********************")
try:
    m_obj = obj.match('Foo,food on the table')
    print(m_obj.group())
except AttributeError:
    print("match none")

print("**********************")
try:
    m_obj = obj.search('Foo,food on the table')
    print(m_obj.group())
except AttributeError:
    print("match none")

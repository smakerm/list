import re

pattern = r'\w+'

obj = re.compile(pattern)

l = obj.findall('hello world')

print(l)

l1 = re.split(r'\s+','hello world ni hao ')

print(l1)


l2 = re.sub(r'[A-Z]', '##', 'Hi,Jam.I am Ice', count=2)
print(l2)
l2 = re.subn(r'[A-Z]', '##', 'Hi,Jam.I am Ice', count=2)
print(l2)



import re

re_obj = re.compile('(ab)cd(?P<dog>ef)')

match_obj = re_obj.search('hi,abcdefghijk')

print('re:',match_obj.re)
print('pos:',match_obj.pos)
print('endpos:',match_obj.endpos)
print('lastgroup:',match_obj.lastgroup)
print('lastindex:',match_obj.lastindex)


#print("search: ",match_obj.group())

print("****************************")

print('start():',match_obj.start())
print('end():',match_obj.end())
print('span():',match_obj.span())
print('group():',match_obj.group())
print('group(1):',match_obj.group(1))
print('group(2):',match_obj.group(2))
print('groups:',match_obj.groups())
#for i in match_obj.groups()


print('groupdict():',match_obj.groupdict())

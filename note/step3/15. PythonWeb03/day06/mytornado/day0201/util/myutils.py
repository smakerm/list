import hashlib
from uuid import uuid4


def mymd5(orginal):

    md = hashlib.md5()
    md.update(orginal.encode('utf8'))
    m = md.hexdigest()
    return m

#生成ｕｕｉｄ字符串
def myuuid():
    u = uuid4()
    md = hashlib.md5()
    md.update(u.bytes)
    m = md.hexdigest()
    return m


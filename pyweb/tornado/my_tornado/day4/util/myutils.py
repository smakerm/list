import hashlib
from uuid import uuid4


def mymd5(orginal):
    md = hashlib.md5()
    md.update(orginal.encode('utf8'))
    return md.hexdigest()

def myuuid():
    u = uuid4()
    return u.hex
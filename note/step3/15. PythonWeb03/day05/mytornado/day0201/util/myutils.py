import hashlib


def mymd5(orginal):

    md = hashlib.md5()
    md.update(orginal.encode('utf8'))
    m = md.hexdigest()
    return m
import hashlib

CHUCKSIZE = 2048

def hashfile(filename):

    h = hashlib.sha256()
    with open(filename, 'rb') as f:
        while True:
            chuck = f.read(CHUCKSIZE)
            if not chuck:
                break
            h.update(chuck)
    return h.hexdigest()

print(hashfile('maxmin.py'))
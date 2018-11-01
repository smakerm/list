from day4.util.myutils import myuuid

session = {}

class MySession:
    def __init__(self, handler):
        self.handler = handler

    def __getitem__(self, key):
        id = self.handler.get_cookie('cookieid')
        if id:
            info = session.get(id)
            if info:
                return info.get(key, None)
            else:
                return None
        else:
            return None

    def __setitem__(self, key, value):

        id = self.handler.get_cookie('cookieid')
        if id:
            info = session.get(id ,None)
            if info:
                info[key] = value
            else:
                d = dict()
                d[key] = value
                session[id] = d
        else:
            d = dict()
            d[key] = value
            id = myuuid()
            session[id] = d
            self.handler.set_cookie('cookieid',id,expires_days=10)
class MyList(list):
    def insert_head(self, value):
        '''以下实现头插'''
        self.insert(0, value)


L = MyList(range(1, 5))
print(L)
L.append(5)
print(L)
L.insert_head(0)
print(L)

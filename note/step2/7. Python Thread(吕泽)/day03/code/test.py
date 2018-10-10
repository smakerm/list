class A(object):
    def __init__(self,value):
        self.value = value 

def Value(s,value):
    obj = A(value)
    return obj 


money = Value('i',2000)

money.value

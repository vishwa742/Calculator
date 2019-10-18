
def addition(a,b):
    return a+b

class Calc:
    result=0

    def __init__(self):
        x = 0
        self.result = x;
        pass

    def add(self, a, b):
        self.result = a+b
        return addition(a,b)
#def subtraction(a,b):
    #return a-b

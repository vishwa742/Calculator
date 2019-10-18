
def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

class Calc:
    result=0

    def __init__(self):
        x = 0
        self.result = x;
        pass

    def add(self, a, b):
        self.result = addition(a,b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a,b)
        return self.result


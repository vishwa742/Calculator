import math

def addition(a,b):
    return a+b

def subtraction(a,b):
    return b-a

def multiplication(a,b):
    return a*b

def division(a,b):
    return float(a)/float(b)

def squared(a):
    return  a*a

def squareroot(a):
    return  math.sqrt(a)

class Calc:
    rest=0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a,b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a,b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a,b)
        return self.result

    def divide(self, a, b):
        self.result = division(a,b)
        return self.result

    def square(self,a):
        self.result = squared(a)
        return self.result

    def root(self,a):
        self.result = squareroot(a)
        return self.result
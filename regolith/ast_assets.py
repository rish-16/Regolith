from pprint import pprint
from rply.token import BaseBox

class Program(BaseBox):
    def __init__(self, token_list):
        self.token_list = token_list
        
    def eval(self):
        return [i.eval() for i in self.token_list]

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value
        
class String(BaseBox):
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return str(self.value).strip('\"')
        
class Comment(BaseBox):
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        pass
        
class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()
        
class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()
        
class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()
        
class Mod(BinaryOp):
    def eval(self):
        return self.left.eval() % self.right.eval()        
        
class Pow(BinaryOp):
    def eval(self):
        return self.left.eval() ** self.right.eval()        
        
class Print():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        print (self.value.eval())
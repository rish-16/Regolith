class Number:
    def __init__(self, val):
        self.val = val
        
    def eval(self):
        return int(self.val)
        
class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()
        
class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()
        
class Print:
    def __init__(self, val):
        self.val = val
        
    def eval(self):
        print (self.val.eval())
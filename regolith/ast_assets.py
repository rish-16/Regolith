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

"""
Conditional types
IF

IF 
ELSE

IF 
ELSE IF ... ELSE IF
ELSE
"""
class T1_Conditional(BaseBox):
    def __init__(self, expression1, block1):
        self.expression1 = expression1
        self.block1 = block1
    
    def eval(self):
        if (self.expression1.eval() == True):
            return [i.eval() for i in self.block1]
            
class T2_Conditional(BaseBox):
    def __init__(self, expression1, block1, block2):
        self.expression1 = expression1
        self.block1 = block1
        self.block2 = block2
    
    def eval(self):
        if (self.expression1.eval() == True):
            return [i.eval() for i in self.block1]
        else:
            return [i.eval() for i in self.block2]
            
class T3_Conditional(BaseBox):
    def __init__(self, expressions, blocks, def_block):
        """
        Indices of conditional expressions match with indices of blocks
        """
        self.expressions = expressions
        self.blocks = blocks
        self.def_block = def_block # ELSE block
    
    def eval(self):
        b_id = 0
        for cond in self.expressions:
            if cond.eval() == True:
                return self.blocks[b_id].eval()
            b_id += 1
            
        return [i.eval() for i in self.def_block] # runs when no other condition is met
        
class Comment(BaseBox):
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        pass
        
class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

# RAW OPERATIONS
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
        
# COMPARATIVES        
class GT(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()
        
class LT(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()
        
class GTE(BinaryOp):
    def eval(self):
        return self.left.eval() >= self.right.eval()
        
class LTE(BinaryOp):
    def eval(self):
        return self.left.eval() <= self.right.eval()        
        
class EQ(BinaryOp):
    def eval(self):
        return self.left.eval() == self.right.eval()
        
class Print():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        print (self.value.eval())
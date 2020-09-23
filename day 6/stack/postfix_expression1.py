class Evaluate:

    def __init__(self,capacity):
        self.capacity = capacity
        self.top = -1
        self.stack = []

    def isempty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        if not self.isempty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "$"
    
    def push(self,i):
        self.top += 1
        self.stack.append(i)
    
    def evalpostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
        return int(self.pop())

exp = "231*+9-"
obj = Evaluate(len(exp))
print(obj.evalpostfix(exp))
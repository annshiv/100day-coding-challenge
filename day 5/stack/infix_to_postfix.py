class conversion:

    def __init__(self,capcity):
        self.top = -1
        self.capcity = capcity
        self.stack = []
        self.postfix = []
        self.priority = {'+' : 1,'-': 1,'*':2,'/':2,'^':3}

    def isempty(self):
        return True if self.top == -1 else False
    
    def pop(self):
        if not self.isempty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "$"
    
    def peek(self):
        return self.stack[-1]

    def push(self,op):
        self.top += 1
        self.stack.append(op)
    
    def isoperand(self,ch):
        return ch.isalpha()
    
    def notgrater(self,i):
        try:
            a = self.priority[i]
            b = self.priority[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
    
    def infixtopostfix(self,exp):
        for i in exp:
            if self.isoperand(i):
                self.postfix.append(i)
            
            elif i == '(':
                self.push(i)
            
            elif i == ')':
                while ((not self.isempty()) and self.peek() != '('):
                    a = self.pop()
                    self.postfix.append(a)
                if (not self.isempty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while((not self.isempty()) and self.notgrater(i)):
                    self.postfix.append(self.pop())
                self.push(i)
        while not self.isempty():
            self.postfix.append(self.pop())
            
        print("".join(self.postfix))

exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = conversion(len(exp)) 
obj.infixtopostfix(exp)
class Evaluate:

    def __init__(self):
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
            try:
                self.push(int(i))
            except ValueError:
                val1 = self.pop()
                val2 = self.pop()
                switcher = {'+':val2 + val1, '-':val2 - val1,'*':val2 * val1,'/':val2 / val1, '^': val2 ** val1}
                self.push(switcher.get(i))
        return int(self.pop())

str ='100 200 + 2 / 5 * 7 +'
  
# splitting the given string to obtain  
# integers and operators into a list


strconv = str.split(' ') 
obj = Evaluate()
print(obj.evalpostfix(strconv))
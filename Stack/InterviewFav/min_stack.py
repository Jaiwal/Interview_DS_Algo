#solution 1: brute force 

class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




#solution2: store pair instead of single element 
class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        if not self.stack:
            #empty currently
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))
        

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop(-1)
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#solution3: there is one more
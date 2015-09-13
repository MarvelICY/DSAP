#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Implementation of Min Stack

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class MinStack:
    # @param x, an integer
    # @return an integer
    # tuple implemetation:MLE

    def __init__(self):
        self.list = []
        self.min = 2147483647   #INT_MAX

    def push(self, x):
        if x < self.min:
            self.list.append((x,x))
            self.min = x
        else:
            self.list.append((x,self.min))
        
    # @return nothing
    def pop(self):
        self.list.pop()
        if len(self.list) == 0:
            self.min = 2147483647
        else:
            self.min = self.getMin()
        

    # @return an integer
    def top(self):
        return self.list[len(self.list)-1][0]

    # @return an integer
    def getMin(self):
        return self.list[len(self.list)-1][1]


class MinStack2:
    # @param x, an integer
    # @return an integer
    # single stack, record the 

    def __init__(self):
        self.list = []
        self.min = 0  

    def push(self, x):
        if self.list == []:
            self.list.append(0)
            self.min = x
        else:
            temp = x - self.min
            self.list.append(temp)
            if temp < 0:
                self.min = x
        
    # @return nothing
    def pop(self):
        length = len(self.list)
        if length == 0:
            return
        temp = self.list[length-1]
        if temp < 0:
            self.min = self.min - temp
        self.list.pop()

    # @return an integer
    def top(self):
        temp = self.list[len(self.list)-1]
        if temp < 0:
            return self.min
        else:
            return temp + self.min

    # @return an integer
    def getMin(self):
        return self.min


class MinStack3:
    # @param x, an integer
    # @return an integer
    # single stack, record the 

    def __init__(self):
        self.list = []
        self.min = 0  

    def push(self, x):
        if self.list == []:
            self.list.append(0)
            self.min = x
        else:
            self.list.append(x - self.min)
            if x - self.min < 0:
                self.min = x
        
    # @return nothing
    def pop(self):
        if len(self.list) == 0:
            return
        if self.list[len(self.list)-1] < 0:
            self.min = self.min - self.list[len(self.list)-1]
        self.list.pop()

    # @return an integer
    def top(self):
        if self.list[len(self.list)-1] < 0:
            return self.min
        else:
            return self.list[len(self.list)-1] + self.min

    # @return an integer
    def getMin(self):
        return self.min


#----------------------------SELF TEST----------------------------#

def main():
    stack = MinStack2()
    stack.push(3)  
    stack.push(4)
    print stack.getMin()
    stack.push(2)
    print stack.getMin()
    stack.push(1)
    print stack.getMin()  
    stack.pop()  
    print stack.getMin()  
    stack.pop()
    print stack.getMin()  
    stack.push(5)
    print stack.getMin()  
    stack.push(0)
    print stack.getMin()  
    pass
            
if __name__ == '__main__': 
    main()
    
    

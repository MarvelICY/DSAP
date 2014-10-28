#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Implementation of Stack 

Created on: Oct 28, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def clear(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def get_top(self):
        return self.items[len(self.items)-1]


#----------------------------SELF TEST----------------------------#

def main():
    s=Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.get_top())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    pass
            
if __name__ == '__main__': 
    main()
    
    

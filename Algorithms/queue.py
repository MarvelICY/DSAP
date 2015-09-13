#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Implementation of Queue 

Created on: Oct 28, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def clear(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def get_head(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[len(self.items)-1]


#----------------------------SELF TEST----------------------------#

def main():
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)
    print(q.dequeue())
    print(q.items)
    print(q.size())
            
if __name__ == '__main__': 
    main()
    
    

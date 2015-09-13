#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Implementation of Deque

Created on: Oct 29, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Deque(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def clear(self):
        self.items = []

    def add_front(self,item):
        self.items.append(item)

    def add_rear(self,item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def get_head(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[len(self.items)-1]


#----------------------------SELF TEST----------------------------#

def main():
    q = Deque()
    q.add_front('hello')
    q.add_rear('dog')
    q.add_front(3)
    print(q.items)
    print(q.remove_rear())
    print(q.items)
    print(q.remove_front())
            
if __name__ == '__main__': 
    main()
    
    

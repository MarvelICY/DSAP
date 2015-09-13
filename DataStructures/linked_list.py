#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Implementation of Linked List 
Including SinLinkedList, SinCycLinkedList, DouCycLinkedList

Created on: Oct 29, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Node(object):
    '''
    Definiton of the node of the single linked list.
    '''
    def __init__(self,initdata):
        #prevent external access
        self.__data = initdata 
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self,data):
        self.__data = data

    def set_next(self,next_node):
        self.__next = next_node

class DouNode(object):
    '''
    Definiton of the node of the double linked list.
    '''
    def __init__(self,initdata):
        self.__data = initdata
        self.__next = None
        self.__prev = None

    def get_data(self):
        return self.__data

    def get_prev(self):
        return self.__prev

    def get_next(self):
        return self.__next

    def set_data(self,data):
        self.__data = data

    def set_prev(self,prev_node):
        self.__next = prev_node

    def set_next(self,next_node):
        self.__next = next_node


class SinLinkedList(object):
    '''
    Implementation of Single Linked List.
    '''
    def __init__(self):
        self.head = None

    def is_empty(self): 
        return self.head == None

    def add(self,item):
        temp_node = Node(item)
        temp_node.set_next(self.head)
        self.head = temp_node

    def remove(self,item):
        previous = None
        current = self.head
        while current != None:
            if current.get_data() == item:
                previous.set_next(current.get_next())
                return True
            previous = current
            current = current.get_next()                
        return False

    def search(self,item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()



class SinCycLinkedList(object):
    '''
    Implementation of Single Cicular Linked List.
    '''
    def __init__(self):
        self.head = Node(None)
        self.head.set_next(self.head)

    def is_empty(self): 
        # check if the reference of the head node leads to itself
        return self.head.get_next() == self.head

    def add(self,item):
        temp_node = Node(item)
        temp_node.set_next(self.head.get_next())
        self.head.set_next(temp_node)

    def remove(self,item):
        previous = self.head
        while previous.get_next() != self.head:
            current = previous.get_next()
            if current.get_data() == item:
                previous.set_next(current.get_next())
                return True
            previous = previous.get_next()
        return False

    def search(self,item):
        current = self.head.get_next()
        while current != self.head:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def size(self):
        count = 0
        current = self.head.get_next()
        while current != self.head:
            count += 1
            current = current.get_next()

class DouCycLinkedList(object):
    '''
    Implementation of Double Linked List
    '''
    def __init__(self):
        self.head = DouNode(None)
        self.head.set_next(self.head)
        self.head.set_prev(self.head)

    def is_empty(self): 
        # check if the reference of the head node leads to itself
        return self.head.get_next() == self.head

    def add(self,item):
        #update the node referrence in the linked list
        temp_node = DouNode(item)
        next_node = head.get_next()
        temp_node.set_next(self.head.get_next())
        temp_node.set_prev(self.head)
        next_node.set_prev(temp_node)
        self.head.set_next(temp_node)

    def remove(self,item):
        #update the node referrence in the linked list
        previous = self.head
        while previous.get_next() != self.head:
            current = previous.get_next()
            if current.get_data() == item:
                previous.set_next(current.get_next())
                next_node = current.get_next()
                next_node.set_prev(previous)
                return True
            previous = previous.get_next()
        return False

    def search(self,item):
        current = self.head.get_next()
        while current != self.head:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def size(self):
        count = 0
        current = self.head.get_next()
        while current != self.head:
            count += 1
            current = current.get_next()



#----------------------------SELF TEST----------------------------#

def main():
    scl = SinCycLinkedList()
    print(scl.is_empty())
    scl.add('7895')
    scl.add('hello')
    scl.add(0.5)
    scl.add('dog')
    print(scl.is_empty())
    print(scl.search('7895'))
    print(scl.remove('hello'))
            
if __name__ == '__main__': 
    main()
    
    

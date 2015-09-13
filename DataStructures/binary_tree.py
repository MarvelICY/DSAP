#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Implementation of Binary Tree 

Created on: Nov 3, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class BinaryTree(object):
    def __init__(self,val):
        self.key = val
        self.left_child = None
        self.right_child = None

    def insert_left(self,node):
        if self.left_child == None:
            self.left_child = BinaryTree(node)
        else:
            new_node = BinaryTree(node)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self,node):
        if self.right_child == None:
            self.right_child = BinaryTree(node)
        else:
            new_node = BinaryTree(node)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root(self,obj):
        self.key = obj

    def get_root(self):
        return self.key



#----------------------------SELF TEST----------------------------#

def main():
    r = BinaryTree('a')
    print(r.get_root())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root())
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_root())
    r.get_right_child().set_root('hello')
    print(r.get_right_child().get_root())
            
if __name__ == '__main__': 
    main()
    
    

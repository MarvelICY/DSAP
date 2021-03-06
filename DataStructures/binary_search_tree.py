#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Implementation of Binary Search Tree 

Created on: Nov 13, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class BinarySearchTree(object):
    def __init__(self,val):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


class TreeNode(object):
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.val = val
        self,left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return parent and self.parent.left_child == self

    def is_right_child(self):
        return parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child or self.right_child

    def replace_node_data(self,key,val,lc,rc):
        self.key = key
        self.val = val
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self


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
    
    

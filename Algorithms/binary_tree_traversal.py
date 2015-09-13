#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: different way to traverse the binary tree

Created on: Nov 6, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
import sys
sys.path.append("..") 
from DataStructures.binary_tree import BinaryTree

def preorder(tree):
    if tree is not None:
        print(tree.get_root())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def inorder(tree):
    if tree is not None:
        inorder(tree.get_left_child())
        print(tree.get_root())
        inorder(tree.get_right_child())

def postorder(tree):
    if tree is not None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root())



#----------------------------SELF TEST----------------------------#

def main():
    r = BinaryTree('0')
    r.insert_left('1')
    r.insert_right('2')
    rl = r.get_left_child()
    rc = r.get_right_child()
    rl.insert_left('3')
    rl.insert_right('4')
    rc.insert_left('5')
    rc.insert_right('6')

    preorder(r)
    print('---')
    inorder(r)
    print('---')
    postorder(r)

    pass
            
if __name__ == '__main__': 
    main()
    
    
    
#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Evluate the arithmetic expression using Infix and Postfix Expression and Stack 
Only for single integers

Created on: Oct 28, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#
import sys
sys.path.append("..") 
from DataStructures.stack import Stack

def infix_to_postfix(infixExp):
    priority = {}
    priority['('] = 1
    priority['+'] = 2
    priority['-'] = 2
    priority['*'] = 3
    priority['/'] = 3

    expStack = Stack()
    postfixExp = []
    tokenList = infixExp.split()

    for token in tokenList:
        if token in '1234567890' \
                or token in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz': 
            postfixExp.append(token)
        elif token == '(':
            expStack.push(token)
        elif token == ')':
            topToken = expStack.pop()
            while topToken != '(':
                postfixExp.append(topToken)
                topToken = expStack.pop()
        else:
            while (not expStack.is_empty()) \
                    and (priority[expStack.get_top()] >= priority[token]):
                postfixExp.append(expStack.pop())
            expStack.push(token)

    while not expStack.is_empty():
        postfixExp.append(expStack.pop())

    result = ' '.join(postfixExp)
    return result

def postfix_eval(postfixExp):
    expStack = Stack()
    tokenList = postfixExp.split()

    for token in tokenList:
        if token in '0123456789':
            expStack.push(token)
        else:
            operator1 = float(expStack.pop())
            operator2 = float(expStack.pop())
            if token == '+':
                result = operator1 + operator2
            elif token == '-':
                result = operator1 - operator2
            elif token == '*':
                result = operator1 * operator2
            elif token == '/':
                result = operator1 / operator2
            expStack.push(result)

    return expStack.pop()

def evaluation(expression):
    postfix = infix_to_postfix(expression)
    result = postfix_eval(postfix)
    return result



#----------------------------SELF TEST----------------------------#

def main():
    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(postfix_eval('7 8 + 3 2 + /'))
    print(evaluation('2 * 3 + 6 * 7'))
    print(evaluation('9 + 3 * 5 / ( 7 - 4 )'))
    pass

if __name__ == '__main__':
    main()
    
    

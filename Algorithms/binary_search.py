#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: Binary search

Created on: Oct 24, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class Solution:
    # the array must be sorted from small to large order
    def binary_search(self, num, value):
        left = 0
        right = len(num) - 1

        while left <= right:
            middle = left + ((right-left)>>1) #Important,calculate middle index without overflow.
            if num[middle] > value:
                right = middle - 1   #update right side
            elif num[middle] < value:
                left = middle + 1    #update left side
            else:
                return middle
        return -1

#----------------------------SELF TEST----------------------------#

def main():
    #test_array = [0]
    test_array = [1,2]
    #test_array = [1,2,3,4]
    #test_array = [2,4,5,6,7,8,9]
    value = 4
    solution = Solution()
    print solution.binary_search(test_array,value)
    pass
            
if __name__ == '__main__': 
    main()
    
    
    
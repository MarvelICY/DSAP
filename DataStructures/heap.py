#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Implementation of MinBinHeap 

Created on: Nov 12, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class MinBinHeap(object):
    # implemention using list
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self,element):
        self.heap_list.append(element)
        self.current_size += 1
        self.prec_up(self.current_size)
   
    def prec_down(self,i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i],self.heap_list[mc] = self.heap_list[mc],self.heap_list[i]
            i = mc    

    def min_child(self,i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[2*i] < self.heap_list[2*i+1]:
                return i * 2
            else:
                return i * 2 + 1
        

    def prec_up(self,i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i],self.heap_list[i//2] = self.heap_list[i//2],self.heap_list[i]
            i = i // 2 

    def del_min(self):
        result = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.prec_down(1)

        return result

    def build_heap(self,list):
        i = len(list) // 2
        self.current_size = len(list)
        self.heap_list = [0] + list[:]

        while i > 0:
            self.prec_down(i)
            i -= 1

    def is_empty(self):
        return self.heap_list == [0]

    def size(self):
        return self.current_size

    def find_min(self):
        return self.heap_list[1]


#----------------------------SELF TEST----------------------------#

def main():
    bh = MinBinHeap()
    bh.insert(5)
    print bh.heap_list
    bh.insert(7)
    print bh.heap_list
    bh.insert(3)
    print bh.heap_list
    bh.insert(11)
    print bh.heap_list

    print(bh.del_min())

    print(bh.del_min())

    print(bh.del_min())

    print(bh.del_min())
            
if __name__ == '__main__': 
    main()
    
    

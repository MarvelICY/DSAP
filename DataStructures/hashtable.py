#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Implementation of HashTable using remainder function

Created on: Nov 1, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

class HashTable(object):
    def __init__(self,size):
        self.items = []
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,value):
        #rehash for collision
        hash_value = self.hash_function(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key 
            self.data[hash_value] = value
        esle:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data    #update
            else:
                next_slot = self.rehash(hash_value)
                while self.slots[next_slot] is not None and \
                    self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key 
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = data #update

    def hash_function(self,key):
        #remainder hash function
        return key%self.size

    def rehash(self, old_hash_value):
        #remainder rehash function
        return (old_hash_value+1)%self.size

    def get(self,key,value):
        start_slot = self.hash_function(key)
        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None \
                and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self,key):
        #used as HashTable['key']
        return self.get(key)

    def __setitem__(self,key,data):
        #used as HashTable['key'] = value
        self.put(key,value)




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
    
    

#!usr/bin/python
# -*- coding:UTF-8 -*-

'''
Introduction: 
Implementation of Sort Method

Created on: Oct 28, 2014

@author: ICY
'''

#-------------------------FUNCTION---------------------------#

def bubble_sort(list):
    #O(n^2)
    for sort_position in range(len(list)-1,0,-1):     #traverse the list reversively
        for i in range(0,sort_position):      #bubble exchange
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

def selection_sort(list):
    #O(n^2)
    for sort_position in range(len(list)-1,0,-1):
        position_max = 0
        for i in range(0,sort_position+1):
            if list[i] > list[position_max]:
                position_max = i
        temp = list[sort_position]
        list[sort_position] = list[position_max]
        list[position_max] = temp
    return list

def insertion_sort(list):
    #O(n^2)
    for index in range(0,len(list)):    #sort from head
        insert_value = list[index]
        position = index
        while position > 0 and list[position-1] > insert_value:   #leave a slot for inserted data
            list[position] = list[position-1]
            position = position - 1
        list[position] = insert_value
    return list

def merge_sort(list):
    #O(nlgn)
    #devide and conquer
    print('Splitting:',list)
    if len(list) > 1:   
        mid = len(list) // 2
        left_list = list[:mid]
        right_list = list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        #merge
        #list here indicate the left_list or right_list above
        left_index = 0
        right_index = 0
        index = 0
        while left_index < len(left_list) \
                 and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                list[index] = left_list[left_index]
                left_index += 1
            else:
                list[index] = right_list[right_index]
                right_index += 1
            index += 1

        while left_index < len(left_list):
            list[index] = left_list[left_index]
            left_index += 1
            index += 1

        while right_index < len(right_list):
            list[index] = right_list[right_index]
            right_index += 1
            index += 1

    print('Merging:',list)

def quick_sort(list,first=0,last=-1):
    #O(nlgn)
    #devide and conquer
    if last == -1:
        last = len(list)-1
    if first < last:
        pivot = list[first]
        left_index = first + 1
        right_index = last
        done = False 
        while not done:
            #skip the values smaller than pivot on the left side
            while left_index <= right_index \
                    and list[left_index] <= pivot:
                    left_index += 1
            #skip the values bigger than pivot on the right side
            while right_index >= left_index \
                    and list[right_index] >= pivot:
                    right_index -= 1
            #change the elements
            if left_index > right_index:
                done = True
            else:
                temp = list[left_index]
                list[left_index] = list[right_index]
                list[right_index] = temp
        #change the pivot to the middle
        temp = list[first]
        list[first] = list[right_index]     #note that now right_index < left_index
        list[right_index] = temp
        print right_index
        #recursively sort
        quick_sort(list,first,right_index-1)
        quick_sort(list,right_index+1,last)


#----------------------------SELF TEST----------------------------#

def main():
    test_array = [100,89,36,27,49,4,55,187,267,1,4,0]

    #bubble_sort(test_array)
    #selection_sort(test_array)
    #insertion_sort(test_array)
    #merge_sort(test_array)
    quick_sort(test_array)
    print test_array
            
if __name__ == '__main__': 
    main()
    
    

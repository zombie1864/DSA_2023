from audioop import reverse
from typing import Any, Dict, List, Optional, Set, Tuple, Union
import sys
import pprint
from datetime import datetime 
from inspect import getmembers, isfunction
'''  
The inspect module provides several useful functions to help get information about live objects such as modules, classes, methods, functions, tracebacks, frame objects, and code objects. For example, it can help you examine the contents of a class, retrieve the source code of a method, extract and format the argument list for a function, or get all the information you need to display a detailed traceback.

The getmembers() function retrieves the members of an object such as a class or module. The functions whose names begin with “is” are mainly provided as convenient choices for the second argument to getmembers(). Return all the members in a list of (name, value). If the optional predicate argument—which will be called with the value object of each member—is supplied, only members for which the predicate returns a true value are included.
'''


def main():
    ''' Main will ask you which algo to exec '''
    print('Choose which algo to execute:\n')
    public_func_list = [
        member[0] for member in getmembers(sys.modules[__name__], isfunction) 
        if member[0] != 'main' and member[0] != 'getmembers' and member[0] != 'isfunction' and member[0][0] != '_'
    ]
    dict_of_avail_funcs = dict(enumerate(public_func_list))
    pprint.pprint(dict_of_avail_funcs) # prints a nicely formatted dict in terminal 
    exec_func = int(input('\nPick a number from the dict: '))
    print(f'\nExecuting order {exec_func}:\n')
    eval(dict_of_avail_funcs[exec_func] + '()')



def prob_01_longest_cp(): # RECORD_TIME:  BEST_TIME: 
    ''' find longest common prefix str in a list[str], if none return empty str 
	'''
    res_1 = _longest_cp(["flower","flow","flight"]) 
    res_2 = _longest_cp(["dog","racecar","car"]) 
    print('pass' if res_1 == 'fl' else res_1)  #=> 'fl'
    print('pass' if res_2 == '' else res_2) #=> ''


def _longest_cp(words:List[str]) -> str:
    '''
    '''



def prob_02_plus_one(): 
    '''  Given a list[int] inc the last int by one and return the resulting list[int]
    '''
    res_1 = _plus_one([1, 2, 3])
    res_2 = _plus_one([9])
    res_3 = _plus_one([9, 9, 9])

    print('pass' if res_1 == [1, 2, 4] else res_1)
    print('pass' if res_2 == [1, 0] else res_2)
    print('pass' if res_3 == [1, 0, 0, 0] else res_3)


def _plus_one(nums:List[int]) -> List[int]: 
    '''  
    '''

    

def prob_03_len_of_last_word(): 
    ''' Given a str consisting of words and spaces, return the len of the last word
    '''
    res_1 = _len_of_last_word('hello world')
    res_2 = _len_of_last_word('   fly me   to   the moon  ')
    print('pass' if res_1 == 5 else res_1) 
    print('pass' if res_2 == 4 else res_2)


def _len_of_last_word(sent:str) -> int: 
    '''  
    '''


def prob_04_top_k_frequent_elements():
    '''  Given a List[int] and a int k, return the k most frequent el
    '''
    res_1 = _top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2) 
    res_2 = _top_k_frequent_elements([3, 3, 3, 1, 1, 1, 2, 2, 2, 4], 3)
    res_3 = _top_k_frequent_elements([1, 2, 3, 4], 1)
    ans_1, ans_2, ans_3 = [1, 2], [1, 2, 3], [1]
    print('pass' if res_1 == ans_1 else res_1)
    print('pass' if res_2 == ans_2 else res_2)
    print('pass' if res_3 == ans_3 else res_3)

def _top_k_frequent_elements(nums:List[int], k:int) -> List[int]: 
    '''  
    '''



def prob_05_linked_list_rm_dups():
    ''' You have a list of random names you wish to alphabetize. In memory there 
    are 2 ways to do this - first with an array and second with linked list. 
    Using an arr has limitations that linked list overcomes, which are size and inefficient 
    insertion/deletion operations. The size limitation is tied to 
    low-level/hardware limitation. Arrs have a fixed size determined at the time of creation. 
    If the initial arr size is too small it leads to overflow and requires resizing 
    which is time-consuming and memory intensive. A linked list can grow dynamically 
    eliminating the need for pre-allocation. The insertion/deletion of entries in array 
    take O(n) where linked-list takes O(1) by using pointers to locate data. 
    Linked-list use pointers that points to data in memory 
        | data | addr | -> | data | addr | 
    and do not need to be adjacent like an array--existing in "cyber space". 
    B/c of the vectorization nature of a linked-list their exist different types of linked list. 

        Single linked list: Navigation is forward only 
        Double linked list: forward and backward navigation 
        circular linked list: last el is linked to the first el

    Given the head of a sorted linked list, delete all duplication and return the linked list sorted. 
    '''
    res_1 = _linked_list_rm_dups([1, 1, 2])
    res_2 = _linked_list_rm_dups([2, 2, 2, 3, 4, 9, 9])
    print('pass' if _linked_list_2_arr(res_1) == [1, 2] else _linked_list_2_arr(res_1))
    print('pass' if _linked_list_2_arr(res_2) == [2, 3, 4, 9] else _linked_list_2_arr(res_2))



class LinkList: 
    def __init__(self, val=0, nxt=None): 
        self._val = val 
        self._nxt = nxt 


def _linked_list_rm_dups(nums:List[int]) -> List[int]: 
    '''  
    '''



def _linked_list_2_arr(head): 
    res, curr = [], head 

    while curr: 
        res.append(curr._val)
        curr = curr._nxt

    return res 







if __name__ == '__main__':

    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n')
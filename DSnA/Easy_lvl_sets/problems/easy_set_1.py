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


class Root:
    def __init__(self, val=0, left=None, right=None): 
        self._val   = val 
        self._left  = left 
        self._right = right 




def prob_00_longest_cp(): # RECORD_TIME:  BEST_TIME: 
    ''' find longest common prefix str in a list[str], if none return empty str 
	'''
    res_1 = _longest_cp(["flower","flow","flight"]) 
    res_2 = _longest_cp(["dog","racecar","car"]) 
    print('pass' if res_1 == 'fl' else res_1)  #=> 'fl'
    print('pass' if res_2 == '' else res_2) #=> ''


def _longest_cp(words:List[str]) -> str:
    '''
    '''
    if not words:
        return ''

    words.sort() # Sort words alphabetically 2 bring potential common prefixes together
    first_word      = words[0]
    last_word       = words[-1]
    common_prefix   = []
    
    for i in range(len(first_word)): #itr(first_word)
        if i < len(last_word) and first_word[i] == last_word[i]:
            common_prefix.append(first_word[i])
        else:
            break

    return ''.join(common_prefix)



def prob_01_plus_one(): 
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
        VAR joined_str_int = ''.join(map(str, nums))
        VAR res_int = int(joined_str_int) 
        res_int += 1 
        RETURN [int(digit) for digit in str(res_int)]
    '''
    joined_str_int = ''.join(map(str, nums)) 
    res_int = int(joined_str_int)
    res_int += 1 
    return [int(digit) for digit in str(res_int)]
    

def prob_02_len_of_last_word(): 
    ''' Given a str consisting of words and spaces, return the len of the last word
    '''
    res_1 = _len_of_last_word('hello world')
    res_2 = _len_of_last_word('   fly me   to   the moon  ')
    print('pass' if res_1 == 5 else res_1) 
    print('pass' if res_2 == 4 else res_2)


def _len_of_last_word(sent:str) -> int: 
    '''  
        VAR words = str.split(' ')
        itr_rev(words, word)
            IF word == ' '
                CONTINUE 
            ELSE 
                RETURN len(word)
        RETURN 0
    '''
    words = sent.split() 

    if words: 
        return len(words[-1])
    else: 
        return 0


def prob_03_top_k_frequent_elements():
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
        VAR freq = {} # {'1': 3, '2': 2, '3': 1}, {'1': 3, '2': 3, '3': 3, '4': 1}
        itr(sorted(nums), num) 
            IF num IN freq 
                freq[num] += 1 
            ELSE 
                freq[num] = 1
        VAR sorted_dict = dict(sorted(freq.items()))
        RETURN sorted([int(k) for k IN range(sorted(sorted_dict.keys()))])
    '''
    freq = {} 
    
    for num in sorted(nums): 
        if num in freq: 
            freq[num] += 1
        else: 
            freq[num] = 1
    sorted_dict = sorted(freq.keys(), key=lambda item: freq[item], reverse=True)
    
    return sorted(sorted_dict[:k])


def prob_04_linked_list_rm_dups():
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
    head = _arr_2_linked_list(nums) 

    if not head or not head._nxt: 
        return head 
    
    curr = head 

    while curr._nxt: 
        if curr._val == curr._nxt._val: 
            curr._nxt = curr._nxt._nxt 
        else: 
            curr = curr._nxt
    
    return head


def _arr_2_linked_list(nums:List[int]): 
    'converts arr 2 linked_list'
    if not nums: 
        return None 
    
    head = LinkList(nums[0]) 
    curr = head 

    for num in nums[1:]: 
        curr._nxt = LinkList(num) 
        curr = curr._nxt

    return head


def _linked_list_2_arr(head): 
    res, curr = [], head 

    while curr: 
        res.append(curr._val)
        curr = curr._nxt

    return res 


def prob_05_BT_inorder_traversal():
    ''' Given the root of a binary treet (BT), return the `inorder` traversal of 
    its nodes' value
    '''
    root                = Root(1)
    root._right         = Root(2)
    root._right._left   = Root(3)
    res  = _BT_inorder_traversal(root)
    
    print('pass' if res == [1, 3, 2] else res)


def _BT_inorder_traversal(Tree:Root) -> List[int]: 
    '''  
    '''
    return _BT_inorder_traversal(Tree._left) + [Tree._val] + _BT_inorder_traversal(Tree._right) if Tree else []



def prob_06_same_BT():
    ''' Given the roots of two BTs p and q, write a fn to check if they are the same or not.
    '''
    p           = Root(1)
    p._left     = Root(2) 
    p._right    = Root(3) 
    q           = Root(1) 
    q._left     = Root(2) 
    q._right    = Root(3) 
    n           = Root(1)
    n._left     = Root(2)
    m           = Root(1) 
    m._right    = Root(2)
    x           = Root(1)
    x._left     = Root(2) 
    x._right    = Root(1) 
    y           = Root(1)
    y._left     = Root(1)
    y._right    = Root(2) 
    res_1 = _same_BT(p, q)
    res_2 = _same_BT(n, m)
    res_3 = _same_BT(x, y)
    print('pass' if res_1 else res_1)
    print('pass' if not res_2 else res_2)
    print('pass' if not res_3 else res_3)



def _same_BT(tree1:Root, tree2:Root) -> bool: 
    '''  
        IF NOT tree1._val == tree2._val 
            RETURN false 
        _same_BT(tree1._left, tree2._left)
        _same_BT(tree1._right, tree2._right)
    '''
    if tree1 is None and tree2 is None: # Both trees are empty, they are the same
        return True 
    if tree1 is None or tree2 is None: # One tree is empty, the other is not, they are diff
        return False 
    return (
        _same_BT(tree1._left, tree2._left)  and 
        tree1._val == tree2._val            and 
        _same_BT(tree1._right, tree2._right)
    )






if __name__ == '__main__':

    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n')
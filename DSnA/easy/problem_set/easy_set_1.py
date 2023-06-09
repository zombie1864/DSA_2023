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
    ''' write a fn to find the longest common prefix str in a list[str], if no common prefix 
    return empty str 
	'''
    res_1 = _longest_cp(["flower","flow","flight"]) 
    res_2 = _longest_cp(["dog","racecar","car"]) 
    print('pass' if res_1 == 'fl' else res_1)  #=> 'fl'
    print('pass' if res_2 == '' else res_2) #=> ''


def _longest_cp(words:List[str]) -> str:
    '''
    '''
    cp = '' 
    words = sorted(words) # sorts list[str] in lexicographical order 
    first_word = words[0]
    last_word = words[-1]

    for idx in range(min(len(first_word), len(last_word))): # 
        if first_word[idx] != last_word[idx]: 
            return cp 
        cp += first_word[idx]

    return cp 


def prob_01_plus_one(): 
    '''  Given a large int, represented as list[int] are ordered from most significant to least in 
    left to right order. Inc the large integer by one and return the resulting list[int]
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
    if not nums:  return [1] 

    if nums[-1] < 9: 
        nums[-1] += 1 
        return nums 
    else: 
        return _plus_one(nums[:-1]) + [0]
    

def prob_02_len_of_last_word(): 
    ''' Given a str consisting of words and spaces, return the len of the last word
    '''
    res_1 = _len_of_last_word('hello world')
    res_2 = _len_of_last_word('   fly me   to   the moon  ')
    print('pass' if res_1 == 5 else res_1) 
    print('pass' if res_2 == 4 else res_2)


def _len_of_last_word(sent:str) -> int: 
    '''  
    []_VAR arr = sent.split(' ')
    []_VAR words = [] 
    []_itr(arr, el)
        []_IF el != ' ' 
            []_words.append(el) 
    []_RETURN len(words[-1])

    O(n)_t: O(n)
    O(n)_s: O(n)
    '''
    arr, words = sent.split(' '), []
    
    for el in arr: 
        if el != '': 
            words.append(el)
 
    return len(words[-1]) 


def prob_03_top_k_frequent_elements():
    '''  Given a List[int], nums, and an int k, return the k most frequent el
    '''
    res_1 = _top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2) 
    ans_1 = [1, 2]
    print('pass' if res_1 == ans_1 else res_1)


def _top_k_frequent_elements(nums:List[int], k:int) -> List[int]: 
    '''  
    []_VAR freq = {}
    []_itr(nums, num)
        []_IF num in freq
            []_freq[num] += 1
        []_ELSE
            []_freq[num] = 1 
    []_VAR freq_arr =  [int(key) for key, val in freq.items() if val > 1]
    RETURN freq_arr[:k + 1]
    O(n)_t: O(n)
    O(n)_s: O(n)
    '''
    freq = {}
    
    for num in nums: 
        if str(num) in freq: 
            freq[str(num)] += 1 
        else: 
            freq[str(num)] = 1 
  
    freq_arr = [int(key) for key, val in freq.items() if val > 1] 

    return freq_arr[: k + 1] 

def prob_04_linked_list_rm_dups():
    ''' Suppose you have a list of random names you wish to put in alphabet order. In memory there 
    are two ways to do this - first with an array and second with linked list. Using an arr ds has 
    limitations that a linked list overcomes. The limitations of an arr is its size and inefficient 
    insertion/deletion operations. The size limitation is tied to low-level/hardware limitation. 
    Arrs have a fixed size determined at the time of creation. If the initial arr size is too small 
    it leads to overflow and requires resizing which is time-consuming and memory intensive. A linked 
    list can grow dynamically eliminating the need for pre-allocation. The insertion/deletion of entries 
    in array take O(n) to index into arr where linked-list takes O(1) by using pointers to locate data. 
    Linked-list use pointers | data | addr | -> | data | addr | that points to data in memory and do 
    not need to be adjacent like an array--existing in "cyber space". B/c of the vectorization nature 
    of a linked-list their exist different types of linked list. 

        Single linked list: Navigation is forward only 
        Double linked list: forward and backward navigation 
        circular linked list: last el is linked to the first el

    Given the head of a sorted linked list, delete all duplication and return the linked list sorted. 
    '''
    res_1 = _linked_list_rm_dups([1, 1, 2])
    res_2 = _linked_list_rm_dups([2, 2, 2, 3, 4, 9, 9])
    print('pass' if res_1 == [1, 2] else res_1)
    print('pass' if res_2 == [2, 3, 4, 9] else res_2)


def _linked_list_rm_dups(nums:List[int]) -> List[int]: 
    '''  
    []_range(0, len(nums) - 1, idx)
        []_IF nums[idx] == nums[idx + 1]
            []_nums.remove(nums[idx])
    []_RETURN nums 
    '''
    idx = 0 

    while idx < len(nums) - 1: 
        if nums[idx] == nums[idx + 1]: 
            # a == b, arr.remove(a); no update to idx 
            nums.remove(nums[idx])
        else: 
            # allowed to move forward in the arr 
            idx += 1

    return nums


def prob_05_BT_inorder_traversal():
    ''' Given the root of a binary treet (BT), return the `inorder` traversal of 
    its nodes' value
    '''
    root                = Root(1)
    root._right         = Root(2)
    root._right._left   = Root(3)
    res  = _BT_inorder_traversal(root)
    
    print('pass' if res == [1, 3, 2] else res)


def _BT_inorder_traversal(Tree:Root, seen:Union[None, int]=[]) -> List[int]: 
    '''  
    []_IF Tree.val == None 
        []_RETURN seen 
    []_IF Tree._left != None
        []_fn(Tree._left, seen)
    []_IF Tree._right != None 
        []_fn(Tree.left, seen.append(Tree.val))
    []_RETURN fn(Tree, seen.append(Tree.val))
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
    []_VAR cond_1 = tree1._val != tree2._val 
    []_VAR cond_2 = tree1._left IS NOT none AND tree2._left IS none 
    []_VAR cond_3 = tree1._left IS none AND tree2._left IS NOT none 
    []_VAR cond_4 = tree1._right IS none AND tree2._right IS NOT none 
    []_VAR cond_5 = tree1._right IS NOT none AND tree2._right IS none 
    
    []_IF cond_1 OR cond_2 OR cond_3 OR cond_4 OR cond_5 
        []_RETURN false 
    
    []_IF tree1._val != tree2._val 
        []_RETURN false 
    []_IF tree1._left AND tree2._left 
        []_RETURN fn(tree1._left, tree2._left)
    []_IF tree1._right and tree2._right 
        []_RETURN fn(tree1._right, tree2._right) 
    []_RETURN true 
    '''
    if tree1 is None and tree2 is None : # 
        return True 
    if tree1 is None or tree2 is None or tree1._val != tree2._val: 
        return False 
    return _same_BT(tree1._left, tree2._left) and _same_BT(tree1._right, tree2._right)





if __name__ == '__main__':

    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n')
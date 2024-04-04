from typing import Any, Dict, List, Optional, Set, Tuple
import sys
import pdb # PYTHON DEBUGGER 
import pprint
from typing import List 
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
    dict_of_avail_funcs = dict(enumerate(public_func_list, start=1))
    pprint.pprint(dict_of_avail_funcs) # prints a nicely formatted dict in terminal 
    exec_func = int(input('\nPick a number from the dict: '))
    print(f'\nExecuting order {exec_func}:\n')
    eval(dict_of_avail_funcs[exec_func] + '()')
    


def prob_01_mini_wait_time(): # RECORD_TIME: 21min BEST_TIME: 11min 25sec 
    ''' Given a List[+int] repr the amt of time that a query take to exec, write a fn that returns 
    the total minimum waiting time for all the queries. A query's wait time is defined as the time 
    that a query must wait before its exec start. If a query is executed second, then its wait time 
    is the duration of the first query, if a query is executed third, then its wait time is the sum of 
    the first two queries. 
	'''
    res_1 = _min_wait_time([2, 8, 1]) 
    res_2 = _min_wait_time([3, 2, 1, 2, 6]) 
    print('pass' if res_1 == 4 else res_1)  #=> 4 
    print('pass' if res_2 == 17 else res_2) #=> 17 


def _min_wait_time(queries:List[int]) -> int:
    '''  
    []_
    '''



def prob_02_is_arr2_greater(): # RECORD_TIME: 12min 
    ''' Write a fn that takes in two List[int] and returns true if all the el from the second arr 
    are greater than each el of the other arr or all the el from the first arr are greater than 
    each el in the other.
    '''
    res_1 = _is_arr2_greater([5, 8, 1], [6, 9, 2])              #=> True 
    res_2 = _is_arr2_greater([0, 8, 1], [6, 0, 1])              #=> False 
    res_3 = _is_arr2_greater([6, 9, 2, 4, 5], [5, 8, 1, 3, 4])  #=> True 
    print('pass' if res_1 else res_1) 
    print('pass' if not res_2 else res_2) 
    print('pass' if res_3 else res_3) 


def _is_arr2_greater(arr1:List[int], arr2:List[int]) -> bool:
    '''  
    []_
    '''



def prob_03_itr_binary_search(): # RECORD_TIME: 32min W SOL look up
    ''' Write a fn that takes in a sorted List[int] and a trg and returns the idx of the int 
    contained in the arr, -1 otherwise.  
    NOTE performance must be considered 
    '''
    res_1 = _itr_binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 88], 33)  #=> 3
    res_2 = _itr_binary_search([1, 2, 3, 4, 5, 6], 5)                           #=> 4
    res_3 = _itr_binary_search([0, 1, 3], 3)                                    #=> 2
    res_4 = _itr_binary_search([0, 1, 3], 9)                                    #=> -1
    print('pass' if res_1 == 3 else res_1)  
    print('pass' if res_2 == 4 else res_2)
    print('pass' if res_3 == 2 else res_3)
    print('pass' if res_4 == -1 else res_4)


def _itr_binary_search(arr:List[int], trg:int) -> int:
    '''  
    []_
    ''' 


def prob_04_recr_binary_search(): # NOTE do not delete this. Knowing how to do binary recr is impo 
    # RECORD_TIME: 16min 
    ''' Implement binary search using recr technique. Explain which technique is better itr or recr 
    NOTE performance must be considered and explain space-time C 
    '''
    print(_recr_binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33)) #=> 3 
    print(_recr_binary_search([1, 2, 3, 4, 5, 6], 5)) #=> 4
    print(_recr_binary_search([0, 1, 3], 3)) #=> 2


def _recr_binary_search(arr:List[int], trg) -> int:
    '''  
    []_
    '''



def prob_05_split_str_into_pairs(): #RECORD_TIME:
    ''' Write a function that splits strings into pairs of two characters. 
    If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_'). '''
    res_1 = _split_str_into_pairs('abc')
    res_2 = _split_str_into_pairs('abcd')
    print('pass' if res_1 == ['ab', 'c_'] else res_1) #=>  ['ab', 'c_']
    print('pass' if res_2 == ['ab', 'cd'] else res_2) #=>  ['ab', 'cd']


def _split_str_into_pairs(string:str) -> List[str]:
    '''  '''




if __name__ == '__main__':
    '''  '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
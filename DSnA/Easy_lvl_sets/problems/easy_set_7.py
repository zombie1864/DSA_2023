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



def prob_01_counting_sort(): 
    '''  
    Quicksort runs n*log(n) which is the fastest sorting can get. Sorting methods 
    rely on comparing els, counting sort does not require comparing els. Instead, u 
    create a List[int], known as an int arr, whose index range covers the entire 
    range of vals in the original arr. Each time a val occurs in the original 
    arr, u inc the counter at that idx. 
    EX: 
        arr     = [1, 1, 3, 2, 1] 
        int_arr = [0, 0, 0, 0, 0]

        idx     val     int_arr
        0       1       [0, 1, 0, 0, 0] += 1 @int_arr_idx int_arr[val]
        1       1       [0, 2, 0, 0, 0]
        2       3       [0, 2, 0, 1, 0]
        3       2       [0, 2, 1, 1, 0]
        4       1       [0, 3, 1, 1, 0]
    Given a List[int], count and return da num of times each val appears as a List[int]
    '''
    arr_1 = [2, 2, 3, 0, 1, 5]
    ans_1 = [1, 1, 2, 1, 0, 1]

    arr_2 = [1, 1, 1, 2, 8, 1, 2, 1, 0]
    ans_2 = [1, 5, 2, 0, 0, 0, 0, 0, 1]

    print('pass' if _count_sort(arr_1) == ans_1 else _count_sort(arr_1)) 
    print('pass' if _count_sort(arr_2) == ans_2 else _count_sort(arr_2)) 

def _count_sort(arr:List[int]) -> List[int]: 
    '''  '''
    arr_int = [0] * len(arr)
    for n in arr: 
        arr_int[n] += 1
    return arr_int



if __name__ == '__main__':
    '''  '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
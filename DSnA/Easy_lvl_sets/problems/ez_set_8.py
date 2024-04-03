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



def prob_02_calculate_slope(): #RECORD_TIME 9min 55sec
    """Given two Dict repr points containing keys x and y, calculate the slope btw two points. 
    If points are equal return float type infinity using float('inf'). Raise ValueError if 
    x or y are not present in the either point.

    TAGS:
        [compSciFund, math]
    """ 
    res_1 = _calculate_slope({'x': 0, 'y': 1}, {'x': 1, 'y': 1})
    res_2 = _calculate_slope({'x': 1, 'y': 1}, {'x': 2, 'y': 2})
    res_3 = _calculate_slope({'x': 1, 'y': 3}, {'x': 2, 'y': 6})
    res_4 = _calculate_slope({'x': 0, 'y': 1}, {'x': 0, 'y': 2})
    res_5 = _calculate_slope({'x': 0,}, {'x': 1, 'y': 1})
    res_6 = _calculate_slope({'x': 0, 'x': 9, 'y': 10}, {'x': 1, 'y': 1}) # NOTE explain what is happening here 
    res_7 = _calculate_slope({'z': 9, 'y': 10}, {'x': 1, 'y': 1})
    print('pass' if res_1 == 0.0 else res_1)                            #=> 0.0
    print('pass' if res_2 == 1.0 else res_2)                            #=> 1.0
    print('pass' if res_3 == 3.0 else res_3)                            #=> 3.0
    print('pass' if res_6 == 1.125 else res_6)                          #=> 1.125
    print('pass' if res_4 == float('inf') else res_4)                   #=> float('inf')
    print('pass' if res_5 == "ValueError('preReq missing')" else res_5) #=> ValueError
    print('pass' if res_7 == "ValueError('preReq missing')" else res_7) #=> ValueError


def _calculate_slope(point_a: Dict[str,float], point_b: Dict[str, float]) -> float: 
    '''   
    '''



if __name__ == '__main__':
    '''  '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
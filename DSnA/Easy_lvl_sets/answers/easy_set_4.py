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
    dict_of_avail_funcs = dict(enumerate(public_func_list))
    pprint.pprint(dict_of_avail_funcs) # prints a nicely formatted dict in terminal 
    exec_func = int(input('\nPick a number from the dict: '))
    print(f'\nExecuting order {exec_func}:\n')
    eval(dict_of_avail_funcs[exec_func] + '()')


def prob_00_filter_out_even_numbers(): #RECORD_TIME: 2min 
    ''' w/o using if statement filter out even vals from a List[int] and return the new List[int]

    TAGS:
        [language]
    '''
    res_1 = _filter_out_even_numbers([2, 6, 1, 4, 5])
    res_2 = _filter_out_even_numbers([])
    res_3 = _filter_out_even_numbers([2, 4])
    print('pass' if res_1 == [1,5] else res_1)  #=> [1,5]
    print('pass' if res_2 == [] else res_2)     #=> []
    print('pass' if res_3 == [] else res_3)     #=> []


def _filter_out_even_numbers(nums: List[int]) ->List[int]: 
    '''  
    RETURN [n for n in nums if n % 2]
    '''
    return [n for n in nums if n % 2]


def prob_01_total_of_2d_arr(): #RECORD_TIME: 1min 30sec BEST_TIME: 1min 30sec 
    ''' Return the sum of a List[List[int]] using listCom

    TAGS:
        [language, compSciFund]
    '''
    res_1 = _total_of_2d_arr([[1,2,3],[1,2,3,4]])
    res_2 = _total_of_2d_arr([[1,2], [1,2,3], [1,2,3]])
    print('pass' if res_1 == 16 else res_1) #=> 16 
    print('pass' if res_2 == 15 else res_2) #=> 15


def _total_of_2d_arr(arr: List[List[int]]) -> int: 
    '''  
    RETURN sum([n for nums in arr for n in nums])
    '''
    return sum([n for nums in arr for n in nums])


def prob_02_list_of_records(): #RECORD_TIME: 16min 17sec BEST_TIME: 11min 35sec 
    """Given matrix and a tuple of col_names, return a List[Dict[str,int]], 
    where each val is associated with a given colname. 
    NOTE performance needs to be considered 
    Raises:
        ValueError: If rows are of unequal length
        ValueError: If column names are not equal to the length of each row

    TAGS:
        [compSciFund, bool_logic]
    """
    ans = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 4, 'b': 5, 'c': 6},
        {'a': 7, 'b': 8, 'c': 9},
    ]
    res_1 = _list_of_records([[1,2,3], [4,5,6], [7,8,9]] , ('a', 'b', 'c'))
    res_2 = _list_of_records([[1,2,3], [4,5]] , ('a', 'b', 'c'))
    res_3 = _list_of_records([[1,2,3], [4,5,6], [7,8,9]] , ('a', 'b'))
    print('pass' if res_1 == ans else res_1) #=> ans 
    print('pass' if res_2 == "ValueError('preReq not meet')" else res_2) #=> ValueError
    print('pass' if res_3 == "ValueError('preReq not meet')" else res_3) #=> ValueError


def _list_of_records(rows: List[List[int]], col_names: Tuple[str]) -> List[Dict[str, int]]: 
    '''  
    try 
        if all(row != len(rows[0]) for row in rows) or len(col_names) != len(rows[0]) 
            raise ValueError(msg)
        
        res = [] 
        itr(rows, row) 
            res_dict = {}
            range(len(row), i)
                val, label = row[i], col_names[i]
                res_dict[label] = val 
            res.append(res_dict)
        
        RETURN res 
    except ValueError as err 
        return reper(err)
    '''
    try:
        if any(len(row) != len(col_names) for row in rows): 
            raise ValueError('preReq not meet')
        return [dict(zip(col_names, row)) for row in rows]
    except ValueError as err: 
        return repr(err)


def prob_03_front_back_exchanged(): #RECORD_TIME: 4min 30sec BEST_TIME: 2min 21sec 
    '''Given a str, return a new str where the first and last chars have been exchanged'''
    res_1 = _front_back_exchanged('code')
    res_2 = _front_back_exchanged('a')
    res_3 = _front_back_exchanged('ab')
    res_4 = _front_back_exchanged('')
    print('pass' if res_1 == 'eodc' else res_1) #=> 'eodc'
    print('pass' if res_2 == 'a' else res_2)    #=> 'a'
    print('pass' if res_3 == 'ba' else res_3)   #=> 'ba'
    print('pass' if res_4 == '' else res_4)     #=> ''


def _front_back_exchanged(string:str) -> str: 
    '''  
    '''


def prob_04_count_last_2(): #RECORD_TIME: 19min 55sec BEST_TIME: 6min 8sec 
    '''Given a str, return the number of times that the last 2 chars appear in the str. Do not count the last substring, 
    use it only as an identifier.
    '''
    res_1 = _count_last_2('hixxhi')
    res_2 = _count_last_2('xaxxaxaxx')
    res_3 = _count_last_2('axxxaaxx')
    res_4 = _count_last_2(' s    s g   h hh h    ')
    print('pass' if res_1 == 1 else res_1) #=> 1
    print('pass' if res_2 == 1 else res_2) #=> 1
    print('pass' if res_3 == 2 else res_3) #=> 2
    print('pass' if res_4 == 7 else res_4) #=> 7


def _count_last_2(string: str) -> int: 
    '''  
    '''


if __name__ == '__main__':
    '''  
    https://www.dollartimes.com/calculators/hours-minutes-calculator
    TOT_RUN_TIME: 1hr, 32min, 14sec 
    DSGN-DOC:
        []_In the future you will be competing against your run time for each problem 
            []_RECORD_TIME vs BEST_TIME vs OPT_TIME 
                []_RECORD_TIME: is the duration of an initial attempt to a problem 
                []_BEST_TIME: is the recorded duration that beats RECORD_TIME 
                []_OPT_TIME: is the statical time AVG of at least 2 or 3 recorded BEST_TIME 
                    ⮑ ex: BEST_TIME: 2min BEST_TIME: 1min 50sec BEST_TIME: 2min 25sec 
                        []_OPT_TIME: 2min 5sec [calculated using time average tool online]
                            ⮑ future attempts will not be recorded instead the OPT_TIME is that best time you are 
                            trying to compete against 

        []_You will also be adding tags to each problem to well DOC each problem by some category 
    '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
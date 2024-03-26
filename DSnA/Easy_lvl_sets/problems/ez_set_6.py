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


def prob_01_mapping_letters(): # actual meta qstn 
    '''
    Given a mapping from digits 2 List[str] of two length determine all possible ways 2 
    replace da digits w chars
    mapping = {
        '1' -> ['A', 'B', 'C'], 
        '2' -> ['D', 'E', 'F'], 
    }
    '''
    rule_1 = {
        '1': ['A', 'B', 'C'], 
        '2': ['D', 'E', 'F']
    }
    rule_2 = {
        '3': ['G', 'H'], 
        '4': ['D', 'E', 'F']
    }
    rule_3 = {
        '5': ['L', 'M', 'N'], 
        '6': ['O']
    }
    res_1 = ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
    res_2 = ['GD', 'GE', 'GF', 'HD', 'HE', 'HF']
    res_3 = ['LO', 'MO', 'NO']
    print('pass' if _mapping_letters('12', rule_1) == res_1 else _mapping_letters('12', rule_1))
    print('pass' if _mapping_letters('34', rule_2) == res_2 else _mapping_letters('34', rule_2))
    print('pass' if _mapping_letters('56', rule_3) == res_3 else _mapping_letters('56', rule_3))



def _mapping_letters(num:str, rule:Dict[str, List[str]]) -> List[str]: 
    '''
    '''



def prob_02_phone_letter_combinations():
    '''
    given a str containing digits from 2-9, return all possible letter combinations that the 
    num could represent. Solve this using da algo technique called `Backtracking`--used 
    2 solve prob recursively that considers searching every possible combination in order 
    2 solve a computational problem. The previous prob can also be solved with this technique 
    but if u didn't that fine but it is important 2 do so here
    '''
    rule = {
        '2': 'abc', 
        '3': 'def', 
        '4': 'ghi', 
        '5': 'jkl', 
        '6': 'mno', 
        '7': 'pqrs', 
        '8': 'tuv', 
        '9': 'wxyz'
    }
    res = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    print('pass' if _letter_combinations('23', rule) == res else _letter_combinations('23', rule))


def _letter_combinations(num:str, rule:Dict[str, str]):
    '''
    '''



def prob_03_lonely_int():
    '''
    Given a List[int], where all el but 1 occur twice, find the unique el
    '''
    arr_1 = [1, 2, 3, 4, 3, 2, 1]
    arr_2 = [0, 9, 3, 3, 1, 0, 9]
    arr_3 = [0, 0, 1, 1, 3, 2, 3] 
    print('pass' if _lonely_int(arr_1) == 4 else _lonely_int(arr_1))
    print('pass' if _lonely_int(arr_2) == 1 else _lonely_int(arr_2))
    print('pass' if _lonely_int(arr_3) == 2 else _lonely_int(arr_3))


def _lonely_int(arr:List[int]) -> int: 
    '''
    '''



def prob_04_diagonal_diff():
    '''
    Given a square matrix, find da abs diff btw da sums of its diagonals 
    '''


def prob_05_is_continous_seq():
    '''  
    Given a seq of ints and an int trg, return a bool whether a continous sequence of int 
    sums up to the trg
    '''
    arr_1 = [1, 3, 1, 4, 23]
    print('pass' if _is_continous_seq(arr_1, 8) else _is_continous_seq(arr_1, 8))
    print('pass' if not _is_continous_seq(arr_1, 7) else _is_continous_seq(arr_1, 7))

def _is_continous_seq(arr, trg): 
    '''  
    '''



if __name__ == '__main__':
    '''  
    '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
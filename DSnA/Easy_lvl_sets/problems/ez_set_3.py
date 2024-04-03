from typing import Any, Dict, List, Optional, Set, Tuple
import sys
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


def prob_01_is_truthiness(): #RECORD_TIME: 12min BEST_TIME: 3min 56sec 
    ''' Given 2 ints return true if one is neg and the other pos or 0. 
    Return true if both are negative and 3rd param is true. 
    NOTE it is best practice to write your fn begining with `is` to identify the output of
    fn is bool. For example def is_data_corrupted(): 

    TAGS:
        [bool_logic]
    '''
    res_1 = _is_truthiness(1, 1)
    res_2 = _is_truthiness(1, 0)
    res_3 = _is_truthiness(1, -1)
    res_4 = _is_truthiness(-1, -1)
    res_5 = _is_truthiness(0, 0)
    res_6 = _is_truthiness(1, 1, True)
    res_7 = _is_truthiness(-1, -1, True)
    print('pass' if not res_1   else res_1)        #=> False 
    print('pass' if not res_2   else res_2)        #=> False 
    print('pass' if res_3       else res_3)        #=> True 
    print('pass' if not res_4   else res_4)        #=> False 
    print('pass' if not res_5   else res_5)        #=> False 
    print('pass' if not res_6   else res_6)        #=> False 
    print('pass' if res_7       else res_7)        #=> True 


def _is_truthiness(a:int, b:int, neg:bool=False) -> bool: 
    '''  
    '''



def prob_02_is_in_range_of_target(): #RECORD_TIME: 3min
    ''' Given an int n, return true if it is within threshold of the trg or twice the trg value 

    TAGS:
        [bool_logic]
    '''
    res_1 = _is_in_range_of_target(90)
    res_2 = _is_in_range_of_target(200)
    res_3 = _is_in_range_of_target(150)
    res_4 = _is_in_range_of_target(150, 165, 20)
    print('pass' if res_1 else res_1)       #=> True
    print('pass' if res_2 else res_2)       #=> True
    print('pass' if not res_3 else res_3)   #=> False
    print('pass' if res_4 else res_4)       #=> True



def _is_in_range_of_target(num:int, trg:int=100, threshold:int=10) -> bool: 
    '''  
    '''


def prob_03_remove_str_at_index(): #RECORD_TIME: 5min 40sec BEST_TIME: 3min 42sec 
    ''' Given a str, return a new str with the given index removed. 
    Raises ValueError with message "string cannot be zero length" if empty string. 
    
    TAGS:
        [compSciFund]
    '''
    res_1 = _remove_str_at_index('hello', 1)
    res_2 = _remove_str_at_index('hello', 0)
    res_3 = _remove_str_at_index('', 1)
    print('pass' if res_1 == 'hllo' else res_1)                                         #=> hllo
    print('pass' if res_2 == 'ello' else res_2)                                         #=> ello
    print('pass' if res_3 == "ValueError('string cannot be zero length')" else res_3)   #=> ValueError

def _remove_str_at_index(txt:str, idx:int) -> str: 
    '''  
    '''



def prob_04_heptiptup(): #RECORD_TIME: 4min 13sec
    '''
    Given an int return a str given the rules:
        * If n is a factor of 3 the string should contain `Hep` 
        * If n is a factor of 5 the string should contain `Tip` 
        * If n is a factor of 7 the string should contain `Tup`
        * If all of these conditions fail return the original value as a string     
    The order of the statements Hep Tip and Tup should be preserved in the res str
    NOTE implement this without too many IF clause. This practice ensures reducing too many 
    redunant IF clause. Too many IF-ELSE statements will run O(n)_t: O(n). Imagine having 100 IF 
    clause the compiler will check against all until it hits a match. Write a func that takes the 
    same O(n) but inc readability of code. 

    TAGS:
        [compSciFund]
    '''
    res_1 = _heptiptup(3)
    res_2 = _heptiptup(6)
    res_3 = _heptiptup(5)
    res_4 = _heptiptup(49)
    res_5 = _heptiptup(15)
    res_6 = _heptiptup(105)
    res_7 = _heptiptup(4)
    print('pass' if res_1 == 'Hep' else res_1)          #=> 'Hep'
    print('pass' if res_2 == 'Hep' else res_2)          #=> 'Hep'
    print('pass' if res_3 == 'Tip' else res_3)          #=> 'Tip'
    print('pass' if res_4 == 'Tup' else res_4)          #=> 'Tup'
    print('pass' if res_5 == 'HepTip' else res_5)       #=> 'HepTip'
    print('pass' if res_6 == 'HepTipTup' else res_6)    #=> 'HepTipTup'
    print('pass' if res_7 == '4' else res_7)            #=> '4'



def _heptiptup(n:int) -> str: 
    '''  
    '''



def prob_05_custom_heptiptup(): #RECORD_TIME: 9min
    """ Given an int and a mapping dict that checks if the int is divisible by 3 natural nums: 
    x, y, and z, with x < y < z and returns a str given the following rules:
        • If n is a factor of x the string should contain `A` 
        • If n is a factor of y the string should contain `B` 
        • If n is a factor of z the string should contain `C`
        • If all of these conditions fail return the original value as a string 
        • Rules should only contain 3 values and those values must be positive integers.
    NOTE that what the str vals do not matter, it should work with anything.
    Raises: 
        ValueError If: 
            3 rules are not given.
            any rule val are not ints 
            any rule val is not positive

    TAGS:
        [bool_logic, compSciFund]
    """
    res_1 = _custom_heptiptup(5, {'A': 5, 'B': 10, 'C': 11})
    res_2 = _custom_heptiptup(550, {'A': 5, 'B': 10, 'C': 11})
    res_3 = _custom_heptiptup(1, {'A': 5, 'B': 10, 'C': 11})
    res_4 = _custom_heptiptup(1, {'A': 5, 'B': 10, 'C': -11})
    print('pass' if res_1 == 'A' else res_1)     #=> 'A'
    print('pass' if res_2 == 'ABC' else res_2)   #=> 'ABC'
    print('pass' if res_3 == '1' else res_3)     #=> '1'
    print('pass' if res_4 == "ValueError('preReq not meet')" else res_4)    #=> ValueError



def _custom_heptiptup(num: int, rule: Dict[str, int]) -> str:
    '''  
    ''' 


if __name__ == '__main__':
    '''  
    '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
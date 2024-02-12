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


def prob_00_mapping_letters(): # actual meta qstn 
    '''
    Given a mapping from digits 2 List[str] of arbitrary length determine all possible ways 2 
    replace da digits w chars
    mapping = {
        '1' -> ['A', 'B', 'C'], 
        '2' -> ['D', 'E', 'F'], 
        ...
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
        '3': ['J', 'K'], 
        '4': ['L', 'M', 'N'], 
        '5': ['O']
    }
    res_1 = ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
    res_2 = ['GD', 'GE', 'GF', 'HD', 'HE', 'HF']
    res_3 = ['JLO', 'JMO', 'JNO', 'KLO', 'KMO', 'KNO']
    print('pass' if _mapping_letters('12', rule_1) == res_1 else _mapping_letters('12', rule_1))
    print('pass' if _mapping_letters('34', rule_2) == res_2 else _mapping_letters('34', rule_2))
    print('pass' if _mapping_letters('345', rule_3) == res_3 else _mapping_letters('345', rule_3))


def _mapping_letters(num:str, rule:Dict[str, List[str]]) -> List[str]: 
    '''
    '''
    def generate_combinations(combination, digits):
        if not digits:
            res.append(combination)
            return
        
        for char in rule[digits[0]]:
            generate_combinations(combination + char, digits[1:])

    res = []
    generate_combinations('', num)
    return res



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
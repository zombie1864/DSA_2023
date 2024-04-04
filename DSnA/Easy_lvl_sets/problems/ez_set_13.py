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
    


def prob_01_how_many_cakes(): #RECORD_TIME: 33min 7sec WARNINGlvl-HARD
    ''' Write a fn that takes a recipe:Dict[str,int] and the avail ingredients:Dict[str,int] and returns the maximum number 
    of cakes that can baked (integer). 
    For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200)

    TAGS:
        [language, compSciFund]
    '''
    res_1 = _how_many_cakes(
            {'flour': 500, 'sugar': 200, 'eggs': 1}, 
            {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
        )
    res_2 = _how_many_cakes(
            {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, 
            {'sugar': 500, 'flour': 2000, 'milk': 2000}
        )
    res_3 = _how_many_cakes(
            {'apples': 68, 'oil': 78, 'sugar': 85}, 
            {'sugar': 5644, 'flour': 721, 'apples': 1026, 'cream': 7952, 'oil': 7327, 'nuts': 7461, 'butter': 7448, 'eggs': 5299, 'crumbles': 8692, 'milk': 4829}
        )
    print('pass' if res_1 == 2 else res_1)  #=> 2
    print('pass' if res_2 == 0 else res_2)  #=> 0
    print('pass' if res_3 == 15 else res_3) #=> 15


def _how_many_cakes(recipe:Dict[str, int], ingredients:Dict[str, int]) -> int:
    '''  
    []_
    O(n)_t: 
    O(n)_s: 
    '''


def prob_02_like_system(): #RECORD_TIME: 19min 38sec
    ''' Impl a fn which takes names:List[str] of ppl and returns a str as shown in the examples.
    NOTE Impl without using conditionals. 

    TAGS:
        [language, compSciFund]
    '''
    res_1 = _like_system([])
    res_2 = _like_system(["Peter"])
    res_3 = _like_system(["Jacob", "Alex"])
    res_4 = _like_system(["Max", "John", "Mark"])
    res_5 = _like_system(["Alex", "Jacob", "Mark", "Max"])
    print('pass' if res_1 == 'No one likes this' else res_1)                    
    print('pass' if res_2 == 'Peter likes this' else res_2)                     
    print('pass' if res_3 == 'Jacob and Alex like this' else res_3)             
    print('pass' if res_4 == 'Max, John, and Mark like this' else res_4)         
    print('pass' if res_5 == 'Alex, Jacob, and 2 others like this' else res_5) 


def _like_system(names:List[str]) -> str:
    '''  
    []_
    O(n)_t: 
    O(n)_s: 
    '''

        
def prob_03_is_valid_braces(): #RECORD_TIME: 11min 9sec NOTE failed to meet constraint
    ''' Write a fn that takes a str and returns a bool if the order of the braces is valid. 
    validated str have matching brace, e.g. (), {}, [] is valid while (}, (], {) is not valid, 
    i.e, the string must contain matching pair(s) to be considered valid.
    NOTE Impl this without conditionals  

    TAGS:
        [compSciFund]
    '''
    res_1 = _is_valid_braces("()")      #=>  True
    res_2 = _is_valid_braces("(){}[]")  #=>  True
    res_3 = _is_valid_braces("([{}])")  #=>  True
    res_4 = _is_valid_braces("(}")      #=>  False
    res_5 = _is_valid_braces("[(])")    #=>  False
    res_6 = _is_valid_braces("[({})](]")#=>  False
    res_7 = _is_valid_braces("([{)}]")  #=>  False
    print('pass' if res_1 else res_1)
    print('pass' if res_2 else res_2)
    print('pass' if res_3 else res_3)
    print('pass' if not res_4 else res_4)
    print('pass' if not res_5 else res_5)
    print('pass' if not res_6 else res_6)
    print('pass' if not res_7 else res_7)


def _is_valid_braces(s:str) -> bool: 
    '''  
    []_
    O(n)_t: 
    O(n)_s: 
    ''' 



def prob_04_is_same_array(): #RECORD_TIME: 4min 26sec 
    ''' Given two list[int] write a fn that checks whether the two arr have the "same" el.
    "Same", means that els in `B` are the els in `A` squared, regardless of order.
    E.g. 
    a = [121, 144, 19, 161, 19, 144, 19, 11]  
    b = [121, 14641, 20736, 361, 25921, 361, 20736, 361] where 
    b ~ a such that 
    b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19] 

    NOTE: Edge cases and performance needs to be considered

    TAGS:
        [language]
    '''
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    a3 = [231, 14641, 20736, 361, 25921, 361, 20736, 361]
    a4 = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
    res_1 = _is_same_array(a1, a2)
    res_2 = _is_same_array(a1, a3)
    res_3 = _is_same_array(a1, a4)
    print('pass' if res_1 else res_1)       #=> True 
    print('pass' if not res_2 else res_2)   #=> False 
    print('pass' if not res_3 else res_3)   #=> False


def _is_same_array(A:List, B:List) -> bool: 
    '''  
    []_
    O(n)_t: 
    O(n)_s: 
    '''
 

def prob_05_is_word_formable(): #RECORD_TIME: 19min 22sec 
    ''' Write a fn that returns True if a portion of str_1 characters can be rearranged to match
    str_2, otherwise returns False. NOTE: Only lower case letters will be used (a-z). No punctuation or 
    digits will be included. Performance needs to be considered.
    '''
    res_1 = _is_word_formable('rkqodlw', 'world')
    res_2 = _is_word_formable('cedewaraaossoqqyt', 'codewars')
    res_3 = _is_word_formable('katas', 'steak') 
    res_4 = _is_word_formable('scriptingjava', 'javascript')
    res_5 = _is_word_formable('bbaaabbnn', 'banana')
    print('pass' if res_1 else res_1)       #=> True
    print('pass' if res_2 else res_2)       #=> True
    print('pass' if not res_3 else res_3)   #=> False 
    print('pass' if res_4 else res_4)       #=> True
    print('pass' if res_5 else res_5)       #=> True


def _is_word_formable(str_1:str, str_2:str) -> bool: 
    '''  
    []_
    O(n)_t: 
    O(n)_s: 
    '''



if __name__ == '__main__':
    '''  '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
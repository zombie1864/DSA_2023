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

def prob_00_is_happy_num() :
    '''
    A happy num is defined as an integer in which the following sequence ends with the num 1.
    Sum of the square of each individual digit equal to 1, then the number is happy.
    A num is unhappy once the same number occurs multiple times in a sequence.

    Ex: 7 is a "happy" number:
    7² = 49 --> 4² + 9² = 97 --> 9² + 7² = 130 --> 1² + 3² + 0² = 10 --> 1² + 0² = 1

    Ex: 6 is not a happy number as the sequence that is generated is the following:
    6, 36, 45, 41, 17, 50, 25, 29, 85, [89], 145, 42, 20, 4, 16, 37, 58, [89]

    When da same num occurs twice, the sequence is guaranteed to go on infinitely.
    Write a fn that returns a list of all happy nums from 1 to n inclusive.
    '''
    ans = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
    ans2 = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617, 622, 623, 632, 635, 637, 638, 644, 649, 653, 655, 656, 665, 671, 673, 680, 683, 694, 700, 709, 716, 736, 739, 748, 761, 763, 784, 790, 793, 802, 806, 818, 820, 833, 836, 847, 860, 863, 874, 881, 888, 899, 901, 904, 907, 910, 912, 913, 921, 923, 931, 932, 937, 940, 946, 964, 970, 973, 989, 998]
    print('pass' if _happy_num(100) == ans else _happy_num(100))


def _happy_num(n):
    '''
    '''
    return [num for num in range(1, n + 1) if _happy(num)]

def _happy(num): 
    seen = set() 
    while num != 1 and num not in seen: 
        seen.add(num) 
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

def prob_01_plus_minus(): 
    '''
    Given a list[int], find the ratios of its elements that are pos, neg, and zero. Print the decimal val of each fraction on a new line with 6 decimal places.

    Example
    arr = [1, 1, 0, -1, -1]
    There are 5 els, two pos, two neg and one zero. Their ratios are 2/5, 2/5, 1/5
    and are printed as:
        0.400000
        0.400000
        0.200000
    the fn should not return a val.
    '''
    arr = [-4, 3, -9, 0, 4, 1]
    _plus_minus(arr) #=> 0.5, 0.333333, 0.166667


def _plus_minus(arr:List[int]) -> None:  
    '''
    '''
    tot = len(arr)
    pos = sum(1 for num in arr if num > 0)
    neg = sum(1 for num in arr if num < 0)
    zero = tot - pos - neg

    print(round(pos / tot, 6))
    print(round(neg / tot, 6))
    print(round(zero / tot, 6))


def prob_02_min_max_sum(): 
    '''
    Given five pos ints, find the min and max vals that can be calculated by summing exactly four
    of the five ints. Return da respective min and max vals as a single line of two 
    space-separated ints.
    Ex: 
        1 + 3 + 5 + 7 = 16 
        3 + 5 + 7 + 9 = 24 
    '''
    arr = [9, 7, 5, 3, 1]
    print('pass' if _min_max_sum(arr) == '16 24' else _min_max_sum) 


def _min_max_sum(arr:List[int]) -> str: 
    '''
    '''
    arr.sort()
    min_val = sum(arr[:4])
    max_val = sum(arr[1:len(arr)])
    return f'{min_val} {max_val}'


def prob_03_time_converstion(): 
    '''
    Given a time in 12-hour AM/PM format, return a str w the time converted to military (24-hour) time.
    Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
    - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
    HINT: u can use {time:02} to help format the time 2 two digits. 
    '''
    time_ex_1 = '07:05:45PM'
    time_ex_2 = '12:40:22AM'
    time_ex_3 = '12:45:00PM'
    print('pass' if _time_converstion(time_ex_1) == '19:05:45' else _time_converstion())
    print('pass' if _time_converstion(time_ex_2) == '00:40:22' else _time_converstion())
    print('pass' if _time_converstion(time_ex_3) == '12:45:00' else _time_converstion())



def _time_converstion(time:str) -> str: 
    '''
    '''
    hour, day_phase = int(time[:2]), time[-2:]

    if day_phase == 'PM' and hour != 12:
        hour = (hour + 12) % 24
    elif day_phase == 'AM' and hour == 12:
        hour = 0

    return f'{hour:02}{time[2:-2]}'


def prob_04_nonzero_2_da_left(): # actual meta qstn 
    '''
    U r given a list[int]. Write an algo that brings all nonzero els to the left of the arr, 
    and returns the num of nonzero els. The algo should operate in place and should not create 
    a new arr. The order of the nonzero els does not matter. The nums that remain in the right
    portion of the array can be anything. Ex: [1, 0, 2, 0, 0, 3, 4], a possible ans
    is [4, 1, 3, 2, ?, ?, ?, ?], 4 non-zero elements, where “?” Can be any number.  
    '''
    arr_1 = [1, 0, 2, 0, 0, 3, 4]
    arr_2 = [-1, 2, 1, 0, -3, 0, 4]
    arr_3 = [0, 0, 0, 0, 0, 0, 0]
    print('pass' if _nonzero(arr_1) == 4 else _nonzero(arr_1))
    print('pass' if _nonzero(arr_2) == 5 else _nonzero(arr_2))
    print('pass' if _nonzero(arr_3) == 0 else _nonzero(arr_3))



def _nonzero(arr:List[int]) -> int: 
    '''  
    first_0_i = arr.index(0) 
    while any(el !=0 for el in arr[first_0_i:]): 
        for i in range(1, len(arr)): 
            if arr[i] != 0: 
                arr[i - 1], arr[i] = arr[i], arr[i - 1] 
        first_0_i = arr.index(0)
    return len(arr[:first_0_i])
    '''
    non_zeros = 0
    i = 0
    j = len(arr) - 1

    while i <= j:
        if arr[i] != 0:
            i += 1
            non_zeros += 1
        elif arr[j] == 0:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            non_zeros += 1

    return non_zeros



if __name__ == '__main__':
    '''  
    '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
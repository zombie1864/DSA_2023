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



def prob_02_():
    '''  
    Ur given a game board represented as a 2D arr of zeros and ones. Zero stands for passable positions and one stands for impassable positions. Design an algorithm to find a path from top left corner to bottom right corner
    EX:
            0 0 0 0 0 0 0 
            0 0 1 0 0 1 0 
            0 0 1 0 1 0 0 
            0 0 1 0 1 1 1
            0 0 0 0 0 0 0 

    Start-> + + + + 0 0 0 
            0 0 1 + 0 1 0 
            0 0 1 + 1 0 0 
            0 0 1 + 1 1 1
            0 0 0 + + + + -> end 
    '''
    M = [
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0, 1, 0], 
        [0, 0, 1, 0, 1, 0, 0], 
        [0, 0, 1, 0, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0]
    ]
    print('pass' if _path_finder(M) else _path_finder(M)) 

def _path_finder(board):
    rows, cols = len(board), len(board[0])

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]# Defines: up, down, left, right

    # Queue for BFS
    queue = [(0, 0)]
    queue_index = 0

    while queue_index < len(queue):
        row, col = queue[queue_index]
        queue_index += 1

        # Check if reached the bottom right corner
        if row == rows - 1 and col == cols - 1:
            return True

        # Mark the current position as visited
        board[row][col] = 1

        # Explore neighbors
        for dr, dc in dirs:
            nr, nc = row + dr, col + dc

            # Check if the neighbor is within bounds and is passable
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 0:
                queue.append((nr, nc))

    # If the queue is empty and no path is found
    return False

if __name__ == '__main__':
    ''' '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
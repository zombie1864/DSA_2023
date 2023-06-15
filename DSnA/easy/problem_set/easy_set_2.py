from audioop import reverse
from typing import Any, Dict, List, Optional, Set, Tuple, Union
import sys
import pprint
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


class BT:
    ''' Class to build BTs '''
    def __init__(self, val=0, left=None, right=None): 
        self.val   = val 
        self.left  = left 
        self.right = right 



def prob_01_sym_tree():
    '''  Given the root of a BT, check whether it is symmetric 
    sym_tree: 
            1
           / \
          2   2
         / \ / \
        3  4 4  3 
    '''
    sym_tree                = BT(1)
    sym_tree.left           = BT(2)
    sym_tree.left.left      = BT(3)
    sym_tree.left.right     = BT(4)
    sym_tree.right          = BT(2)
    sym_tree.right.left     = BT(4)
    sym_tree.right.right    = BT(3)
    tree                    = BT(1)
    tree.left               = BT(2)
    tree.left.right         = BT(3)
    tree.right              = BT(2)
    tree.right.right        = BT(3)

    res_1 = _sym_tree(sym_tree) 
    res_2 = _sym_tree(sym_tree) 

    print('pass' if res_1 else res_1)
    print('pass' if not res_2 else res_2)



def _sym_tree(tree:BT) -> bool: 
    '''  
    []_VAR lhs_nodes = [tree.val] + fn(tree.left) + fn(tree.right)
    '''




if __name__ == '__main__':

    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n')
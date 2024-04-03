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

class BT(): 
    def __init__(self, val) -> None:
        self.val    = val 
        self.left   = None 
        self.right  = None 



def prob_01_validate_BST(): 
    bt_1                = BT(2)
    bt_1.left           = BT(1) 
    bt_1.right          = BT(3)
    bt_2                = BT(2) 
    bt_2.right          = BT(3) 
    bt_2.right.right    = BT(4)
    bt_3                = BT(2)
    bt_3.left           = BT(3) 
    bt_3.right          = BT(1)
    bt_4                = BT(5)
    bt_4.left           = BT(4) 
    bt_4.left.left      = BT(3)
    bt_4.left.right     = BT(6)
    print('pass' if _validate_BST(bt_1) else _validate_BST(bt_1)) 
    print('pass' if _validate_BST(bt_2) else _validate_BST(bt_1)) 
    print('pass' if not _validate_BST(bt_3) else _validate_BST(bt_3)) 
    print('pass' if not _validate_BST(bt_4) else _validate_BST(bt_4)) 

def _validate_BST(BT): 
    def _inorder_path(BT): 
        return _inorder_path(BT.left) + [BT.val] + _inorder_path(BT.right) if BT else []
    vals = _inorder_path(BT)       
    for i in range(len(vals) - 1): 
        n = vals[i]
        m = vals[i + 1]

        if n > m: 
            return False 
        
    return True

def prob_02(): 
    pass




def prob_03(): 
    pass 



if __name__ == '__main__':
    '''  '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
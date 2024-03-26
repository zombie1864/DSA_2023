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
    dict_of_avail_funcs = dict(enumerate(public_func_list, start=1))
    pprint.pprint(dict_of_avail_funcs) # prints a nicely formatted dict in terminal 
    exec_func = int(input('\nPick a number from the dict: '))
    print(f'\nExecuting order {exec_func}:\n')
    eval(dict_of_avail_funcs[exec_func] + '()')



class Root:
    def __init__(self, val=0, left=None, right=None): 
        self.val   = val 
        self.left  = left 
        self.right = right 
        self.children = [] 


    def add_child(self, val): 
        self.children.append(Root(val))
        return self 


    def depth_first_search(self, arr): 
        '''  
        '''
        pass


def prob_01_BT_inorder_traversal():
    ''' Given the root of a binary treet (BT), return the `inorder` traversal of 
    its nodes' value
    '''
    root              = Root(1)
    root.right        = Root(2)
    root.right.left   = Root(3)
    res  = _BT_inorder_traversal(root)
    
    print('pass' if res == [1, 3, 2] else res)


def _BT_inorder_traversal(Tree:Root) -> List[int]: 
    '''  
    '''




def prob_02_same_BT():
    ''' Given the roots of two BTs p and q, write a fn to check if they are the same or not.
    '''
    p           = Root(1)
    p.left      = Root(2) 
    p.right     = Root(3) 
    q           = Root(1) 
    q.left      = Root(2) 
    q.right     = Root(3) 
    n           = Root(1)
    n.left      = Root(2)
    m           = Root(1) 
    m.right     = Root(2)
    x           = Root(1)
    x.left      = Root(2) 
    x.right     = Root(1) 
    y           = Root(1)
    y.left      = Root(1)
    y.right     = Root(2) 
    res_1 = _same_BT(p, q)
    res_2 = _same_BT(n, m)
    res_3 = _same_BT(x, y)
    print('pass' if res_1 else res_1)
    print('pass' if not res_2 else res_2)
    print('pass' if not res_3 else res_3)



def _same_BT(tree1:Root, tree2:Root) -> bool: 
    '''  
    '''



def prob_03_sym_tree():
    '''  Given the root of a BT, check whether it is symmetric 
    sym_tree:        unsym_tree: 
            1            1 
           / \          / \
          2   2        2   2
         / \ / \        \   \
        3  4 4  3        3   3
    '''
    sym_tree                = Root(1)
    sym_tree.left           = Root(2)
    sym_tree.left.left      = Root(3)
    sym_tree.left.right     = Root(4)
    sym_tree.right          = Root(2)
    sym_tree.right.left     = Root(4)
    sym_tree.right.right    = Root(3)
    #-----------------------------
    unsym_tree              = Root(1)
    unsym_tree.left         = Root(2)
    unsym_tree.left.right   = Root(3)
    unsym_tree.right        = Root(2)
    unsym_tree.right.right  = Root(3)

    res_1 = _sym_tree(sym_tree) 
    res_2 = _sym_tree(unsym_tree) 

    print('pass' if res_1 else res_1)
    print('pass' if not res_2 else res_2)


def _sym_tree(bt:Root) -> bool: 
    '''  
    '''

    

def prob_04_BT_max_depth() -> None: 
    '''  Given the root for a BT find the max depth, i.e. the length of the 
    deepest node from its root

    tree_1:   tree_2: 
        3          1 
       / \        / \
      9  20      2   3
        /  \        / 
       15   7      4 
                    \
                     5
                    / \
                   6   7 
    '''
    tree_1              = Root(3)
    tree_1.left         = Root(9)
    tree_1.right        = Root(20)
    tree_1.right.left   = Root(15) 
    tree_1.right.right  = Root(7)
    #----------------------
    tree_2                          = Root(1)
    tree_2.left                     = Root(2)
    tree_2.right                    = Root(3)
    tree_2.right.left               = Root(4)
    tree_2.right.left.right         = Root(5) 
    tree_2.right.left.right.left    = Root(6) 
    tree_2.right.left.right.right   = Root(7) 
    res_1 = _BT_max_depth(tree_1)
    res_2 = _BT_max_depth(tree_2)

    print('pass' if res_1 == 3 else res_1)
    print('pass' if res_2 == 5 else res_2)


def _BT_max_depth(bt:Root) -> int: 
    '''  
    '''
    def _depth_len(node, lvl=0): 
        if node is None: 
            return lvl 
        lhs_depth = _depth_len(node.left, lvl + 1)
        rhs_depth = _depth_len(node.right, lvl + 1) 

        return max(lhs_depth, rhs_depth) 
    return _depth_len(bt)




def prob_05__depth_first_search(): # RECORD_TIME: 
    '''  U're given a `Root` class that takes a val and an arr of optional 
    `children` nodes. Impl the `depth_first_serach` on the `Root` class, which takes in an 
    empty arr, traverse the tree using the method from left to right, stores all of the 
    nodes names in an array, and returns it. 
    Ex: 
    tree =    A
            / | \
           B  C  D
          / \   / \
         E   F G   H
            / \ \
           I   J K
    '''
    root   = Root('A')
    root.add_child('B')
    root.add_child('E')
    root.add_child('F')
    root.add_child('I')
    root.add_child('J')
    root.add_child('C')
    root.add_child('D')
    root.add_child('G')
    root.add_child('K')
    root.add_child('H')
    ans = ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
    res = root.depth_first_search([])
    print('pass' if res == ans else res)



if __name__ == '__main__':

    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n')
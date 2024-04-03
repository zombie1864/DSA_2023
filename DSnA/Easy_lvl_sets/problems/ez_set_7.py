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

class Node:
    def __init__(self, val) -> None:
        self.val = val 
        self.nxt = None


class LList():
    def __init__(self) -> None:
        pass

    def add_node(self, val): 
        '''  '''
        
    def rm_dups(self): 
        '''  '''

    def print_list(self): 
        '''  '''


def prob_01_add_nodes_2_LL():
    '''  
    In prob set 1 we intro'ed del nodes from a link list by rm'in dups. 
    Write an algo that appends nodes 2 da end of a ll and prints da res'in ll 
    '''
    llist = LList() 
    llist.add_node(1)
    llist.add_node(2)
    llist.add_node(3)
    llist.print_list() # 1 -> 2 -> 3 -> None
        


def prob_02_sum_links():
    '''  
    U have 2 ints repr'ed by a llist, where each node contains a single 
    digit. Da order of the num is reversed, such that the head of da
    llist is at da tail. Write a fn that adds da 2 num and returns 
    da sym a reversed llist. 
    EX: 
        input: (7 -> 1 -> 6) + (5 -> 9 -> 2) // 617 + 295
        output: 2 -> 1 -> 9 // 617 + 295 = 912 
    '''
    llist_1 = LList() 
    llist_1.add_node(7)
    llist_1.add_node(1)
    llist_1.add_node(6)

    llist_2 = LList() 
    llist_2.add_node(5)
    llist_2.add_node(9)
    llist_2.add_node(2)

    _sum_links(llist_1, llist_2)

def _sum_links(ll1, ll2): 
    '''  '''



def prob_03_rm_dups():
    '''  
    rm dups from an unsorted llist
    '''
    llist = LList() 
    llist.add_node(1)
    llist.add_node(2)
    llist.add_node(3)
    llist.add_node(2)
    llist.add_node(4)
    llist.add_node(3) 
    llist.print_list() #output: 1->2->3->2->4->3->None 
    llist.rm_dups()
    llist.print_list() #output: 1->2->3->4->None 



def prob_04_del_mid_node(): 
    '''  
    Impl code 2 del a node in btw(first_node, last_node) in a single llist, 
    given acc only 2 that node. Da code returns None. 
    Ex: 
        llist: a->b->c->d->e->f
        input: 'c' 
        output: a->b->d->e->f 
    '''
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f') 
    a.nxt = b 
    b.nxt = c 
    c.nxt = d 
    d.nxt = e
    e.nxt = f 

    _del_node(c) 

    curr_node = a 
    while curr_node is not None: 
        print(curr_node.val, end=' -> ') 
        curr_node = curr_node.nxt 
    print('None') 

def _del_node(node): 
    '''  ''' 


def prob_05_palindrome_llist():
    '''  
    impl a fn 2 check if a llist is a palindrome. A palindrome is a ds 
    that is the same forward and backwards. 
    EX:
        1->2->3->2->1 // true 
        1->2->1->0 // false 
    '''
    llist_1 = LList() 
    llist_2 = LList() 
    llist_1.add_node(1)
    llist_1.add_node(2)
    llist_1.add_node(3)
    llist_1.add_node(2)
    llist_1.add_node(1)
    llist_2.add_node(1)
    llist_2.add_node(2)
    llist_2.add_node(1)
    llist_2.add_node(0)
    print('pass' if _palindrome_llist(llist_1) else _palindrome_llist(llist_1))
    print('pass' if not _palindrome_llist(llist_2) else _palindrome_llist(llist_2))


def _palindrome_llist(ll):
    '''  '''



if __name__ == '__main__':
    '''  '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
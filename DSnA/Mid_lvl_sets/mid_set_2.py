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


def prob_01_list_of_depth(): 
    # Example usage:
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # Create linked lists of nodes at each depth
    lists = _create_level_linked_lists(root)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _create_level_linked_lists(root):
    if not root:
        return []

    result = []
    current_level = []
    queue = [(root, 0)]  # Queue to store nodes along with their depths

    while queue:
        node, depth = queue.pop(0)
        
        # If it's a new depth, create a new linked list for it
        if len(result) == depth:
            result.append(ListNode(node.val))
            current_level.append(result[depth])
        else:
            current_level[depth].next = ListNode(node.val)
            current_level[depth] = current_level[depth].next

        # Enqueue left and right children with their depths
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return result

def prob_02_(): 
    # Example usage:
    # Constructing a balanced binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(is_balanced(root))  # Output: True

    # Constructing an unbalanced binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)

    print(is_balanced(root))  # Output: False

def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def is_balanced(root):
    if not root:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    
    return False




if __name__ == '__main__':
    ''' '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
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


def prob_01_BFS_undirected_graph(): 
    '''  
    An undirected graph is a network of interconnected nodes that do not have a 
    general direction or flow. They represent the relationship between entities 
    in both direction, often forming a symmetric shape. For example, in a social network
    usr A is friends w usr B, then usr B is also friends w usr A, making it model as an 
    undirected graph. They key point of these graphs is it's symmetry. A corner stone 
    and fundamental concept in graph theory. 

    The conncections, often called `adjacency`, btw two vertices/nodes that r 
    connected by an edge is a collection of arrs. Each arr repr vertect in da 
    graph. 
    EX:  
            A
         /     \
        B-------C
    Da adjacency repr this graph is 
    @ Node A: [B, C] 
    @ Node B: [A, C] 
    @ Node C: [A, B]

    Given an undirected graph repr as an adjacency list (a ds used 2 repr a graph)
    and a src node, impl BFS (Breadth-First Search) 2 traverse da graph starting 
    from the given src node. Print the nodes visted during BFS traversal, note
    that the order does not matter. 
    '''
    src_node = 'A' 
    graph = {
        'A': {'B', 'C'}, 
        'B': {'A', 'D', 'E'}, 
        'C': {'A', 'F'}, 
        'D': {'B'}, 
        'E': {'B', 'F'}, 
        'F': {'C', 'E'} 
    }
    print(_BFS_undirected_graph(graph, src_node)) #=> 'A B C D E F' @least 

def _BFS_undirected_graph(G, src): 
    '''  '''
    seen    = set() 
    queue   = [src]

    while queue: 
        node = queue.pop(0)
        if node not in seen: 
            print(node, end=' ') 
            seen.add(node)
            queue.extend(G[node] - seen) # extend appens an iter like set 2 list



def prob_02_BT_BFS(): 
    '''  
    Given a BT, impl BFS 2 print the node in level order travsersal
    '''
    root                = BT(1) 
    root._left          = BT(2)
    root._right         = BT(3)
    root._left._left    = BT(4)
    root._left._right   = BT(5)
    root._right._left   = BT(6)
    root._right._right  = BT(7)
    print(_BT_BFS(root)) #=> 1 2 3 4 5 6 7 

class BT:
    def __init__(self, val) -> None:
        self._val   = val 
        self._left  = None 
        self._right = None 

def _BT_BFS(root:BT) -> None: 
    '''  '''
    if not root: 
        return 
    queue = [root] 

    while queue: 
        node = queue.pop(0)
        print(node._val, end=' ') 
        
        if node._left: 
            queue.append(node._left) 
        if node._right: 
            queue.append(node._right) 



def prob_03_shortest_path():
    '''  
    Given a grid with obstacles, find da shortest path from da top-left corner 2 da 
    bottom-right corner. 
    '''
    grid = [
        [0, 0, 0, 0], 
        [1, 1, 0, 1], 
        [0, 0, 0, 0], 
        [0, 1, 1, 0]
    ]
    res = _shortest_path(grid)
    print(res) 

def _shortest_path(M:List[List[int]]) -> int: 
    '''  '''
    dirs        = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
    rows, cols  = len(M), len(M[0]) 
    queue       = [(0, 0, 0)] # (x, y, dis) | x, y = 0 start coord | dis = 0 (distance) 

    while queue: 
        x, y, dis = queue.pop(0) 
        if (x, y) == (rows - 1, cols - 1): # (rows - 1, cols - 1) bottom right corner 
            
            return dis + 1
        
        for a, b in dirs: 
            dx = x + a 
            dy = y + b 

            if 0 <= dx < rows and 0 <= dy < cols and M[dx][dy] == 0: 
                queue.append((dx, dy, dis + 1)) 

    return -1 

            





if __name__ == '__main__':
    '''  '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
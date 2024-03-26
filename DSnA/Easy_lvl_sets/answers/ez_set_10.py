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



def prob_01_grouped_anagrams_w_o_hasing(): 
    '''  
    Given a List[str], group anagrams together with its variants as el in a container
    arr and return the res'in arr. Anagrams are words that when its characters r 
    rearranged it forms another word. Impl w/o using hashing. 
    '''
    res = _group_anagrams_w_o_hashing(["eat", "tea", "tan", "ate", "nat", "bat"])
    ans = [["eat","tea","ate"],["tan","nat"],["bat"]]
    print('pass' if res == ans else res)


def _group_anagrams_w_o_hashing(arr): 
    freq = None 
    res = [] 
    group_anagrams = [] 

    while len(arr) > 0: 
        first_word = arr.pop(0) 
        group_anagrams = [first_word] 
        freq = _create_word_freq(first_word) 
        for i, word in enumerate(arr): 
            is_anagram = True 
            
            for char in word: 
                if char not in freq: 
                    is_anagram = False 
                    break 
            if is_anagram: 
                group_anagrams.append(word) 
                arr.pop(i) 
        res.append(group_anagrams) 
        freq = None 
        group_anagrams = [] 
    
    return res 


def _create_word_freq(word): 
    freq = {} 
    for char in word: 
        if char in freq: 
            freq[char] += 1 
        else: 
            freq[char] = 1

    return freq 



def prob_02_grouped_anagrams_w_hasing():
    '''  
    Given a List[str], group anagrams together with its variants as el in a container
    arr and return the res'in arr. Anagrams are words that when its characters r 
    rearranged it forms another word. Impl w/o using hashing. 
    '''
    res = _group_anagrams_w_hashing(["eat", "tea", "tan", "ate", "nat", "bat"])
    ans = [["eat","tea","ate"],["tan","nat"],["bat"]]
    print('pass' if res == ans else res)


def _group_anagrams_w_hashing(arr):
    group_anagrams = {} 

    for word in arr: 
        sorted_chars = ''.join(sorted(word)) 

        if sorted_chars in group_anagrams: 
            group_anagrams[sorted_chars].append(word) 
        else: 
            group_anagrams[sorted_chars] = [word] 

    return list(group_anagrams.values())



def prob_03_check_str_nPr(): 
    '''  
    Given 2 strs, write a fn 2 decide if one is a permutation of da other. 
    NOTE: in math nPr means permutation 
    '''
    print('pass' if _check_nPr('cat', 'act') else _check_nPr('cat', 'act'))
    print('pass' if not _check_nPr('cat', 'dog') else _check_nPr('cat', 'dog'))
    print('pass' if not _check_nPr('cat', 'at') else _check_nPr('cat', 'at'))


def _check_nPr(str1, str2): 
    '''  '''
    if len(str1) != len(str2):
        return False 
    
    char_freq = {} 

    for c in str1: 
        if c in char_freq: 
            char_freq[c] += 1
        else: 
            char_freq[c] = 1 
    
    for c in str2: 
        if c not in char_freq: 
            return False 
    
    return True 




def prob_04_palindrome_permutation():
    '''  
    Given a str, write a fn to check if it is a permutation of a palindrome. 
    A palindrome is a word or phrase that is the same forwards and backwards. 
    A permutation is a rearrangement of letters. The palindrome does not 
    need to be limited to just dictionary words.
    EX:
        Input:  Tact Coa
        Output: True (permutations: "taco cat", "atco cta", etc.)
    '''
    print('pass' if _palindrome_nPr('Tact Coa') else _palindrome_nPr('Tact Coa'))


def _palindrome_nPr(txt): 
    '''  
    '''
    txt = txt.replace(' ', '').lower() # 'cleans' input 
    char_freq = {} 

    for char in txt: 
        if char in char_freq: 
            char_freq[char] += 1
        else: 
            char_freq[char] = 1 

    # odd count permutation methodology used 4 palindrome 
    odd_count = 0 # most chars occur an even num of times 2 keep symmetry 

    for n in char_freq.values():
        if n % 2 != 0: 
            odd_count += 1 # `pivot` char divides the sym pattern 
        if odd_count > 1: # more than 1 pivot disrupts sym balance 
            return False 
        
    return True 



def prob_05_two_sum():
    '''  
    Given a List[int] and a trg, return the 2 indicies of the 2 ints such that 
    they add up to da trg, achieve this in O(logN) and NOT O(N) 
    '''
    print('pass' if _two_sum([2, 7, 11, 15], 9) == [0, 1] else _two_sum([2, 7, 11, 15], 9))


def _two_sum(arr, trg): 
    conj_idx = {} # conjugate indices 

    for i, n in enumerate(arr): 
        conj_n = trg - n 

        if conj_n in conj_idx: 
            return [conj_idx[conj_n], i] 
        conj_idx[n] = i 
    return []
  
  

if __name__ == '__main__':
    '''  '''
    print('\n----------[ START ]----------\n')
    main()
    print('\n----------[ END ]----------\n') 
'''  
When working with a large number of iterations, using loops will have 
slowdowns depending if the algo runs on one of type of operation order: 
O(n), O(log n), O(n log n), O(x^n)
Vectorization helps improve speed performances when you are able to use it. 

What is vectorization? 
Vectorization is the technique of implementing (NumPy) array operations on a dataset. In the background, 
it applies the operations to all the elements of an array or series in one go (unlike a for loop that manipulates one row at a 
time).
'''

import time 



def sum(num: int) -> None: 
    '''  '''
    start_time = time.time() 
    tot = 0 

    for n in range(0, num): 
        tot += n 

    print(f'Sum is: {tot}') 
    end_time = time.time() 

    print(f'Time operation: {end_time - start_time}')



sum(150000000) # 15 mil numbers 
'''  
Sum is: 11249999925000000
Time operation: 8.082597732543945
'''


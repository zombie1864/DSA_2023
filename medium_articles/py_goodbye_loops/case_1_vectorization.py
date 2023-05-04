import time 
import numpy as np 



def sum(num): 
    '''  '''
    start_time = time.time() 

    print(np.sum(np.arange(num)))

    end_time = time.time() 
    print(f'Time operation: {end_time - start_time}')



sum(150000000) # 15 mil numbers 
'''  
-1186941120
Time operation: 0.32314181327819824

for now ignore the negative sum - but look at the massive difference in speed between 
vectorization and for loop 
'''


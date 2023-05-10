'''  
In data science, using pandas `DataFrame` method, developers use loops 
to create new derived columns using mathematical operations. 
Data frames are tabular data in the form of rows and columns - essentially 
creating an excel spreedsheet. 

Below we are creating 150,000,000 mil rows and 4 col filed 
with random values between 0 and 50 
'''

import time 
import numpy as np 
import pandas as pd 

dataframe = pd.DataFrame(
    np.random.randint(1, 50, size=(1000000, 4)), columns=('a', 'b', 'c', 'd') 
) 

dataframe.shape 
dataframe.head() 

# we will create a new col 'ratio' to find the ratio of the col 'd' and 'c' using loops 

def create_ratio_col(): 
    '''  '''
    start_time = time.time() 
    
    for idx, row in dataframe.iterrows(): 
        # create new column 
        dataframe.at[idx, 'ratio'] = 100 * (row['d'] / row['c'])
    
    end_time = time.time() 

    print(end_time - start_time) 


create_ratio_col() # 54 sec 


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

df = pd.DataFrame(np.random.randint(0, 50, size=(150000000)), columns=('a', 'b', 'c', 'd')) 
df.shape 
df.head() 

# we will create a new col 'ratio' to find the ratio of the col 'd' and 'c' using loops 
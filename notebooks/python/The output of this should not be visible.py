# !pip3 install pandas
# !pip3 install numpy

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
df.head()

g = df.hist()

# # This is a test markdown 

df.describe()



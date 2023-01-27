#%%

import numpy as np
import pandas as pd
from numpy.linalg import inv

#%%

class OLS:
    def __init__(self,y,X):
        self.y = y
        self.X = X

    
    def b(self):
        coef = inv(X.T@X)@X.T@y
        return coef


#%%


X = [[1,2],[2,3],[1,3]]

y = [[4,2,3]]

X = np.array(X)
y= np.array(y).T


result = OLS(y,X)
result.b().T

#%%

X.T@y


#%%
X.shape
y.shape

#%%



#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%



#%%

import numpy as np
import pandas as pd
from numpy.linalg import inv
from numpy import array as arr
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm
import scipy


#%%

fama = pd.read_csv("25_Portfolios_ME_INV_5x5.txt", sep='\s+')
factors = pd.read_csv("F-F_Research_Data_5_Factors_2x3.csv")
ri = fama.query('index > 196206  & index < 201400 ')
factors = factors.query('month > 196206  & month < 201400 ')
factors = factors.drop(columns=['month','RF'])
factors = sm.add_constant(factors)
factors.describe()


#%%

re = ri.apply( lambda x: x-factors.RF.tolist() )
re = re.reset_index(drop=True)


table1 = ri.mean()-factors.RF.mean()
table1 = [round(x,2) for x in table1]
table1

#%%

re.describe().loc['mean']


#%%

a = []
b = []
s = []
h = []
r = []
c = []
e = []


t_a = []
t_b = []
t_s = []
t_h = []
t_r = []
t_c = []


for i in re.columns:

    model = OLS(re[i],factors[[i for i in factors.columns ]])
    results = model.fit()
    a.append(results.params.loc['const'].tolist())
    b.append(results.params.loc['Mkt-RF'].tolist())
    s.append(results.params.loc['SMB'].tolist())
    h.append(results.params.loc['HML'].tolist())
    r.append(results.params.loc['RMW'].tolist())
    c.append(results.params.loc['CMA'].tolist())

    t_a.append(results.tvalues.loc['const'].tolist())
    t_b.append(results.tvalues.loc['Mkt-RF'].tolist())
    t_s.append(results.tvalues.loc['SMB'].tolist())
    t_h.append(results.tvalues.loc['HML'].tolist())
    t_r.append(results.tvalues.loc['RMW'].tolist())
    t_c.append(results.tvalues.loc['CMA'].tolist())

    e.append(results.resid)
    


    
#%%  GRS test of times series

T = re.shape[0]
N = 25
K = 5
Ef = factors.describe().loc['mean'][1:].tolist()

Omega = 0
for t in range(T):
    f = factors.iloc[t].tolist()

    f_d = [[ Ef[j]-f[j] for j in range(5) ]]
    f_d = arr(f_d)
    Omega += f_d.T@f_d

Omega = Omega/T


Ef = arr([Ef])



Part2 = 1/(1+Ef@ inv(Omega)@Ef.T)

e = arr(e)

Sig = 0
for t in range(T):
    eps = arr([e[:,t]])
    Sig += eps.T@eps

Sig = Sig/T

alpha = arr([a])

Part3 = alpha@inv(Sig)@alpha.T

GRS = (T-N-K)/N * Part2 * Part3



(1-scipy.stats.f.cdf(GRS, N, T-N-K, loc=0, scale=1))*2







#%%

for i in factors.columns:
    print(i)


#%%

for i in re.columns:
    print(re[[i]])



#%%
Ef = factors.describe().loc['mean'][1:].tolist()
f = factors.iloc[0].tolist()

[ Ef[j]-f[j] for j in range(5) ]



#%%

factors['SMB'].tolist()



#%%

results.params.loc['const']



#%%


f

#%%




#%%




#%%




#%%




#%%




#%%




#%%





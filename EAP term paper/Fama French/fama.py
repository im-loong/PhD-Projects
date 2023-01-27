#%%
import numpy as np
import pandas as pd
from reg import *


#%%

fama = pd.read_csv("F-F_Research_Data_5_Factors_2x3.txt", sep='\s+')
q_f = pd.read_csv('benportf_me_ia_roe_monthly_2021.csv')
q_5 = pd.read_csv('q5_factors_monthly_2021.csv')
q_5['X_MKT'] = q_5['R_MKT'] - q_5['R_F']

#%%

print(q_5)


#%%

a=q_f.describe()
print(a)
#%%


#%%

q_f_test = q_f.query('year ==1967 & month ==1')
q_f_test2 = q_f.query('year ==1967 & month ==2')


#%%

q_f_rme = q_f_test.query(' rank_ME == 1 ')
q_f_rme2 = q_f_test.query(' rank_ME == 2 ')
q_f_rme['ret_vw'].mean()- q_f_rme2['ret_vw'].mean()

#%%


q_111 = q_f.query( ' rank_ME==1 & rank_IA==1 & rank_ROE==1 ' )





#%%

y = q_111['ret_vw']

X = q_5[['X_MKT','R_ME','R_IA','R_ROE']]

res_OLS = OLS(y,X)


#%%
print(X)

np.array(X)
X.shape


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
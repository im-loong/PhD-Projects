#%%
import numpy as np
import pandas as pd
from numpy.linalg import inv
from numpy import array as arr

#%%

class OLS:
    def __init__(self,y,X):
        self.y = y
        self.X = X

    
    def b(self):
        coef = inv(X.T@X)@X.T@y
        return coef



#%%

fama = pd.read_csv("F-F_Research_Data_5_Factors_2x3.txt", sep='\s+')
q_f = pd.read_csv('benportf_me_ia_roe_monthly_2021.csv')
q_5 = pd.read_csv('q5_factors_monthly_2021.csv')
q_5['X_MKT'] = q_5['R_MKT'] - q_5['R_F']
q_5['ones'] = np.ones(q_5.shape[0])

#%%



#%%

# time series
q_f = q_f.query('year > 1971  & year < 2013 ')
q_5 = q_5.query('year > 1971  & year < 2013 ')
X = q_5[[ 'ones','X_MKT','R_ME','R_IA','R_ROE']]
X = np.array(X)

betas = []

y_bar = []

for i in [1,2]:
    for j in [1,2,3]:
        for k in [1,2,3]:
            q_t = q_f[(q_f.rank_ME == i) & (q_f.rank_IA == j) & (q_f.rank_ROE == k)]

            y = [q_t['ret_vw']-list(q_5['R_F'])]
            y_bar.append(np.mean(y))

            y=np.array(y).T

            res = OLS(y,X)
            b = np.squeeze(res.b())
            b = b.tolist()

            betas.append(b)
beta_df = pd.DataFrame(betas)

beta_df.describe()

for i in betas:
    i.pop(0)

pd.DataFrame(betas).describe()


#%%
# cross sectional - standard

N=18
K=4




y = [y_bar]

y=np.array(y).T

betas = arr(betas)
b= inv(betas.T@betas)@betas.T@y
e= y-betas@b

s2 = e.T@e /(N-K)
s2= np.squeeze(s2).sum()
var_b = s2* inv(betas.T@betas)

b = np.squeeze(b).tolist()
e=np.squeeze(e).tolist()





#%%

# cross sectional - fama mcbeth

N=18
K=4



years = q_f.year.unique()
months = q_f.month.unique()

lambdas = []
alphas = []

for i in years:
    for j in months:

        q_c = q_f[(q_f.year == i) & (q_f.month == j)]
        y = q_c['ret_vw']
        rf = q_5[(q_5.year == i) & (q_5.month == j)].R_F.sum()

        y = [y-rf ]
        y=np.array(y).T

        betas = arr(betas)
        b= inv(betas.T@betas)@betas.T@y
        e= y-betas@b

        s2 = e.T@e /(N-K)
        s2= np.squeeze(s2).sum()
        var_b = s2* inv(betas.T@betas)

        b = np.squeeze(b).tolist()
        e=np.squeeze(e).tolist()

        lambdas.append(b)
        alphas.append(e)




#%%



#%% sample estimates of lambda and alpha



a=pd.DataFrame(alphas).describe()
alpha_i = a.loc['mean'].tolist()

b=pd.DataFrame(lambdas).describe()
lambda_hat = b.loc['mean'].tolist()

#%%


lambda_hat


#%%

t=[]
for i in range(4):
    t.append(
        lambda_hat[i]/ (np.sqrt( var_b[i,i] ))
    )
t

#%%

lambda_hat

#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%
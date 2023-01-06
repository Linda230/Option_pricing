import numpy as np
import matplotlib.pyplot as plt
from sobol_normal import generate_sobol
from sobol_normal import normal

# calculate the price of Asian option
def asian_path(S,r,sigma_0,T,steps,N):
  Sigma = [sigma_0] 
  # construct B-S-M model with GARCH(1,1) volatility
  for j in range(1, T):
    if j == 1:
      sigma_j = np.sqrt(0.0006 + 0.1 * (0.0003)**2 + 0.85 *(sigma_0)**2)
      Sigma.append(sigma_j)
    else:
      sigma_j = np.sqrt(0.0006 + 0.95 * Sigma[j-1] ** 2)
      Sigma.append(sigma_j)

  original = np.zeros((N,1))
  dt = T/steps
  for m, sigma in enumerate(Sigma):
    increments = (r - sigma**2/2)*dt + sigma*np.sqrt(dt)*np.expand_dims(sobol_normal[:,m], axis=1) 
    original = np.concatenate([original, increments], axis=1)

  lnS = np.log(S) + np.cumsum(original,axis=1)
  ST_sum = np.sum(np.exp(lnS), axis=1)
  AT = np.mean(np.exp(lnS), axis=1)

  return ST_sum, AT

S = 50 #stock price S_{0}
K = 50 # strike
T = 90 # time to maturity, 30/90/180 days
r = 0.0005 # risk free risk in day %
sigma_0 = 0.02 # daily volatility at initial time
steps = 90 # time steps = T
N = 10000 # number of trials 1000/10000/100000

# generate Sobol normal data
sobol_data = generate_sobol(N, T)
sobol_normal = normal(sobol_data, N, T) 

# calculate the price of asian option
ST_sum, AT = asian_path(S,r,sigma_0,T,steps,N)
print(ST_sum.shape)
print(AT.shape)

Return = np.concatenate([np.expand_dims(AT-K, axis=1),np.zeros((N,1))],axis=1) 
C = np.exp(-r*T) * np.max(Return, axis=1) # the maturity return of underlying asset
# C_mean = np.mean(C) 
# print(C_mean)

# construct control variable
Expection_S =S * (1-np.exp(r*T))/(1-np.exp(r*(T/steps)))
# construct the coefficient 
cov = np.cov(ST_sum, C)[0,1]
var = np.var(ST_sum)
corrcoef = cov / var  
# obtain the final variable
Control = C - corrcoef * (ST_sum - Expection_S)
Control_mean = np.mean(Control)

# the price of asian optice
print("price of asian optice", Control_mean)

# the standard error using Quasi-Monte-Carlo and Control Variable
print('standard error using quai-MC and control variable', np.sqrt(np.var(Control))/np.sqrt(N))

### The generation of Sobol normal sequence 
import numpy as np
import matplotlib.pyplot as plt
import openturns as ot

# Create a Sobol sequence of N points of T dimensions
def generate_sobol(N, T):
  sequence_sobol = ot.LowDiscrepancySequence(ot.SobolSequence(T))
  sobol_data = sequence_sobol.generate(N)
  sobol_data = np.array(sobol_data)# Convert a data type to an array
  return sobol_data

def normal(data,N,T):
  a0 = 2.50662823884
  b0 = 1.00
  b1 = -8.47351093090
  a1 = -18.61500062529
  b2 = 23.08336743743
  a2 = 41.39119773534
  b3 = -21.06224101826
  a3 = -25.44106049637
  b4 = 3.13082909833
  c0 = 0.3374754822726147
  c5 = 0.0003951896511919
  c1 = 0.9761690190917186
  c6 = 0.0000321767881768
  c2 = 0.1607979714918209 
  c7 = 0.0000002888167364
  c3 = 0.0276438810333863 
  c8 = 0.0000003960315187
  c4 = 0.0038405729373609
  x = np.zeros(shape=(N,T))
  y = np.zeros(shape=(N,T))

  for i in range(0, N):
    for j in range(0, T):
      y[i,j] = data[i,j] - 0.5
      if np.abs(y[i,j]) < 0.42:
        r = y[i,j] * y[i,j]
        x[i,j] = y[i,j] * (((a3*r+a2)*r+a1)*r+a0) / ((((b4*r+b3)*r+b2)*r+b1)*r+b0)
      else:
        r = data[i,j]
        if y[i,j] >0:
          r = 1- data[i,j]
        r = np.log(-np.log(r))
        x[i,j] = c0 + r * (c1+r*(c2+r*(c3+r*(c4+r*(c5+r*(c6+r*(c7+r*c8)))))))
        if y[i,j] <0:
          x[i,j] = -x[i,j]
  return x



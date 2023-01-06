
# The code for Figure 1
import numpy as np
import openturns as ot
import matplotlib.pyplot as plt

# Create a random number of 1000 points of 2 dimensions
rand_data = np.random.uniform(low=0.0, high=1.0, size=(1000,2))


# Create a Halton sequence of 1000 points of 2 dimensions
sequence_halton = ot.LowDiscrepancySequence(ot.HaltonSequence(2))
halton_data = sequence_halton.generate(1000)
halton_data = np.array(halton_data)# Convert a data type to an array

# Create a Faure sequence of 1000 points of 2 dimensions
sequence_faure = ot.LowDiscrepancySequence(ot.FaureSequence(2))
faure_data = sequence_faure.generate(1000)
faure_data = np.array(faure_data)# Convert a data type to an array

# Create a Sobol sequence of 1000 points of 2 dimensions
sequence_sobol = ot.LowDiscrepancySequence(ot.SobolSequence(2))
sobol_data = sequence_sobol.generate(1000)
sobol_data = np.array(sobol_data)# Convert a data type to an array

fig, ax = plt.subplots(2,2,figsize = (10, 7))
# Uniform
plt.subplot(221)
plt.plot(rand_data[:,0],rand_data[:,1],'b.',)
plt.title('Uniform')

# Halton
plt.subplot(222)
plt.plot(halton_data[:,0],halton_data[:,1],'b.',)
plt.title('Halton')

# Faure
plt.subplot(223)
plt.plot(faure_data[:,0],faure_data[:,1],'b.',)
plt.title('Faure')

# Sobol
plt.subplot(224)
plt.plot(sobol_data[:,0],sobol_data[:,1],'b.',)
plt.title('Sobol')

plt.subplots_adjust(top=0.9, bottom=0.09, left=0.1, right=0.9, hspace=0.25,
                    wspace=0.25)
                
plt.savefig('scatter.eps',dpi=150)

plt.show()


 # The code for Figure 2
import numpy as np
import openturns as ot
import matplotlib.pyplot as plt

# Create a Halton sequence of 1000 points of 30 dimensions
sequence_halton = ot.LowDiscrepancySequence(ot.HaltonSequence(30))
halton_data = sequence_halton.generate(1000)
halton_data = np.array(halton_data)# Convert a data type to an array

# Create a Faure sequence of 1000 points of 60 dimensions
sequence_faure = ot.LowDiscrepancySequence(ot.FaureSequence(60))
faure_data = sequence_faure.generate(1000)
faure_data = np.array(faure_data)# Convert a data type to an array

# Create a Sobol sequence of 1000 points of 60 dimensions
sequence_sobol_01 = ot.LowDiscrepancySequence(ot.SobolSequence(60))
sobol_data_01 = sequence_sobol_01.generate(1000)
sobol_data_01 = np.array(sobol_data_01)# Convert a data type to an array

# Create a Sobol sequence of 1000 points of 250 dimensions
sequence_sobol_02 = ot.LowDiscrepancySequence(ot.SobolSequence(250))
sobol_data_02 = sequence_sobol_02.generate(1000)
sobol_data_02 = np.array(sobol_data_02)# Convert a data type to an array

fig, ax = plt.subplots(2,2,figsize = (10, 7))

# Halton_29*30
plt.subplot(221)
plt.plot(halton_data[:,28],halton_data[:,29],'b.',)
plt.title('Halton 29 * 30')

# Faure_59*60
plt.subplot(222)
plt.plot(faure_data[:,58],faure_data[:,59],'b.',)
plt.title('Faure 59 * 60')

# Sobol_59*60
plt.subplot(223)
plt.plot(sobol_data_01[:,58],sobol_data_01[:,59],'b.',)
plt.title('Sobol 59 * 60')

# Sobol_249*250
plt.subplot(224)
plt.plot(sobol_data_02[:,248],sobol_data_02[:,249],'b.',)
plt.title('Sobol 249 * 250')

plt.subplots_adjust(top=0.9, bottom=0.09, left=0.1, right=0.9, hspace=0.25,
                    wspace=0.25)
                
plt.savefig('degradation.eps',dpi=150)

plt.show()


# Code for figure 3
import matplotlib.pyplot as plt
import numpy as np
from sobol_normal import generate_sobol
from sobol_normal import normal

normal_data = np.random.normal(loc=0, scale=1, size=(1000,30))

sobol_data_02 = generate_sobol(1000, 30)
sobol_normal_02 = normal(sobol_data_02, 1000, 30)  

sobol_data_03 = generate_sobol(1000, 90)
sobol_normal_03 = normal(sobol_data_03, 1000, 90)  

sobol_data_04 = generate_sobol(1000, 180)
sobol_normal_04 = normal(sobol_data_04, 1000, 180)  

fig, ax = plt.subplots(2,2,figsize = (10, 7))

# Sobol 29 * 30
plt.subplot(221)
plt.plot(normal_data[:,28],normal_data[:,29],'b.',)
plt.title('Normal  29 * 30')

# Sobol 59 * 60
plt.subplot(222)
plt.plot(sobol_normal_02[:,27],sobol_normal_02[:,28],'b.',)
plt.title('Sobol-Normal 29 * 30')

# Sobol 89 * 90
plt.subplot(223)
plt.plot(sobol_normal_03[:,88],sobol_normal_03[:,89],'b.',)
plt.title('Sobol-Normal 89 * 90')

# Sobol 179 * 180
plt.subplot(224)
plt.plot(sobol_normal_04[:,178],sobol_normal_04[:,179],'b.',)
plt.title('Sobol-Normal 179 * 180')

plt.subplots_adjust(top=0.9, bottom=0.09, left=0.1, right=0.9, hspace=0.25,
                    wspace=0.25)
                
plt.savefig('normal.eps',dpi=150)

plt.show()

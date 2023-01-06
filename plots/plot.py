# This program uses the pyplot module to plot two exponential 
# functions

import numpy as np
import matplotlib.pyplot as plt

# I generate a set of numbers between 0 and 8 for which the  
# functions will be calculated
x=np.linspace(0,8,100,endpoint=True)
print x

# I define the functions using the exp function from numpy
y1=np.exp(0.3*x)
y2=6*np.exp(-x**2)

# Here the functions are plotted
plt.plot(x,y1)
plt.plot(x,y2)
plt.title ('Exponential plots')
plt.show()
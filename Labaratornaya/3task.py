import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-20,20.1,0.1)
def f(n):
    return np.log((n**2+1)*np.exp(-1*np.abs(x)/10))/np.log(1+np.tan(1/(1+(np.sin(n))**2)))
plt.plot(x,f(x))
plt.show()
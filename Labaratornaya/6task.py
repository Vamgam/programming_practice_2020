import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-2.1,2.1,0.01)
def w(n):
    m=0
    for i in range(200):
        m+=(0.5)**i*np.cos(3**i*np.pi*n)
    return m
plt.plot(x,w(x))
plt.show()
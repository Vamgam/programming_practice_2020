import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-0.1,6.2,0.1)
plt.plot(x,x*x-x*6,0*x)
plt.title(r'$f(x)=x^2-6x$')
plt.grid(True)

plt.show()
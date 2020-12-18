import matplotlib.pyplot as plot
import numpy as np
def func(x):
    if x>5:
        return 2*x
    if -5<=x<=5:
        return x**2
    if x<-5:
        return 2*abs(x)-1
x=np.arange(-10,10,0.1)
y = np.vectorize(func, otypes=[float])

plot.plot(x,y(x))
plot.show()

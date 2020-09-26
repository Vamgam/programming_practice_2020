import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10,11]
y=[0.99,0.49,0.35,0.253,0.18,0.12,0.09,0.073,0.060,0.050,0.036]
p,v=np.polyfit(x,y,deg=1,cov=True)
p2,v=np.polyfit(x,y,deg=2,cov=True)
plt.errorbar(x,y,xerr=0.05, yerr=0.1,fmt='none')
def P(x):
    return float(p[0])*x+float(p[1])
def P2(x):
    return float(p2[0])*x**2+float(p2[1])*x+float(p2[0])*x
m=np.arange(0,12,0.1)
plt.plot(m,P(m))
n=np.arange(0,12,0.1)
plt.plot(n,P2(n))
plt.grid()
plt.show()
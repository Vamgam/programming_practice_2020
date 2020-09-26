import numpy as np
x=[1,10,100]
def f(n):
    return np.log(((np.e)**(1/(np.sin(n)+1)))/(5/4+1/(n*5)))/np.log(1+n**2)
for i in x:
 print(f(i)," ", end='')
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10.1,0.1)
m=input()
with plt.xkcd():
    plt.plot(x,eval(m))
    plt.title("Твоя функция")
plt.show()
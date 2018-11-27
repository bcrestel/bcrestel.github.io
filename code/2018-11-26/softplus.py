import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,2000)
relu = (x>0)*x
sp = np.log(1+np.exp(x))

def f(a):
    return np.log(1. + np.exp(a*x))/a


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,relu,'k--', label='RELU')
ax.plot(x,sp, 'k', label='softplus')
ax.plot(x, f(2), 'r', label='a=2')
ax.plot(x, f(4), 'b', label='a=4')
ax.plot(x, f(8), 'g', label='a=8')
plt.legend(loc='best')
fig.savefig('softplus.png')

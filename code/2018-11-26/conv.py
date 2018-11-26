import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,1000)
s = 1./(1+np.exp(-x))   # logistic function
ds = s*(1.-s)
dds = ds - 2*s*ds

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, s, 'b', label='original')
ax.plot(x, s-dds, 'r', label='sharpened')
plt.legend(loc='best')
fig.savefig('laplacian.png')

sp = s[2:]
sm = s[:-2]
dds_fd = (sp - 2*s[1:-1] + sm) / (x[1]-x[0])**2
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, dds, label='derivative')
ax.plot(x[1:-1], dds_fd, label='fd')
plt.legend(loc='best')
fig.savefig('fd.png')

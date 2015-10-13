import numpy as np
import matplotlib.pyplot as plt

alpha = ['ABC', 'DEF', 'GHI', 'JKL']

data = np.random.random((4,4))

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(data, interpolation='nearest')
fig.colorbar(cax)

ax.set_xticklabels(['']+alpha)
ax.set_yticklabels(['']+alpha)

plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
hvap = pd.read_csv("Hvap.csv")
n_groups = len(hvap.D_OPLS)

opls = list(hvap.D_OPLS)
x_lab = list(hvap.Molecules)
cm5 = list(hvap.D_CM5)
cm1a = list(hvap.D_CM1A)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.33
opacity = 0.5
rects1 = plt.bar(index, opls, bar_width,
                 alpha=opacity,color='r',label='OPLS')
rects2 = plt.bar(index + bar_width, cm5, bar_width,
                 alpha=opacity,color='g',label='1.27*CM5')
rects3 = plt.bar(index + 2 * bar_width, cm1a, bar_width,
                 alpha=opacity,color='b',label='1.14*CM1A')
plt.ylabel(r'$\Delta H_{vap}^{expt}-\Delta H_{vap}^{calc}~$ (kcal/mol)')
plt.xticks(index + bar_width, x_lab, rotation=90)
plt.grid()
plt.xlim(-0.5, n_groups + 0.5)
plt.legend(loc='lower left', ncol=3)
plt.tight_layout()
plt.savefig("Tesh_hvap.pdf")

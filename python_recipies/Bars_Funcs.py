import matplotlib
matplotlib.use('Agg')
matplotlib.rc('font', family='serif')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.ticker import FuncFormatter
cm1a = pd.read_csv('CM1A_means.csv')
cm5 = pd.read_csv('CM5_means.csv')
m1=list(cm1a['CM1A_Scale_factor'])
m2=list(cm5['CM5_Scale_factor'])
################################
def millions(x, pos):
    'The two args are the value and tick position'
    return '%2.2f' % (x)
formatter = FuncFormatter(millions)
################################
colors = cm.Spectral(np.linspace(0, 1, len(m1)))
index = np.arange(len(m1))
bar_width = 1.0
opacity = 1.0
fig=plt.figure(figsize=(10, 5),dpi=300)
ax1=plt.subplot(121)
ax2=plt.subplot(122)
y1=list(cm1a['1.05'])
y2=list(cm5['1.21'])
ax1.xaxis.grid()
ax2.xaxis.grid()
ax1.yaxis.grid()
ax2.yaxis.grid()
for i in range(0,len(y1)):
  ax1.bar(index[i],y1[i],bar_width,color=cm.Spectral(1.*i/len(m1)),alpha=opacity)
ax1.set_xticks(index+0.5)
ax1.set_xticklabels(m1, rotation=90)
ax1.set_ylabel(r'MUE $\Delta G_{hyd}^{1.05*CM1A}$ (kcal/mol)',fontsize=16)
ax2.set_ylabel(r'MUE $\Delta G_{hyd}^{1.21*CM5}$ (kcal/mol)',fontsize=16)
for i in range(0,len(y2)):
  ax2.bar(index[i],y2[i],bar_width,color=cm.Spectral(1.*i/len(m2)),alpha=opacity)
ax2.set_xticks(index+0.5)
ax2.set_xticklabels(m2, rotation=90)
fig.subplots_adjust(left  = 0.15,hspace = .001)
plt.tight_layout(rect=[0.0,0.01,0.99,0.99])
plt.savefig("bar.pdf")


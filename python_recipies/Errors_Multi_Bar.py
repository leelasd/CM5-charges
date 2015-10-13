import matplotlib
matplotlib.use('Agg')
matplotlib.rc('font', family='serif')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import seaborn as sns
sns.set()
from matplotlib.ticker import FuncFormatter
hvap = pd.read_csv('Hvap.csv')
den = pd.read_csv('Den.csv')
d_std=pd.read_csv('STD_Den.csv')
h_std=pd.read_csv('STD_Hvap.csv')
h_std['CM5']=h_std.CM5_127
hvap.drop(hvap.columns[[1,2,3,4,5,7]], axis=1, inplace=True)
den.drop(den.columns[[1,2,3,4,5,7]], axis=1, inplace=True)
m1=list(hvap['Molecules'])
m2=list(den['Molecules'])
################################
def millions(x, pos):
    'The two args are the value and tick position'
    return '%2.2f' % (x)
formatter = FuncFormatter(millions)
################################
l1= (hvap.columns.values)[1:]
l2= (den.columns.values)[1:]
colors = cm.rainbow(np.linspace(0, 1, len(l1)))
fig,(ax1, ax2) = plt.subplots(2, sharex=True)
index = np.arange(len(m1))
bar_width = 1.0/len(l1)
opacity = 1.0
patterns = [  "*", "o", "."]
for i,c in zip(range(0,len(l1)),colors): 
	ax1.bar(index+bar_width*i,hvap[l1[i]] , bar_width,
        	         alpha=opacity,
        	         facecolor=c,
			 edgecolor = c,
#			 hatch=patterns[i],
        	         label=l1[i][2:],yerr=h_std[l1[i][2:]],ecolor='k',capsize=1)
ax1.legend(fontsize=10,loc=9, bbox_to_anchor=(0.5, 1.2),ncol=3,frameon=False)
ax1.set_ylabel(r'$\Delta H_{vap}^{expt}-\Delta H_{vap}^{calc}~$ (kcal/mol)')
ax1.yaxis.set_major_formatter(formatter)
ax1.yaxis.set_ticks(np.arange(-6,3,2))
for i,c in zip(range(0,len(l2)),colors): 
	ax2.bar(index+bar_width*i,den[l1[i]] , bar_width,
        	         alpha=opacity,
        	         facecolor=c,
			 edgecolor=c,
			 #hatch=patterns[i],
        	         label=l2[i][2:],yerr=d_std[l1[i][2:]],ecolor='k',capsize=1)
ax2.set_ylabel(r'$\Delta \rho^{expt}-\Delta \rho^{calc}~$ (g/cc)')
ax2.yaxis.set_ticks(np.arange(-0.1,0.08,0.04))
plt.xticks(index + bar_width*len(l2)/2, m2, rotation=90,fontsize=10)
#ax1.xaxis.grid()
#ax2.xaxis.grid()
#ax1.yaxis.grid()
#ax2.yaxis.grid()
ax1.set_xlim(-0.1, len(m1) + 0.0)
ax2.set_xlim(-0.1, len(m2) + 0.0)
plt.tight_layout(rect=[0.0,0.01,0.89,0.99])
plt.savefig("Ers_Multi_bar.pdf")

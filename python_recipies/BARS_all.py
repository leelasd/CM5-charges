import matplotlib
matplotlib.use('Agg')
matplotlib.rc('font', family='serif')
from matplotlib import pylab
from pylab import rcParams
rcParams['figure.figsize'] = 11, 7
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
dat = pd.read_csv('all_cm5_dat.csv')
method=list(dat['Molecules'])
################################
legend= (dat.columns.values)[1:]
#colors = cm.Greens(np.linspace(0, 1, len(legend)))
colors = cm.Spectral(np.linspace(0, 1, len(legend)))
index = np.arange(len(method))
bar_width = 1.0/len(legend)
opacity = 1.0
for i,c in zip(range(0,len(legend)),colors): 
	plt.bar(index+bar_width*i,dat[legend[i]] , bar_width,
        	         alpha=opacity,
        	         color=c,
        	         label=legend[i])
plt.ylabel(r'$\Delta H_{vap}^{expt}-\Delta H_{vap}^{calc}~$ (kcal/mol)',fontsize=14)
plt.xticks(index + bar_width*len(legend)/2, method, rotation=90,fontsize=12)
plt.grid()
plt.xlim(-0.1, len(method) + 0.0)
#plt.legend(bbox_to_anchor=(1.0, 1.01),fontsize=9,loc=0,frameon=False)
plt.legend(loc='upper left', ncol=6,fontsize=10, frameon=False)
plt.tight_layout(rect=[0.0,0.01,0.99,1])
plt.savefig("Thh.pdf")

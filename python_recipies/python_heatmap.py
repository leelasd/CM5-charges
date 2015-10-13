import matplotlib
matplotlib.use('Agg')
matplotlib.rc('font', family='serif')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dat = pd.read_csv("Ar_Hm_dat.csv")
for i in list(dat.columns.values)[1:]:
        print ('%3s %3s %3.3f %3s %3.3f'%(i,dat.DFT[dat[i].idxmin()],dat[i].min(),dat.DFT[dat[i].idxmax()],dat[i].max()))
t = list (dat.columns.values)
methods = t[1:]
mols = list (dat.DFT)
budat = dat
dat =dat.drop('DFT',axis=1)
fig=plt.figure(figsize=(5,5))
plt.imshow(dat,cmap=plt.get_cmap('bwr'), interpolation='nearest')
plt.colorbar(fraction=0.046, pad=0.04)
plt.gca().xaxis.set_ticks_position('top')
plt.xticks(range(0,len(methods)),methods,rotation=90)
plt.yticks(range(0,len(mols)),mols,rotation=0)
plt.tight_layout()
plt.savefig('hm_anion.pdf')
plt.savefig('hm_anion.png',res=300)

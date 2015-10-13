import matplotlib
matplotlib.use('Agg')
matplotlib.rc('font', family='serif')
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
cm5=pd.read_csv("CM5_ARRANGED_DATA_FROM_R.csv")
cm1=pd.read_csv("CM1A_ARRANGED_DATA_FROM_R.csv")
xcm5=cm5['Expt']
ycm5=cm5['G121']
xcm1=cm1['Expt']
ycm1=cm1['G105']
m1,c1,r1,p1,se1=stats.linregress(xcm1,ycm1)
m5,c5,r5,p5,se5=stats.linregress(xcm5,ycm5)
fig=plt.figure(figsize=(10, 5),dpi=300)
ax1 = plt.subplot(121)
cm1lab="$"+('y=%2.2fx+%2.2f, r^2=%1.2f'%(m1,c1,r1**2))+"$"
ax1.plot(xcm1,ycm1,'^',mfc='none',mec='b',mew=1.2)
ax1.plot(xcm1, m1*xcm1+c1,'k--',linewidth=2,label=cm1lab)
plt.grid()
plt.ylabel(r'$\Delta G^{GB/SA}_{hyd}~$ 1.05*CM1A (kcal/mol)',fontsize=16)
plt.xlabel(r'$\Delta G^{Expt}_{hyd}~$ (kcal/mol)',fontsize=16)
ax1.legend( loc='upper left')
ax2 = plt.subplot(122)
cm5lab="$"+('y=%2.2fx+%2.2f, r^2=%1.2f'%(m5,c5,r5**2))+"$"
ax2.plot(xcm5,ycm5,'o',mfc='none',mec='r',mew=1.2)
ax2.plot(xcm5, m5*xcm5+c5,'k--',linewidth=2,label=cm5lab)
ax2.legend( loc='upper left')
plt.ylabel(r'$\Delta G^{GB/SA}_{hyd}~$ 1.21*CM5 (kcal/mol)',fontsize=16)
plt.xlabel(r'$\Delta G^{Expt}_{hyd}~$ (kcal/mol)',fontsize=16)
plt.grid()
fig.subplots_adjust(left  = 0.15,hspace = .001)
fig.tight_layout()
plt.savefig('GBSA_comp.pdf')

import numpy as np
import matplotlib.pyplot as plt

l = np.loadtxt('pmf.dat')

l = l.T

x = l[0] 
#print(x)

F = l[1]

Ferr = l[2]

#for i in range(len(Ferr)):
#    if Ferr[i] == 'nan' or Ferr[i] == -'nan'

#plt.errorbar(x, F, yerr=Ferr, c='b', ls='-', lw=2, elinewidth=2, capsize = 5, barsabove=True)
plt.plot(x, F, c='b', ls='-', lw=2)
plt.fill_between(x, F - Ferr, F + Ferr, facecolor='xkcd:lightblue')

#plt.title('PMF along $\Theta$ (HG)',fontsize=18)
plt.xlabel("Distance ($\AA$)",fontsize=18)
plt.ylabel("PMF (kcal/mol)",fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
#plt.ylim(0,25)
plt.tight_layout()
plt.show()
#plt.savefig('umbrella-pmf.pdf')


import numpy as np
import matplotlib.pyplot as plt

l = np.loadtxt('pmf.dat')

l = l.T

x = l[0] 

F = l[1]




plt.plot(x, F, c='r', ls='-', lw=2, label='Free Energy')

plt.xlabel("Distance ($\AA$)",fontsize=18)
plt.ylabel("PMF (kcal/mol)",fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=14)
plt.tight_layout()
plt.show()
#plt.savefig('umbrella-pmf.pdf')


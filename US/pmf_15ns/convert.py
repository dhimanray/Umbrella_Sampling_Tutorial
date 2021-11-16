import numpy as np

disc = 25000 #first 25000 points (5 ns) to be discarded

indices = [i for i in range(1,58)]
#indices.remove(54)
#indices.remove(53)

for j in indices:
    l = np.loadtxt('../data/US_%d.colvars.traj'%j)
    l = l.T
    f1 = open('US_data/US_%d_data.dat'%j,'w')
    for i in range(disc,len(l[1])):
        print(l[0,i],l[1,i],file=f1)
    f1.close()

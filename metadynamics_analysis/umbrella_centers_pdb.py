#Obtaining starting structures for milestoning simulation

import numpy as np
import MDAnalysis as md

u = md.Universe('ionized.pdb','MetaD_wrapped.dcd')


ever = u.select_atoms("all")

l = np.loadtxt('umbrella_centers.dat')
l = l.T

framelist = l[1]
rlist = l[0]

#print(rlist)

for i in range(len(framelist)):
    
    for ts in u.trajectory:

        if ts.frame == framelist[i]:
            with md.Writer('../umbrella_centers/us_%d.pdb'%(i+1)) as W:
                W.write(ever)
                print('pdb-written',rlist[i])


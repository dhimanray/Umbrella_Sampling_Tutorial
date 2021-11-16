import numpy as np
import MDAnalysis as md

u = md.Universe('ionized.pdb','MetaD_wrapped.dcd')

ab = u.select_atoms("bynum 1:6410")

spike = u.select_atoms("bynum 6411:6655")

for ts in u.trajectory:
    a = ab.centroid()
    b = spike.centroid()
    r = np.linalg.norm(a-b)
    #print(a,b)
    print(ts.frame,r)

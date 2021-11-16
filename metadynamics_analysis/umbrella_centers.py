import numpy as np

l = np.loadtxt('distance.dat')

distance = l[:,1]

initial = 32 #location of the first umbrella center
final = 60   #location of the last umbrella center
dx = 0.5     #spacing between umbrella centers

ucenters = np.arange(initial,final,dx)

for x0 in ucenters:
    idx = (np.abs(distance - x0)).argmin()
    frame = l[idx,0]
    colvar = l[idx,1]

    print('%0.1f'%x0,int(frame),colvar)

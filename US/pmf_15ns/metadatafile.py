indices = [i for i in range(1,58)]
#If some of the trajectories crash you can discard them in the following way
#indices.remove(54)
#indices.remove(53)


f1 = open('metadatafile.in','w')
for i in indices:
    print('US_data/US_%d_data.dat'%i, '%0.1f'%(31.5+0.5*float(i)), 4.0, 50.0, file=f1)
    #The above line wrtites the path of the data file, location of the center of the umbrella
    #harmonic potential, corresponding spring constant (targetForceConstant/(width**2) from 
    #colvars.in), and the correlation length (this can be compued from the autocorrelation 
    #function of the collective variable, bute we kept it constant at 50 (X 50 frames) for 
    #the sake of simplicity
f1.close()

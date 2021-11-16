indices = [i for i in range(1,58)]
#indices.remove(54)
#indices.remove(53)


f1 = open('metadatafile.in','w')
for i in indices:
    print('US_data/US_%d_data.dat'%i, '%0.1f'%(31.5+0.5*float(i)), 4.0, 50.0, file=f1)
f1.close()

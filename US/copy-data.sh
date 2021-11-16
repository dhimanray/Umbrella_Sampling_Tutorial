#!/bin/bash

for i in {1..57}
do
	cp US_$i/US.colvars.traj data/US_${i}.colvars.traj
done

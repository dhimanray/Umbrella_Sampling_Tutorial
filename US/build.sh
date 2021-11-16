#!/bin/bash

for i in {2..57}
do
	mkdir US_$i
	cd US_$i
	center=$(( 315 + 5*i ))e-1
	cp -r ../US_1/* .
	cp ../../umbrella_centers/us_$i.pdb .
	cp us_$i.pdb structure.pdb
	rm US.*
	rm *.out
	sed -i "s/US_1/US_${i}/g" job.sh
	sed -i "s/centers 32.0/centers $center/g" colvars.in
	cd ..
done

#!/bin/bash

for i in {2..57}
do
	cd US_$i
	qsub job.sh
	cd ..
done

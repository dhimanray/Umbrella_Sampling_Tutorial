#!/bin/csh
#PBS -A ucichem-gibbs
#PBS -q home-gibbs
#PBS -N ext_eq Run1
#PBS -l nodes=1:ppn=8
#PBS -l walltime=20:00:00
#PBS -o pbs.out
#PBS -e pbs.err
#PBS -V
#PBS -M dray1@uci.edu
#PBS -m a

module load cuda

cd /oasis/tscc/scratch/dray1/dhiman/Stem-binding-antibody-covid/s2p6/sars/US/US_1 
set namd_directory = /home/dray1/NAMD_2.14_Linux-x86_64-multicore-CUDA




# Running metadynamics
${namd_directory}/namd2 +idlepoll +isomalloc_sync +p 8 umbrella.inp > umbrella.out




#!/bin/bash
#PBS -N wff
#PBS -q batch 
#PBS -l nodes=1:ppn=48
#PBS -j oe  
#PBS -l walltime=1000:00:00

cd $PBS_O_WORKDIR
NP=`cat $PBS_NODEFILE | wc -l`

source /etc/profile
export LD_LIBRARY_PATH=/opt/intel/impi/5.0.1.035/intel64/lib:$LD_LIBRARY_PATH

YY=`date +%Y`
MM=`date +%m`
DD=`date +%d`
echo ' '$PBS_O_WORKDIR' Start at '`date`' '>>/home/wff/log-start

#mpirun -np $NP  -machinefile $PBS_NODEFILE /share/software/vasp.5.4.1_vtst/bin/vasp_std 2>&1 | tee log
mpirun -np $NP  -machinefile $PBS_NODEFILE /home/software/vasp.5.4.1_vtst/bin/vasp_std 2>&1 | tee log

YY=`date +%Y`
MM=`date +%m`
DD=`date +%d`
echo ' '$PBS_O_WORKDIR' Finished at '`date`' '>>/home/wff/log-finished


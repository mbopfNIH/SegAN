#!/bin/bash
#
# envSlurm.sh
#   -- Mike Bopf; 2018-06-14
#
# This is a Slurm sbatch job that runs an environment test that runs on the DGX by default. 
# Run the following command where $ indicates a the shell prompt:
#     $ sbatch envSlurm.sh
# To run on the VM partition do
#     $ sbatch --partition=VM envSlurm.sh
#

#SBATCH --workdir=/slurm_storage/mbopf/projects/SegAN
#SBATCH --output=slurmOut/slurm_%j.out
#SBATCH --error=slurmOut/slurm_%j.error
#SBATCH --job-name=BopfEnvTest
#SBATCH --partition=dgx1

env | sort
nvidia-smi
nvcc --version
uptime
python --version
ps -aux | grep mbopf | grep -v grep

python testSlurm.py


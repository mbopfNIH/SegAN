#!/bin/bash
#
# loopNvidia.sh
#   -- Mike Bopf; 2018-06-12
#
# This is a Slurm sbatch job that runs an environment test that runs on the DGX by default. 
# Run the following command where $ indicates a the shell prompt:
#     $ sbatch loopNvidia.sh
# To run on a particular VM node, do:
#     $ sbatch --partition=VM -w, nodelist=<nodename> loopNvidia.sh
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOTE: This job will loop INDEFINITELY and must be cancelled manually:
#     $ scancel <jobId>
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#SBATCH --workdir=.
#SBATCH --output=slurmOut/slurm_%j.out
#SBATCH --error=slurmOut/slurm_%j.error
#SBATCH --job-name=nvidiaTest
#SBATCH --partition=dgx1

nvidia-smi -l 20


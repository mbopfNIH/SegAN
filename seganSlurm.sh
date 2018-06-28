#!/bin/bash

#SBATCH --workdir=/slurm_storage/mbopf/projects/SegAN
#SBATCH --output=slurmOut/slurm_%j.out
#SBATCH --error=slurmOut/slurm_%j.error
#SBATCH --job-name=SegAN_slurm
#SBATCH --gres=gpu:1
#SBATCH --partition=dgx1 

export PATH=/slurm_storage/public/cuda8.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/slurm_storage/public/cuda8/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

env | sort
nvidia-smi
nvcc --version
python --version
python train.py --cuda --batchSize 4 --niter 200 --outpath /slurm_storage/mbopf/projects/SegAN/outputs

#!/bin/bash

#SBATCH --workdir=.
#SBATCH --output=slurmOut/slurm_%j.out
#SBATCH --error=slurmOut/slurm_%j.error
#SBATCH --job-name=predict
#SBATCH --gres=gpu:1
#SBATCH --partition=dgx1

export PATH=/slurm_storage/public/cuda8.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/slurm_storage/public/cuda8/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

# Dynamically create outputs directory
mkdir outputs_$SLURM_JOB_ID

#env | sort
#nvidia-smi
#nvcc --version
date
python predict.py --statedict NetS_epoch_60.pth --inputfile ksnInputs/DSCN4362.png --outdir outputs_$SLURM_JOB_ID
date

################################
# slurm aliases #
################################
alias sa='sacct --format="JobID,JobName,Partition,CPUTime,MaxRSS,State"'
alias sct='scontrol show jobid '
alias si='sinfo -al'
alias sidall='sinfo --partition=dgx1 -N -o=%all'
alias sq='squeue'
alias smid='srun --partition=dgx1 nvidia-smi'
alias smiv='srun nvidia-smi' # only displays first node
alias smidl='srun --partition=dgx1 nvidia-smi -l '

################################
# SegAN directory aliases #
################################
alias amit='cd /slurm_storage/public/AMIT'
alias sega='cd /slurm_storage/public/AMIT/projects/SegAN'

################################
# SlurmOut commands
################################
vo() {
    if [ "$1" == "" ]; then
        echo "tfo requires the processId as a parameter"
    else
        vim slurmOut/slurm_$1.out
    fi
}

to() {
    if [ "$1" == "" ]; then
        echo "tfo requires the processId as a parameter"
    else
        tail slurmOut/slurm_$1.out
    fi
}

ve() {
    if [ "$1" == "" ]; then
        echo "tfo requires the processId as a parameter"
    else
        vim slurmOut/slurm_$1.error
    fi
}

te() {
    if [ "$1" == "" ]; then
        echo "tfo requires the processId as a parameter"
    else
        tail slurmOut/slurm_$1.error
    fi
}

tfo() {
    if [ "$1" == "" ]; then
    echo "tfo requires the processId as a parameter"
    else
        tail -f slurmOut/slurm_$1.out
    fi
}

vl() {
    FILE=`\ls slurmOut/ | sort -r | head -1`
    vim slurmOut/$FILE
}

tl() {
    FILE=`\ls slurmOut/ | sort -r | head -1`
    tail slurmOut/$FILE
}

tfl() {
    FILE=`\ls slurmOut/ | sort -r | head -1`
    tail -f slurmOut/$FILE
}

export EDITOR=vim
export PATH=/slurm_storage/public/AMIT/anaconda3/bin:$PATH
umask 002

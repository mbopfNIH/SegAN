#
# testPython.py
#   -- Mike Bopf; 2018-06-10
#
# This is a simply Python program to verify that our environment is working correctly.
# Normally submitted via following command
#    $ sbatch envSlurm.sh
# But also can be done directly on the command line in the correct environment.
#
#    $ source activate py27torch02
#    $ python testPython.py

import numpy as np
import torch
from torchvision.transforms import Compose
import sys

print(sys.version)
print(np.__version__)
print(torch.__version__)

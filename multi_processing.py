#!/usr/bin/env python3
#@ Sujata Goswami
#  specifying number of CPUs per task
import os
from multiprocessing import Pool, cpu_count

# function you want to run in parallel:
def myfunction(a, b):
  print(a+b)
  return a + b

# list of tuples to serve as arguments to function:
args = [(1, 0), (2, 0), (3, 0), (4,0), (5,0), (6,0),(7,0),(8,0)]

# specify the number of CPUS per task for SLURMto use
number_of_cores = int(os.environ.get('SLURM_CPUS_PER_TASK', cpu_count()))
#number_of_cores = int(os.environ.get('SLURM_CPUS_PER_TASK', 3))
print('CPU cores:', number_of_cores)

# multiprocssing pool to distribute tasks to:
with Pool(number_of_cores) as pool:
    # distribute computations and collect results:
    results = pool.starmap(myfunction, args)

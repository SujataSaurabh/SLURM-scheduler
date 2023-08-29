# SLURM


SLURM is a scheduler and resource allocator tool
Full documentation is here -> https://slurm.schedmd.com/

Here, I am listing some frequently used commandsand their use with python programs. 

# if number of cpus per task for SLURM are in defined in python script    
sbatch <python-script>

# if number of cpus per task are defined with sbatch command 
sbatch --cpus-per-task 2 <python-script>

# for the number of processes that the program will launch. This can be on separate machines. 
sbatch --ntasks=8 <python-script>

# for the number of processes with specifying the number of cpus per task
sbatch --ntasks=8 --cpus-per-task=2 <python-script>

# using --mem-per-cpu to specify the memory per core, in MB (or G for GB)
sbatch --ntasks=8 --cpus-per-task=2 --mem-per-cpu=4G <python-script>



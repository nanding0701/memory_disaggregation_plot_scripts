## profile on Cori Haswell node:
module load vtune
srun -n1 vtune -collect memory-access -r toast.vtune.res -finalization-mode=deferred -data-limit=0 toast_benchmark_satellite --case tiny

## and then finalize on a login node: 
vtune -finalize -result-dir toast.vtune.res

## creates a summary report 
amplxe-cl -report hw-events -group-by=package -r toast.vtune.res/ -column=UNC_M_CAS_COUNT -format=csv -csv-delimiter=comma >> toast.vtune.csv

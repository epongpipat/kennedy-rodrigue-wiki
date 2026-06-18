(server-cortex)=

# Server: cortex

cortex (`cortex.cvl.utdallas.edu`) is a High-Performance Computing (HPC) server managed by {{cvltech}}.

## Interactive Commands (Testing & Debugging)

To run commands, compile software, or debug code interactively, you must launch an interactive session inside a partition (`dev` or `kenrod`). 

:::{warning}
Do not run computations on the login node. Running heavy jobs on the login node will slow down the server for all users and may crash the system.
:::

### Entering a Compute Node

:::{note}
The `dev` partition is preferred for testing and debugging interactive sessions.
:::

Launch an interactive session on the **dev** partition:

```bash
srun --partition=dev --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=4G --pty /bin/bash
```

Launch an interactive session on the **kenrod** partition:

```bash
srun --partition=kenrod --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=4G --pty /bin/bash
```

Alternatively, rather than memorizing or typing or memorizing the full `srun` command, you can run the interactive prompt helper:

```bash
srun-prompt
```

### Running the Code

Once inside the allocated partition, execute scripts and commands normally.

For example, to run a bash script:
```bash
bash /path/to/script.sh
```

For example, to run an AFNI command using its container:
```bash
module load afni
afni-exec 3dinfo /path/to/nifti/file
```

## Batch Jobs (SLURM)

cortex is managed by the [SLURM](https://slurm.schedmd.com/) workload manager. To schedule parallel batch jobs, write a shell script featuring SLURM directives and submit it using `sbatch`.

Common SLURM commands:

```bash
sbatch <script>          # Submit a job
squeue                   # View pending and running jobs
scancel <jobid>          # Cancel a specific job
scancel -u <username>    # Cancel all jobs for your user
```

Standard SLURM template header:

```bash
# ------------------------------------------------------------------------------
# slurm settings
# ------------------------------------------------------------------------------
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1        # can be increased if needed
#SBATCH --mem=4G                 # can be increased if needed
#SBATCH --partition=kenrod
#SBATCH --output=jid-%A_jname-%x.log
#SBATCH --mail-type=FAIL
#SBATCH --time=2-00:00:00        # day-hours:minutes:seconds format
#SBATCH --export=NONE            # export no environment variables
```

Submit a batch job script:

```bash
sbatch /path/to/script.sh
```

---

*For templates and code files, see the [Script Template](script-template).*

(server-ponyo)=

# Server: ponyo

ponyo is a standalone server (`cvlkrcompute1.utdallas.edu`).

## Direct Commands (Testing & Debugging)

Unlike cortex, you can run tests and debug scripts directly in your shell session on ponyo. 

For example, to run a bash script:

```bash
bash /path/to/script.sh
```

For example, to run an AFNI command using its container:

```bash
module load afni
afni-exec 3dinfo /path/to/nifti/file
```

## Batch Jobs (Sun Grid Engine)

ponyo features the [Sun Grid Engine (SGE)](https://en.wikipedia.org/wiki/Oracle_Grid_Engine) queue scheduler.

First, load the SGE module:

```bash
module load sge
```

Common SGE commands:

```bash
qsub <script>    # Submit a job
qstat            # View statuses of jobs
qdel <jobid>     # Cancel a job
qhold <jobid>    # Hold a queued job to prevent it from running
```

Standard SGE template header:

```bash
# ------------------------------------------------------------------------------
# sge settings
# ------------------------------------------------------------------------------
#$ -V
#$ -S /bin/bash
#$ -o jid-$JOB_ID-$TASK_ID_jname-$JOB_NAME.log
#$ -j y
#$ -m a \
#$ -M ${USER}@utdallas.edu
```

Submit an SGE batch job script with arguments:

```bash
qsub /path/to/script.sh --airc_id 3tb1111 --sub 0001 --date 20230101 --ses 3
```

---

*For templates and code files, see the [Script Template](script-template).*

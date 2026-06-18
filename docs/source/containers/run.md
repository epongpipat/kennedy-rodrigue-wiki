% run:

# Run Containers

## Prebuilt Containers (Preferred)

For convenience and standardized execution, we have prebuilt containers and corresponding modulefiles that handle mounting directories and setting up container environments automatically. This is the preferred method for running containers on our servers.

To use one of the prebuilt containers,

1. Load module of containerized software:
```bash
module load containers/<software>/<version>
```

2A. Run the following, replacing `<software>` with the name of the software and `<command>` with the command you want to run:
```bash
<software>-exec <command>
```

For example, to load the `freesurfer` version `8.2.0` container and run `recon-all`:
```bash
module load containers/freesurfer/8.2.0
freesurfer-exec recon-all --help
```

2B. Alternatively, if you want to access the container directly, run the following command:
```bash
<software>-run
```

For example, if you want to load the `r` version `4.2.1` container and enter into R directly:
```bash
module load containers/r/4.2.1
r-run
```

---

## Custom Container Execution (Advanced)

### Skeleton

```bash
singularity exec \
<singularity opts> \
/path/to/singularity_image.<simg|sif> \
<command>
```

### Common Singularity Options

```bash
--cleanenv                  # clean environment
-B <src>:[[dest[:opts]]     # bind paths to container
--env <env var>=<value>     # set environment variables in container
```

Please see `singularity exec --help` for more options and details

`-B` and `--env` can be used multiple times

Make sure to bind the path before setting the environment variable

### Example

An example of running `recon-all` from the `freesurfer` container with our script template format.

```bash
#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH --cpus-per-task 12
#SBATCH -o jid-%j_jname-%x.log
#SBATCH -p kenrod
#SBATCH --mem=8G                 # can be increased if needed

# ------------------------------------------------------------------------------
# modules
# ------------------------------------------------------------------------------
module load bashHelperKennedyRodrigue
source bashHelperKennedyRodrigueFunctions.sh
module load bashHelperBIDS
module load singularity
fs_ver="7.1.1"

# ------------------------------------------------------------------------------
# args/hdr
# ------------------------------------------------------------------------------
parse_args "${@}"
req_args=(study sub ses)
check_req_args ${req_args[@]}
print_header
set -e

# ------------------------------------------------------------------------------
# paths
# ------------------------------------------------------------------------------
if [[ -z ${root_dir} ]]; then
    root_dir=`get_root_dir kenrod`
    echo "root_dir: ${root_dir}"
    if [[ -z ${root_dir} ]]; then
        error_msg "root_dir is empty"
    fi
fi

declare -A in_paths
in_paths[fs_subj_dir]="${root_dir}/study-${study}/mri/anat_T1w/freesurfer${fs_ver}_container"
in_paths[T1w]=$(get_bids_paths --bids_dir $(get_bids_dir ${study}) --suffix T1w --extension .nii.gz --sub ${sub} --ses ${ses})
in_paths[T2w]=$(get_bids_paths --bids_dir $(get_bids_dir ${study}) --suffix T2w --extension .nii.gz --sub ${sub} --ses ${ses} --acq 3d)
in_paths[fs_simg]="${root_dir}/software/singularity_images/freesurfer-${fs_ver}.simg"
in_paths[tmpdir]="${root_dir}/software/singularity_images/tmp"
in_paths[cachedir]="${root_dir}/software/singularity_images/cache"
in_paths[fs_license]="/home/${USER}/fs_license.txt"

out_dir="${root_dir}/study-${study}/mri/anat_T1w/freesurfer${fs_ver}_container/sub-${sub}_ses-${ses}"


# ------------------------------------------------------------------------------
# check paths
# ------------------------------------------------------------------------------
check_in_paths ${in_paths[@]}

if [[ -d ${out_dir} ]] && [[ ${overwrite} -eq 0 ]]; then
    error_msg "file already exists and overwrite set to 0 (${out_dir})"
    exit 1
elif [[ -d ${out_dir} ]] && [[ ${overwrite} -eq 1 ]]; then
    warning_msg "overwriting, file already exists and overwrite set to 1 (${out_dir})"
    rm -r ${out_dir}
fi

# ------------------------------------------------------------------------------
# main
# ------------------------------------------------------------------------------
cmd="singularity exec \
--cleanenv \
-B ${in_paths[fs_subj_dir]} \
-B ${in_paths[T1w]} \
-B ${in_paths[T2w]} \
-B ${in_paths[tmpdir]} \
-B ${in_paths[cachedir]} \
-B ${in_paths[fs_license]} \
--env SUBJECTS_DIR=${in_paths[fs_subj_dir]} \
--env TMPDIR=${in_paths[tmpdir]} \
--env CACHEDIR=${in_paths[cachedir]} \
--env FS_LICENSE=${in_paths[fs_license]} \
${in_paths[fs_simg]} \
recon-all \
-subjid sub-${sub}_ses-${ses} \
-all \
-i ${in_paths[T1w]} \
-T2 ${in_paths[T2w]} \
-openmp 12"
echo -e "\ncommand:\n${cmd}\n"
eval ${cmd}

# ------------------------------------------------------------------------------
# print footer
# ------------------------------------------------------------------------------
print_footer
```

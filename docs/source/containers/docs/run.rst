.. run:

Run Containers
========

Skeleton
--------

.. code:: bash

    singularity exec \
    <singularity opts> \
    /path/to/singularity_image.<simg|sif> \
    <command>


Common Singularity Options
--------

.. code:: bash

    --cleanenv                  # clean environment
    -B <src>:[[dest[:opts]]     # bind paths to container
    --env <env var>=<value>     # set environment variables in container

Please see ``singularity exec --help`` for more options and details

``-B`` and ``--env`` can be used multiple times

Make sure to bind the path before setting the environment variable

Example
--------

An example of running ``recon-all`` from the ``freesurfer`` container with our script template format.

.. code:: bash

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
    module load singularity
    fs_ver="7.1.1"
    if [[ ${USER} == 'eep170030' ]] && [[ ${HOSTNAME} == 'login-01' ]]; then
        source /home/${USER}/.bash_profile
    fi

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
    in_paths[T1w]=`ls ${root_dir}/study-${study}/sourcedata/nii_software-dcm2niix_v-1.0.20210317/KENROD_PAMS_????????_${sub}_${wave}/sub-${sub}_ses-${ses}_acq-*-MPRAGE.nii.gz`
    in_paths[T2w]=`ls ${root_dir}/study-${study}/sourcedata/nii_software-dcm2niix_v-1.0.20210317/KENROD_PAMS_????????_${sub}_${wave}/sub-${sub}_ses-${ses}_acq-*-3D_T2.nii.gz`
    in_paths[fs_simg]="${root_dir}/software/singularity_images/freesurfer-${fs_ver}.simg"
    in_paths[tmpdir]="${root_dir}/software/singularity_images/tmp"
    in_paths[cachedir]="${root_dir}/software/singularity_images/cache"
    in_paths[fs_license]="/home/eep170030/fs_license.txt"

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
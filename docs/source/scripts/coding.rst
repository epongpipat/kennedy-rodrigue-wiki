######
Coding
######



.. note::
   This documentation is under active development. Last updated: 2024-09-12

.. contents:: Table of Contents
   :depth: 2
   :local:
   :backlinks: none

.. _script_template:

bash Script Template
======

.. code:: bash

    #!/bin/bash

    # ------------------------------------------------------------------------------
    # author:       Neo Shin
    # date:         2023-08-09
    # function:     script.sh --airc_id <airc_id> --sub <sub> --date <20230201> --ses <1|2|3>
    # description:  script to run through slurm or SGE
    # ------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------
    # parallel engine settings
    # ------------------------------------------------------------------------------
    # SLURM settings
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1        # can be increased if needed
    #SBATCH --mem=4G                 # can be increased if needed
    #SBATCH --partition=kenrod
    #SBATCH --output=jid-%A-%a_jname-%x.log
    #SBATCH --mail-type=FAIL
    #SBATCH --time=2-00:00:00        # day-hours:minutes:seconds format

    # SGE settings
    #$ -V
    #$ -S /bin/bash
    #$ -o jid-$JOB_ID-$TASK_ID_jname-$JOB_NAME.log      
    #$ -j y
    #$ -m a
    #$ -M ${USER}@utdallas.edu                          

    # ------------------------------------------------------------------------------
    # modules
    # ------------------------------------------------------------------------------
    module load bashHelperKennedyRodrigue
    source bashHelperKennedyRodrigueFunctions.sh

    # ------------------------------------------------------------------------------
    # args/hdr
    # ------------------------------------------------------------------------------
    parse_args "$@"
    req_args=(airc_id sub date ses)
    check_req_args ${req_args[@]}
    print_header
    set -e

    # ------------------------------------------------------------------------------
    # paths
    # ------------------------------------------------------------------------------
    root_dir=`get_root_dir kenrod`
    
    declare -A in_paths
    in_paths[nii_dir]="${root_dir}/to/the/input/directory"
    in_paths[code_dir]=`dirname $0`
    
    declare -A out_paths
    out_paths[nii_dir]="${root_dir}/to/the/output/directory"
    out_paths[test]="${root_dir}/to/the/output/file"

    # ------------------------------------------------------------------------------
    # check paths
    # ------------------------------------------------------------------------------
    # Stops script if the input directories do not exist
    check_in_paths ${in_paths[@]} 

    # Stop script if the output directory exists and overwrite was not enabled
    if [[ -d ${out_paths[nii_dir]} ]] && [ ! -z "$(ls -A ${out_paths[nii_dir]})" ] && [[ ${overwrite} -eq 0 ]]; then 
        echo "error: non-empty directory exists and overwrite set to 0 (out_paths: ${out_paths})"
        exit 1;
    fi

    # ------------------------------------------------------------------------------
    # main
    # ------------------------------------------------------------------------------
    cmd="<insert command here>"
    eval_cmd -c "${cmd}" -o ${out_paths[test]} --overwrite ${overwrite} --print ${print}

    # ------------------------------------------------------------------------------
    # end
    # ------------------------------------------------------------------------------
    print_footer

Command Example
+++++++++

To run this script:

.. code:: bash

    # SLURM
    sbatch /path/to/script/script.sh --airc_id 3tb1111 --sub 0001 --date 20230101 --ses 3

    # SGE
    module load sge
    qsub /path/to/script/script.sh --airc_id 3tb1111 --sub 0001 --date 20230101 --ses 3

.. _flex_uber:

Flex Uber
+++++

If scripts are created using the script template, consider making use of the `flex_uber <https://github.com/epongpipat/bashHelperKennedyRodrigue/wiki/flex_uber>`_ or `flex_wrapper <https://github.com/epongpipat/bashHelperKennedyRodrigue/wiki/flex_wrapper>`_ functions.

Common Issues
=====

1. End of line sequence for file is CRLF (Windows) rather than LF (Unix)
+++++

If you are getting the following error:

.. code:: bash

   line 1: $':\r': command not found
   line 5: syntax error near unexpected token `$'\r''

Then that means you have Windows-style line endings (occassionally caused by copy-pasting code from browsers).
To fix, go to terminal and type the following:

.. code:: bash

   vi -b /path/to/file

In ``vi``, type:

.. code:: bash

   :%s/\r$//
   :x

If you are trying to test your script that calls from a .csv file but the output looks like it's being cut off or being flipped, the .csv is possibly saved in Windows-style format.
Quick fix is to open up the csv file via Visual Studio Code (or other code editors), hover to the bottom right of the application, change CRLF to LF, and save the csv file.

.. build:

Build Containers
========

Option #1
---------

.. code:: bash

    group="freesurfer"
    software="freesurfer"
    ver="7.1.1"
    export SINGULARITY_TMPDIR="${root_dir}/software/singularity_images/tmp"
    export SINGULARITY_CACHEDIR="${root_dir}/software/singularity_images/cache"
    cmd="singularity build \
    ${root_dir}/software/singularity_images/${software}-${ver}.simg \
    docker://${group}/${software}:${ver}"
    echo -e "\ncommand:\n${cmd}\n"
    eval ${cmd}


Option #2
---------

If the first option doesn't work, try running this locally. Assuming that you have docker installed and working (https://docs.docker.com/get-docker/)

.. code:: bash

    group="freesurfer"
    software="freesurfer"
    ver="7.1.1"
    out_dir="${root_dir}/software/singularity_images"
    cmd="docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ${out_dir}:/output \
    --privileged \
    --tty \
    --rm \
    singularityware/docker2singularity \
    ${group}/${software}:${ver}"
    echo -e "\ncommand:\n${cmd}\n"
    eval ${cmd}

Option #3
---------

If the two first options don't work, obtain or create a docker file (advanced option). 

.. code:: bash

    docker build -t <docker_image_name> </path/to/Dockerfile>

To check if the image was created:

.. code:: bash

    docker images

Then, run option #2 to save the docker image as a singularity image

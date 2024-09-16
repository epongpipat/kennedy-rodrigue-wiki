######
Server
######

To access our server, make sure that you are connected to the UTD network:

* If you're on-campus, make sure that you are connected to the CometNet internet
* If you're working off-campus, make sure that you are connected to the UTD VPN by following the instructions `here <https://atlas.utdallas.edu/TDClient/30/Portal/Requests/ServiceDet?ID=167>`_

.. _map_network_drive:

Map Network Directory
-----------------

To map the ``kenrod/`` drive (formerly, the ``shared/`` drive) to your local computer:

For Mac users, go to ``Finder`` > ``Go`` > ``Connect to Server``, enter the following and press ``Connect``:

.. code::

    smb://smb.cvl.utdallas.edu/groups/kenrod


For Windows users, follow the instructions `here <https://atlas.utdallas.edu/TDClient/30/Portal/KB/ArticleDet?ID=51>`_ and enter the following for ``Folder`` field:

.. code::

    \\smb.cvl.utdallas.edu\groups/kenrod

.. _login:

Login with Command Line
-----

For Max users, we can use the ``Terminal`` app, which is already included in Macs

For Windows users, install either `Putty <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_ or `MobaXterm <https://mobaxterm.mobatek.net/download-home-edition.html>`_

You can login by typing the following:

.. code:: bash

    ssh -Y <user>@<hostname>

User is your UTD Net ID and hostname can be one of the following:

* ``cvlkrcompute1.utdallas.edu`` or ``ponyo.utdallas.edu``
* ``cortex.cvl.utdallas.edu``

.. _software:

Software
--------

To see available software, run:

.. code:: bash

    module avail

To load available software, run:

.. code:: bash

    module load <software>

To unload software, run:

.. code:: bash

    module unload <software>

.. _parallel:

Parallel Jobs
--------

To run parallel jobs, we can use `SLURM (preferred) <https://slurm.schedmd.com/quickstart.html>`_ or `Sun Grid Engine (old) <http://star.mit.edu/cluster/docs/0.93.3/guides/sge.html>`_.

`Parallel Script Template <https://kennedy-rodrigue-wiki.readthedocs.io/en/latest/scripts/ScriptTemplates.html#parallel-script-template>`_

SLURM
+++++++

To use ``SLURM``, first access the server via ``cortex.cvl.utdallas.edu``.

Basic SLURM commands:

.. code:: bash
    
    sbatch <script>          # Submit a job
    squeue                   # Show see pending jobs
    scancel <jobid>          # cancel specific job
    scancel -u <username>    # Cancel all jobs

Common SLURM settings:

.. code:: bash

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
    #SBATCH --export=NONE            # ALL or comma-separated environment variables

Command Example:

.. code:: bash

    sbatch /path/to/script.sh

Sun Grid Engine
+++++++

To use ``Sun Grid Engine``, run the following on ``cvlkrcompute1.utdallas.edu`` (or ``ponyo.utdallas.edu``):

.. code:: bash

    module load sge

Basic SGE commands:

.. code:: bash

    qsub <script>    # Submit a job
    qstat            # Show statuses of jobs
    qdel <jobid>     # Cancel a job
    qhold <jobid>    # Place a hold on queued job to prevent it from running

Common SGE settings:

.. code:: bash

    # ------------------------------------------------------------------------------
    # sge settings
    # ------------------------------------------------------------------------------
    #$ -V
    #$ -S /bin/bash
    #$ -o jid-$JOB_ID-$TASK_ID_jname-$JOB_NAME.log
    #$ -j y
    #$ -m a \
    #$ -M ${USER}@utdallas.edu

Command Example:

.. code:: bash

    qsub /path/to/script.sh --airc_id 3tb1111 --sub 0001 --date 20230101 --ses 3

.. _ood:

Open OnDemand (OOD)
-----

Open OnDemand allows users to access terminal via a web browser or use programs that require GUI interfaces (e.g., `SPM`, `freeview`, or `fslview`).


Login using the link below using your UTD credentials.

https://ood.cvl.utdallas.edu/

To use terminal:

``Clusters`` > ``>_cortex Shell Access``

To use programs that require GUI interface:

``My Interactive Sessions`` > ``cortex Desktop`` > adjust settings as needed and click ``Launch``


.. _tech_info:

Profiles
------

Consider adding these global lab profiles to your user profile. You can copy and paste either into its respective profile file by using the :code:`nano` function (e.g., :code:`nano ~/.bash_profile`)

1. :code:`~/.bash_profile`

.. code:: bash

    if [[ ${HOSTNAME} =~ 'cvlkrcompute' ]]; then
      export root_dir='/cvl/kenrod'
    else
      export root_dir='/mfs/cvl/groups/kenrod'
    fi
    source ${root_dir}/server/profiles/global/bash_profile.sh

2. :code:`~/.Rprofile`

.. code:: R

    if (Sys.info()[['nodename']] == 'cvlkrcompute1.utdallas.edu') {
            root_dir <- '/cvl/kenrod'
    } else {
            root_dir <- '/mfs/cvl/groups/kenrod'
    }
    source(sprintf('%s/server/profiles/global/r_profile.R', root_dir))



Technical Information
------

.. csv-table:: 
   :header: "hostname", "alias", "cores", "memory", "cortex node"

    "cvlkrcompute1", "ponyo", 32, "132GB", ""
    "cvlkrcompute2", "totoro", 32, "132GB", "compute-16"
    "cvlkrcompute3", "kiki", 12, "65GB", "compute-02"

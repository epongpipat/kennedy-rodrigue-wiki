.. _T1w:

T1w
=============

.. _T1w_preproc:

Preprocessing
-------------

#. Run freesurfer and manual interventions

#. Setup

   .. code:: bash

      module load bashHelperKennedyRodrigue
      root_dir='get_root_dir kenrod'
      code_dir="${root_dir}/software/scripts/eep170030/study-jlbs/mri/anat/T1w"

#. Convert freesurfer ROIs from surfaces to volumes

   .. code:: bash

      bash ${code_dir}/s01_freesurfer_roi_from_surface_to_volume_faster.sh

   
   ROIs:

   * ``brainmask.mgz``
   * ``aparc+aseg.mgz``
   * ``aparc.a2009s+aseg.mgz``
   * ``wmparc.mgz``


#. Warp volumetric ROIs from freesurfer-space to native T1w space

   .. code:: bash

      bash ${code_dir}/s02_warp_freesurfer_roi_from-fsnative_to-T1w-native.sh

#. Preprocess T1w

   .. code:: bash

      bash ${code_dir}/s03_preprocess_T1w.sh

   
   The code performs the following:
   
   * brain extraction (using ANTs, FSL, and Freesurfer)
   * combines brain masks
   * warps the brain to MNI152 space
   * creates tissue segments (FSL's fast)

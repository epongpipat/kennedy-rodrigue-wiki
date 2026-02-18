.. _fmri:

fMRI processing
#####

fMRI Pipeline Description
*****

#. Ensure processed T1w (post-freesurfer processing)

#. Ensure functional data (including local) are copied over

To run this pipeline, please use ``flex_uber`` and use the ``study-pams/mri/func/task-circles_bold/preprocessing/scripts.txt`` pipeline.

Then, use ``flex_uber`` and use the ``study-pams/mri/func/task-circles_bold/first-level/scripts.txt`` pipeline

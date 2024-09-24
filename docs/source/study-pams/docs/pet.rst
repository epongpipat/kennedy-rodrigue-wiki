.. _pet:

pet
=====

Amyloid Pipeline Description
-----

#. Ensure processed T1w (post-freesurfer processing)

#. Correct for motion

#. Warp PET from native space to T1w space (coregister)

#. Warp DK Atlas from T1w space to PET space

#. Create mask and obtain PET reference values

#. Calculate SUVR image

#. Create cortical ROIs

#. Extract SUVR from cortical ROIs

To run this pipeline, please use ``flex_uber`` and use the ``study-pams/pet/scripts.txt`` pipeline
